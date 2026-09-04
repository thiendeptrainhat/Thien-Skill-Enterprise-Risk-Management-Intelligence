/** Optional Office exporter. Requires @oai/artifact-tool and docx supplied by host.
 * Run a byte-identical copy in a temporary module directory whose node_modules
 * points to the approved runtime. No installation, network or implicit overwrite.
 * Input is report.json produced by report.py; not an unvalidated raw engagement.
 */
import fs from 'node:fs/promises';
import path from 'node:path';
import {Workbook, SpreadsheetFile, Presentation, PresentationFile} from '@oai/artifact-tool';
import {Document, Packer, Paragraph, TextRun, HeadingLevel, Header, Footer, ImageRun} from 'docx';

const [input,out,logo,preview]=process.argv.slice(2);
if(!input||!out||!logo||!preview) throw Error('Usage: export_office.mjs report.json output-dir logo.png temporary-preview-dir');
const d=JSON.parse(await fs.readFile(input,'utf8'));
if(d.validation?.status!=='VALID'||!d.source_sha256||!d.snapshot)throw Error('Validated report.json required');
await fs.mkdir(out,{recursive:true});await fs.mkdir(preview,{recursive:true});
for(const name of ['report.xlsx','report.docx','report.pptx']){
  try{await fs.access(path.join(out,name));throw Error('Refusing overwrite: '+name);}catch(e){if(e.code!=='ENOENT')throw e;}
}
const logoBytes=await fs.readFile(logo), brand='Thiện’s Skill · ERM', navy='#142D4E', gold='#AD7E22';
const meta=`${d.context.entity} | ${d.context.as_of} | ${d.context.horizon} | ${d.context.currency} (${d.context.unit}) | v${d.context.version}`;
const label=d.context.synthetic?'SYNTHETIC · DỮ LIỆU THỬ NGHIỆM':'DỰ THẢO · CHƯA PHÊ DUYỆT';
const toText=v=>v===null||v===undefined?'UNKNOWN':typeof v==='object'?JSON.stringify(v):String(v);
const cell=v=>typeof v==='string'&&/^[=+@\-]/.test(v)?"'"+v:v;
const col=i=>{let s='';for(i++;i;i=Math.floor((i-1)/26))s=String.fromCharCode(65+(i-1)%26)+s;return s;};

// Excel has 15 significant decimal digits. Preserve text fields; normalize only
// typed quantitative cells. Reject excess precision before writing any artifacts.
function decimalKey(value){
 const m=String(value).trim().match(/^([+-]?)(?:(\d+)(?:\.(\d*))?|\.(\d+))(?:[eE]([+-]?\d+))?$/);
 if(!m)throw Error('Invalid numeric cell: '+value);
 let digits=((m[2]||'')+(m[3]??m[4]??'')).replace(/^0+/,'');
 let exponent=Number(m[5]||0)-(m[3]??m[4]??'').length;
 if(!digits)return {key:'0',digits:0};
 const zeros=digits.match(/0*$/)[0].length;digits=digits.slice(0,digits.length-zeros);exponent+=zeros;
 return {key:(m[1]==='-'?'-':'')+digits+'e'+exponent,digits:digits.length};
}
function excelNumber(value,field){
 if(value===null||value===undefined)return null;
 const original=decimalKey(value),n=Number(value);
 if(!Number.isFinite(n)||Math.abs(n)>1e30||original.digits>15||decimalKey(n).key!==original.key)
  throw Error('Excel precision limit at '+field+': use at most 15 significant decimal digits; retain exact value in report.json and choose an explicit rescaling/rounding policy.');
 return n;
}
const numericFields={KRI:['value'],Rules:['threshold'],Losses:['amount'],Observations:['value'],Treatments:['cost']};

