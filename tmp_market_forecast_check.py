import sys
import os
import json

sys.path.append(os.path.join(os.getcwd(), 'backend'))
from finance_app.ai_module import FinanceAIService

for sym in ['bitcoin', 'gold', 'cse']:
    try:
        report = FinanceAIService.get_market_forecast(symbol=sym, horizon='monthly')
        print('SYMBOL', sym)
        print('STATUS', report.get('status'))
        print('KEYS', sorted(report.keys()))
        print('SAMPLE', json.dumps({
            k: report[k]
            for k in ['symbol', 'current_price', 'market_signal', 'recommendation', 'return_estimates', 'investment_advice', 'data_source']
            if k in report
        }, indent=2))
        print('FORECAST_LENGTHS', len(report.get('daily_forecast', [])), len(report.get('monthly_forecast', [])), len(report.get('yearly_forecast', [])))
        print('---')
    except Exception as e:
        print('ERROR', sym, e)
