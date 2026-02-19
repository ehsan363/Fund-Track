from helper.dateAndTime import reportDateCompare
from data.database import DBmanager
from pathlib import Path
import json

def monthlyReport():
    with open('data/config.json', 'r') as pathFile:
        JSONfile = json.load(pathFile)
        path = Path(JSONfile['Report'][0]['Path'])

    if path.exists():
        data = JSONfile['Report'][1]['LastGenDate']
        update, year, month = reportDateCompare(data)
        if update == 'Outdated':
            db = DBmanager()
            categories, total_income = db.ReportData(year, month)
            total_expense = db.Expense()

            budgetRead = JSONfile['User'][1]['Budget']
            TXT = f'''FundTrack Monthly Report
=========================
Year: {year}
Month: {month}

Total Income: {total_income} AED

Budget: {float(budgetRead):,.2f} AED
Total Expense: {total_expense} AED
Saved: {float(budgetRead)-total_expense:,.2f} AED

Expenses By Category:

'''
            for i in categories:
                TXT+=f'- {i[0]}: {i[1]:,.2f} AED\n'


            with open(str(path)+f'/Report{year}-{month}.txt','a') as report:
                report.write(TXT)

            with open('data/config.json', 'r') as f:
                data = json.load(f)

            data['Report'][1]['LastGenDate'] = f'{year}-{month}'

            with open('data/config.json', 'w') as f:
                json.dump(data, f, indent=4)