const w=Workbook.create();
const views=[
 ['Register',d.risks.map(r=>({id:r.id,title:r.title,owner:r.owner,cause:r.cause,event:r.event,impact:r.impact,objective:r.objective,appetite:r.appetite.known_status,incomplete:r.appetite.incomplete,evidence:r.evidence_ids}))],
 ['Assessment',d.risks.flatMap(r=>r.assessments)], ['Taxonomy',d.snapshot.taxonomy],
 ['KRI',d.metrics.map(m=>({id:m.id,label:m.label,value:m.value,quality:m.quality,approval:m.approval,status:m.status,unit:m.unit,currency:m.currency,horizon:m.horizon,observed_at:m.observed_at,action:m.action}))],
 ['Rules',d.metrics.flatMap(m=>m.rules.map(r=>({metric:m.id,...r})))],
 ['Controls',d.snapshot.controls],['Scenarios',d.snapshot.scenarios],['Treatments',d.snapshot.treatments],
 ['Losses',d.snapshot.losses],['Observations',d.snapshot.observations],['Sources',d.snapshot.sources],
 ['Methods',d.snapshot.methods],['Dependencies',d.snapshot.dependencies],['Handoffs',d.snapshot.handoffs],
 ['Warnings',d.validation.warnings.map((warning,i)=>({id:'Q'+(i+1),warning}))]
];
for(const [name,records] of views)for(const [i,r] of records.entries())
 for(const field of numericFields[name]??[])excelNumber(r[field],`${name}[${i}].${field}`);
const summary=w.worksheets.add('Summary'), ranges=[];
for(const [name,records] of views){
 const sh=w.worksheets.add(name);sh.showGridLines=false;
 const fields=records.length?Object.keys(records[0]):['No data'];
 sh.getRangeByIndexes(0,0,1,Math.max(fields.length,4)).merge();sh.getRange('A1').values=[[name+' · '+label]];
 sh.getRangeByIndexes(1,0,1,Math.max(fields.length,4)).merge();sh.getRange('A2').values=[[meta]];
 const matrix=[fields,...records.map(r=>fields.map(k=>(numericFields[name]??[]).includes(k)?excelNumber(r[k],name+'.'+k):cell(typeof r[k]==='object'&&r[k]!==null?JSON.stringify(r[k]):r[k]??null)))];
 const range=sh.getRangeByIndexes(2,0,matrix.length,fields.length);range.values=matrix;
 range.format.font={name:'Arial',size:11};range.format.wrapText=true;range.format.columnWidth=28;
 sh.getRangeByIndexes(2,0,1,fields.length).format={fill:navy,font:{bold:true,color:'#FFFFFF'},rowHeight:30};
 if(records.length)sh.tables.add(`A3:${col(fields.length-1)}${records.length+3}`,true,name+'Table');
 sh.getRange('A1').format.font={name:'Arial',size:18,bold:true,color:navy};sh.getRange('A1').format.rowHeight=32;
 sh.getRange('A2').format.rowHeight=26;sh.freezePanes.freezeRows(3);
 for(let r=0;r<records.length;r++){
  const max=Math.max(...matrix[r+1].map(v=>toText(v).length));
  sh.getRangeByIndexes(r+3,0,1,fields.length).format.rowHeight=Math.min(360,Math.max(38,Math.ceil(max/27)*15));
 }
 ranges.push({name,range:`A1:${col(fields.length-1)}${Math.max(4,records.length+3)}`});
}
// Status is formula-driven from displayed predicates. Method changes require revalidation.
const kr=w.worksheets.getItem('KRI');let ruleRow=4;
for(let i=0;i<d.metrics.length;i++){
 const m=d.metrics[i],r=i+4, clauses=[];
 for(const rule of m.rules){
  const rr=ruleRow++,threshold=`'Rules'!C${rr}`,op=`'Rules'!B${rr}`;
  clauses.push({rank:{warning:1,breach:2,capacity_breach:3}[rule.severity],
   expr:`IF(OR(AND(${op}=">",C${r}>${threshold}),AND(${op}=">=",C${r}>=${threshold}),AND(${op}="<",C${r}<${threshold}),AND(${op}="<=",C${r}<=${threshold})),'Rules'!D${rr},__NEXT__)`});
 }
 let f='"within"';for(const c of clauses.sort((a,b)=>a.rank-b.rank))f=c.expr.replace('__NEXT__',f);
 if(!clauses.length)f='"UNKNOWN"';
 f=`=IF(E${r}<>"approved","DRAFT",IF(OR(D${r}<>"valid",ISBLANK(C${r})),"UNKNOWN",${f}))`;
 kr.getRange(`F${r}`).formulas=[[f]];
}
if(d.metrics.length){kr.getRange(`F4:F${d.metrics.length+3}`).conditionalFormats.add('containsText',{text:'breach',format:{font:{color:'#A42324',bold:true}}});}
summary.showGridLines=false;summary.getRange('A1:F1').merge();summary.getRange('A1').values=[['ERM · Quyết định điều hành']];
summary.getRange('A1').format={font:{name:'Arial',size:22,bold:true,color:navy},rowHeight:38};
summary.getRange('A2:F2').merge();summary.getRange('A2').values=[[label]];
summary.getRange('A3:F3').merge();summary.getRange('A3').values=[[meta]];
summary.getRange('A5:B8').values=[['Số risk',null],['Metric breach',null],['Metric UNKNOWN/DRAFT',null],['Trạng thái đã biết',d.summary.known_status]];
const end=d.metrics.length+3;
summary.getRange('B5').formulas=[[`=COUNTA('Register'!A4:A${Math.max(4,d.risks.length+3)})`]];
summary.getRange('B6').formulas=[[`=COUNTIF('KRI'!F4:F${Math.max(4,end)},"breach")+COUNTIF('KRI'!F4:F${Math.max(4,end)},"capacity_breach")`]];
summary.getRange('B7').formulas=[[`=COUNTIF('KRI'!F4:F${Math.max(4,end)},"UNKNOWN")+COUNTIF('KRI'!F4:F${Math.max(4,end)},"DRAFT")`]];
summary.getRange('A10:F12').merge();summary.getRange('A10').values=[[d.context.decision]];
summary.getRange('A14:F16').merge();summary.getRange('A14').values=[['Snapshot đã validate; xem sheet Warnings để biết khoảng trống bằng chứng. Thay dữ liệu/method cần chạy lại validator; các output định lượng ngoài công thức trong workbook là kết quả model nhập, không phải công thức Excel.']];
summary.getRange('A18:F19').merge();summary.getRange('A18').values=[['SHA-256 '+d.source_sha256]];
summary.getRange('A2:F19').format.wrapText=true;summary.getRange('A2:F19').format.font={name:'Arial',size:11};
summary.getRange('A1:F19').format.columnWidth=22;summary.getRange('A2:F19').format.rowHeight=24;
summary.getRange('A5:A8').format.font={bold:true,color:navy};summary.getRange('B5:B7').setNumberFormat('0');
summary.images.add({dataUrl:'data:image/png;base64,'+logoBytes.toString('base64'),anchor:{from:{row:4,col:4},extent:{widthPx:110,heightPx:110}}});
const checks={counts:summary.getRange('B5:B7').values,statuses:kr.getRange(`F4:F${Math.max(4,end)}`).values};
if(d.metrics.length&&JSON.stringify(checks.statuses.flat())!==JSON.stringify(d.metrics.map(m=>m.status)))throw Error('Excel KRI formula reconciliation failed');
if(JSON.stringify(checks.counts.flat())!==JSON.stringify([d.summary.risk_count,d.summary.confirmed_breaches,d.summary.unresolved_metrics]))throw Error('Excel summary reconciliation failed');
if(process.argv.includes('--check')){console.log(JSON.stringify({checks,numeric_policy:'15 significant decimal digits; unsafe precision rejected'}));process.exit(0);}
const scan=await w.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A',options:{useRegex:true,maxResults:30},maxChars:3000});
await fs.writeFile(path.join(preview,'workbook-check.json'),JSON.stringify({checks,formulaScan:scan.ndjson},null,2));
for(const r of [{name:'Summary',range:'A1:F19'},...ranges]){
 const blob=await w.render({sheetName:r.name,range:r.range,scale:1,format:'png'});
 await fs.writeFile(path.join(preview,'xlsx-'+r.name+'.png'),new Uint8Array(await blob.arrayBuffer()));
}
await (await SpreadsheetFile.exportXlsx(w)).save(path.join(out,'report.xlsx'));

