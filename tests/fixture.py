"""Synthetic engagement used by quantitative tests and all four artifact samples."""
def engagement():
    ctx = dict(id='SYN-ERM-01', version='1', as_of='2026-09-03', entity='Công ty Mẫu',
               scope='Group', jurisdictions=['VN', 'SG'], currency='VND', horizon='Q4-2026',
               unit='triệu', industry='FMCG', objectives=['Bảo vệ cash và khả năng giao hàng'],
               materiality='Synthetic: ảnh hưởng cash/giao hàng cấp tập đoàn', synthetic=True,
               decision='Quyết định nguồn lực dự phòng và xử lý breach thanh khoản; chưa phê duyệt.')
    data = {k: [] for k in ['sources','taxonomy','risks','methods','assessments','metrics',
                          'observations','controls','scenarios','losses','dependencies','treatments','handoffs']}
    data['context'] = ctx
    data['sources'] = [dict(id='SYN1',title='Fixture synthetic của dự án ERM',locator='synthetic:fixture-v1',
        version='1',accessed_at='2026-09-03',kind='synthetic',status='current',replaced_by=None,
        limitations='Không phải dữ liệu doanh nghiệp thực hoặc benchmark ngành.')]
    data['taxonomy'] = [dict(id='T0',label='Enterprise exposure',level=0,parent_id=None),
                        dict(id='T1',label='Continuity và liquidity',level=1,parent_id='T0')]
    titles = ['Gián đoạn nguồn cung', 'Thiếu hụt thanh khoản', 'Chất lượng và thu hồi']
    events = ['Cảng chung dừng dài hơn buffer', 'Thu tiền trễ hơn hạn thanh toán', 'Batch phải thu hồi']
    for i in range(3):
        data['risks'].append(dict(id=f'R{i+1}',taxonomy_id='T1',title=titles[i],
            cause=['Hai suppliers cùng cảng','Khách hàng trả chậm','Sai lệch quá trình đóng gói'][i],
            event=events[i],impact=['Thiếu hàng và giảm contribution','Cash xuống dưới mức sàn','Chi phí recall và mất service'][i],
            objective=ctx['objectives'][0],owner=['COO','CFO','Quality Director'][i],scope='Group',
            exposure=['1.000 đơn vị demand','20.000 triệu VND cash','100 đơn vị recall'][i],evidence_ids=['SYN1']))
    data['methods'] = [dict(id='M1',version='synthetic-1',approval='approved',approved_by='Synthetic Board',
        impact_levels=[f'Mức {i}: consequence theo bảng giả định thử nghiệm, không dùng thực tế' for i in range(1,6)],
        likelihood_levels=[f'Mức {i}: likelihood theo horizon Q4, giả định thử nghiệm' for i in range(1,6)],
        rating_basis='Synthetic categorical mapping do người lập fixture xác định; không nhân/trung bình điểm',horizon=ctx['horizon'])]
    for i in range(3):
        data['assessments'].append(dict(id=f'A{i+1}',risk_id=f'R{i+1}',method_id='M1',basis='current',
            as_of=ctx['as_of'],horizon=ctx['horizon'],impact=[4,5,None][i],likelihood=[3,4,None][i],
            rating=['High','Critical',None][i],rationale='Synthetic rating để kiểm tra hiển thị; R3 thiếu dữ liệu.',evidence_ids=['SYN1']))
    definitions = [('K1','Capacity thiếu hụt','units','N/A','higher',100,200,300,'COO'),
                   ('K2','Cash cuối kỳ','triệu','VND','lower',5000,0,-1000,'CFO'),
                   ('K3','Complaint rate','ratio','N/A','higher',.01,.02,.05,'Quality Director')]
    for i,(key,label,unit,currency,direction,warn,limit,capacity,owner) in enumerate(definitions):
        data['metrics'].append(dict(id=key,label=label,risk_ids=[f'R{i+1}'],unit=unit,currency=currency,
            horizon=ctx['horizon'],scope='Group',bad_direction=direction,formula=['max(demand-capacity,0)',
            'opening + inflows - outflows','confirmed complaints / units sold'][i],owner=owner,frequency='monthly',
            max_age_days=40,approval='approved',approved_by='Synthetic Board',rules=[dict(op='>=' if direction=='higher' else '<=',
            threshold=t,severity=s) for t,s in zip([warn,limit,capacity],['warning','breach','capacity_breach'])],
            action=['Xác nhận nguồn thay thế','Escalate CFO/Board và cash plan','Xác minh complaint và batch'][i]))
        for j,dt in enumerate(['2026-07-31','2026-08-31','2026-09-03']):
            value = [[80,120,200],[8000,3000,-2000],[None,None,None]][i][j]
            data['observations'].append(dict(id=f'O{i+1}{j+1}',metric_id=key,as_of=dt,value=value,
                quality='missing' if value is None else 'valid',evidence_ids=['SYN1'],unit=unit,currency=currency,horizon=ctx['horizon'],scope='Group'))
    data['controls'] = [dict(id='C1',risk_ids=['R1'],label='Nguồn cung dự phòng',owner='COO',state='designed',
        design_conclusion='Thiết kế có phương án alternate',operating_conclusion='Chưa thử giao hàng',
        design_evidence_ids=['SYN1'],operating_evidence_ids=[],rcsa='Self-assessment; chưa độc lập kiểm thử')]
    data['scenarios'] = [dict(id='SC1',label='Port outage + chậm thu tiền',kind='stress',horizon=ctx['horizon'],
        baseline='Demand 1000, capacity1000; opening cash20000 triệu',assumptions=['Capacity800','Contribution40 triệu/unit',
        'Recovery2000 triệu','Penalty1000 triệu','Inflows8000 triệu','Outflows30000 triệu'],
        transmission='Port dừng → capacity giảm → contribution mất; thu tiền trễ → cash breach',
        result='Incremental loss 11000 triệu VND; closing cash -2000 triệu VND',
        limitations='Synthetic combined stress; không có probability/forecast; không cộng cash balance với P&L loss.',evidence_ids=['SYN1'])]
    data['losses'] = [dict(id='L1',risk_ids=['R1','R2'],amount=11000,currency='VND',horizon=ctx['horizon'],scope='Group',eliminated=False,evidence_ids=['SYN1']),
        dict(id='L2',risk_ids=['R3'],amount=2000,currency='VND',horizon=ctx['horizon'],scope='Group',eliminated=False,evidence_ids=['SYN1'])]
    data['dependencies'] = [dict(id='DEP1',from_risk_id='R1',to_risk_id='R2',kind='cascade',mechanism='Delivery delay làm chậm collection',evidence_ids=['SYN1'])]
    data['treatments'] = [dict(id='TR1',risk_ids=['R1','R2'],option='reduce',action='Thử alternate port và cash contingency',
        owner='COO + CFO',deadline='2026-09-20',status='proposed',cost=500,currency='VND',lead_time='2 tuần',
        resource_constraint='Cần 2 người; mới có 1',secondary_risk='Alternate port tăng transit và phí',
        expected_benefit='Giảm thời gian gián đoạn; chưa đo benefit thực tế',
        no_action_case='Synthetic: giữ exposure gián đoạn và cash shortfall của SC1.',
        target='Synthetic: khôi phục khả năng giao hàng; residual exposure chưa định lượng, chờ thử alternate port.',
        target_assessment_ids=[],benefit_basis='assumed',acceptance_authority=None,evidence_ids=['SYN1'])]
    data['handoffs'] = [dict(id='H1',specialist='BCP',capability_status='unverified',version='unknown',
        question='BIA và recovery feasibility cho alternate port',target='Group supply chain',horizon=ctx['horizon'],
        as_of=ctx['as_of'],input_refs=['R1','SYN1'],constraints='Không cài hoặc gửi bên ngoài',
        acceptance_criteria='BIA scope, verified recovery test và limitations',output_contract='Recovery alternatives và evidence',
        result_status='not_run',method=None,validation_status=None,limitations='Chưa thử handoff specialist',monitoring='Review sau exercise')]
    return data
