import tushare as ts


report = ts.get_report_data(2014,3)

profitReport = ts.get_profit_data(2014,3)
report = report.join(other=profitReport.set_index('code'),on='code',rsuffix='_profit',how='left')

operationReport = ts.get_operation_data(2014,3)
report = report.join(other=operationReport.set_index('code'),on='code',rsuffix='_operation',how='left')

growthReport = ts.get_growth_data(2014,3)
report = report.join(other=growthReport.set_index('code'),on='code',rsuffix='_growth',how='left')

debtpayingReport = ts.get_debtpaying_data(2014,3)
report = report.join(other=debtpayingReport.set_index('code'),on='code',rsuffix='_debtpaying',how='left')

cashflowReport = ts.get_cashflow_data(2014,3)
report = report.join(other=cashflowReport.set_index('code'),on='code',rsuffix='_cashflow',how='left')


print(report)