// Word: standard_business_brief preset, memo_masthead without decorative rule.
const para=(text,heading,pageBreakBefore)=>new Paragraph({text,heading,style:heading?undefined:'Normal',keepNext:!!heading,pageBreakBefore});
const children=[new Paragraph({children:[new ImageRun({data:logoBytes,type:'png',transformation:{width:68,height:68}})]}),
 para('BÁO CÁO RỦI RO DOANH NGHIỆP',HeadingLevel.TITLE),para(label),para(meta),
 para('Quyết định cần xử lý',HeadingLevel.HEADING_1),para(d.context.decision),
 para(`${d.summary.risk_count} risks; ${d.summary.confirmed_breaches} metric breaches; ${d.summary.unresolved_metrics} metric chưa đủ. Trạng thái đã biết: ${d.summary.known_status}.`),
 para('Risk profile',HeadingLevel.HEADING_1)];
for(const r of d.risks){children.push(para(`${r.id} · ${r.title}`,HeadingLevel.HEADING_2),para(`${r.cause} → ${r.event} → ${r.impact}. Owner: ${r.owner}.`),
 para('Assessment: '+r.assessments.map(a=>`${a.basis}/${a.method_id}: ${a.rating??'UNKNOWN'} (${a.approval}); I=${a.impact??'—'}, L=${a.likelihood??'—'}`).join('; ')),
 para(`Appetite: ${r.appetite.known_status}; incomplete=${r.appetite.incomplete}. Evidence: ${r.evidence_ids.join(', ')}.`));}
children.push(para('Appetite và KRI',HeadingLevel.HEADING_1,true));
for(const m of d.metrics)children.push(para(`${m.id} · ${m.label}`,HeadingLevel.HEADING_2),para(`${toText(m.value)} ${m.unit} ${m.currency} · ${m.status} · ${m.observed_at??'missing'}. ${m.action}`),para('Rules: '+m.rules.map(r=>`${r.severity} ${r.op} ${r.threshold}`).join('; ')));
children.push(para('Scenario và tổn thất',HeadingLevel.HEADING_1));
for(const s of d.snapshot.scenarios)children.push(para(`${s.id} · ${s.label} (${s.kind})`,HeadingLevel.HEADING_2),para(s.result),para(s.baseline+'; '+s.assumptions.join('; ')),para(s.limitations));
for(const g of d.loss_totals)children.push(para(`Economic losses: ${g.total} ${g.unit} ${g.currency}; ${g.scope}/${g.horizon}; loại nội bộ ${g.eliminated}. Không cộng cash balance vào loss.`));
children.push(para('Treatment',HeadingLevel.HEADING_1,true));
for(const t of d.snapshot.treatments)children.push(para(`${t.id} · ${t.action}`,HeadingLevel.HEADING_2),para(`${t.owner} | ${t.deadline} | ${t.status} | ${t.cost} ${t.currency}`),para(`${t.expected_benefit} (${t.benefit_basis}). ${t.resource_constraint}. Secondary risk: ${t.secondary_risk}.`));
for(const t of d.snapshot.treatments)children.push(para(`${t.id} · No-action và target`,HeadingLevel.HEADING_2),
 para('No-action: '+(t.no_action_case??'Chưa đủ dữ liệu')),para('Target: '+(t.target??'Chưa đủ dữ liệu')),
 para('Target assessment IDs: '+((t.target_assessment_ids??[]).join(', ')||'Chưa cung cấp')));
children.push(para('Khoảng trống bằng chứng',HeadingLevel.HEADING_1));
for(const warning of d.validation.warnings)children.push(para(warning));
if(!d.validation.warnings.length)children.push(para('Không có warning cấu trúc; không thay review nghiệp vụ.'));
children.push(para('Phương pháp và bằng chứng',HeadingLevel.HEADING_1));
for(const m of d.snapshot.methods)children.push(para(`${m.id}/${m.version} · ${m.approval}. ${m.rating_basis}. Horizon ${m.horizon}.`));
for(const s of d.snapshot.sources)children.push(para(`${s.id}: ${s.title}; ${s.locator}; v${s.version}; ${s.status}; ${s.limitations}`));
const doc=new Document({styles:{default:{
 document:{run:{font:'Calibri',size:22,color:'142D4E'},paragraph:{spacing:{before:0,after:120,line:264}}},
 title:{run:{size:46,bold:true,color:'000000'},paragraph:{spacing:{before:0,after:160}}},
 heading1:{run:{size:32,bold:true,color:'2E74B5'},paragraph:{spacing:{before:320,after:160},keepNext:true}},
 heading2:{run:{size:26,bold:true,color:'2E74B5'},paragraph:{spacing:{before:240,after:120},keepNext:true}}},
 },
 // docx paragraphStyles does not serialize w:default; use externalStyles
 // to declare Normal explicitly as the default paragraph style.
 externalStyles:'<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:style w:type="paragraph" w:styleId="Normal" w:default="1"><w:name w:val="Normal"/><w:next w:val="Normal"/><w:pPr><w:spacing w:before="0" w:after="120" w:line="264"/></w:pPr><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:eastAsia="Calibri" w:cs="Calibri"/><w:color w:val="142D4E"/><w:sz w:val="22"/></w:rPr></w:style></w:styles>',

 sections:[{properties:{page:{size:{width:12240,height:15840},margin:{top:1440,bottom:1440,left:1440,right:1440,header:720,footer:720}}},
 headers:{default:new Header({children:[para(brand+' · '+label)]})},footers:{default:new Footer({children:[new Paragraph({children:[new TextRun({text:d.context.id+' · v'+d.context.version,size:18}),new TextRun({text:'Snapshot SHA-256: '+d.source_sha256,break:1,size:14})],spacing:{after:0,line:220}})]})},children}]});
await fs.writeFile(path.join(out,'report.docx'),await Packer.toBuffer(doc),{flag:'wx'});

const p=Presentation.create({slideSize:{width:1280,height:720}});
function text(slide,value,x,y,width,height,size=26,bold=false,color=navy){
 const s=slide.shapes.add({geometry:'textbox',position:{left:x,top:y,width,height},fill:'none',line:{fill:'none',width:0}});
 s.text=value;s.text.style={fontFamily:'Arial',fontSize:size,bold,color};return s;
}
function slide(title,body,notes){
 if(title.length>85||body.length>750)throw Error('Slide content needs custom pagination/layout; do not truncate.');
 const s=p.slides.add();s.background.fill='#FFFFFF';text(s,label,72,36,1136,32,18,true,gold);
 text(s,title,72,103,1136,130,48,true);text(s,body,72,267,1136,300,27);
 text(s,meta,72,635,1136,48,18);s.speakerNotes.textFrame.setText(notes+'\n[Sources]\n'+d.snapshot.sources.map(x=>x.id+': '+x.locator).join('\n')+'\nOwner-supplied TDTN logo.\nSnapshot SHA-256: '+d.source_sha256);return s;
}
const cover=slide('Quyết định về rủi ro doanh nghiệp',`${d.summary.risk_count} risks · ${d.summary.confirmed_breaches} metric breaches · ${d.summary.unresolved_metrics} metric chưa đủ\n\n${d.context.decision}`,JSON.stringify(d.summary));
cover.images.add({blob:logoBytes.buffer.slice(logoBytes.byteOffset,logoBytes.byteOffset+logoBytes.byteLength),contentType:'image/png',alt:'TDTN',fit:'contain',position:{left:1090,top:480,width:110,height:110}});
for(const r of d.risks)slide(r.id+' · '+r.title,`${r.cause} → ${r.event}\n${r.impact}\n\nAppetite: ${r.appetite.known_status}${r.appetite.incomplete?' · dữ liệu chưa đầy đủ':''}\nOwner: ${r.owner}`,JSON.stringify({risk:r,metrics:d.metrics.filter(m=>m.risk_ids.includes(r.id))}));
for(const s of d.snapshot.scenarios)slide(s.id+' · '+s.label,s.result+'\n\n'+s.limitations,JSON.stringify({scenario:s,loss_totals:d.loss_totals}));
for(const t of d.snapshot.treatments)slide(t.id+' · Quyết định nguồn lực',`${t.action}\n${t.owner} · ${t.deadline} · ${t.status}\n\n${t.resource_constraint}\n${t.expected_benefit} (${t.benefit_basis})\nSecondary risk: ${t.secondary_risk}`,JSON.stringify(t));
for(const t of d.snapshot.treatments)slide(t.id+' · No-action và target',
 'No-action: '+(t.no_action_case??'Chưa đủ dữ liệu')+'\n\nTarget: '+(t.target??'Chưa đủ dữ liệu')+
 '\n\nTarget assessment IDs: '+((t.target_assessment_ids??[]).join(', ')||'Chưa cung cấp'),JSON.stringify(t));
let warningPage=[];
for(const warning of d.validation.warnings){
 if(warning.length>650)throw Error('Warning requires custom pagination; do not truncate.');
 if([...warningPage,warning].join('\n\n').length>650){slide('Khoảng trống bằng chứng',warningPage.join('\n\n'),JSON.stringify(warningPage));warningPage=[];}
 warningPage.push(warning);
}
if(warningPage.length)slide('Khoảng trống bằng chứng',warningPage.join('\n\n'),JSON.stringify(warningPage));
for(const [i,s] of p.slides.items.entries()){
 const img=await p.export({slide:s,format:'png',scale:1});await fs.writeFile(path.join(preview,`slide-${i+1}.png`),new Uint8Array(await img.arrayBuffer()));
 const layout=await s.export({format:'layout'});await fs.writeFile(path.join(preview,`slide-${i+1}.json`),await layout.text());
}
await (await PresentationFile.exportPptx(p)).save(path.join(out,'report.pptx'));
console.log(JSON.stringify({xlsx:'created',docx:'created_visual_review_required',pptx:'created',checks,slides:p.slides.items.length}));
