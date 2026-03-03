# Importing functions from other files
from helper.dateAndTime import reportDateCompare
from data.database import DBmanager

# Importing from modules
from pathlib import Path
import json

def monthlyReport():
    '''
    Function to generate monthly report.
    Generated .txt files as a report right now but will change later on to a PDF or/and .xlsx files.
    Will generate a report for the previous month if the date is too old in the json file.
    A button will be added to the user window or some other window which will allow the user to generate a report on demand.
    '''
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

            with open('data/config.json') as f:
                data = json.load(f)
                currencySuffix = f' {data["CurrencySuffix"]}'

            budgetRead = JSONfile['User'][1]['Budget']
            TXT = f'''FundTrack Monthly Report
=========================
Year: {year}
Month: {month}

Total Income: {total_income}{currencySuffix}

Budget: {float(budgetRead):,.2f}{currencySuffix}
Total Expense: {total_expense}{currencySuffix}
Saved: {float(budgetRead)-total_expense:,.2f}{currencySuffix}

Expenses By Category:

'''
            for i in categories:
                TXT+=f'- {i[0]}: {i[1]:,.2f}{currencySuffix}\n'


            with open(str(path)+f'/Report{year}-{month}.txt','a') as report:
                report.write(TXT)

            with open('data/config.json', 'r') as f:
                data = json.load(f)

            data['Report'][1]['LastGenDate'] = f'{year}-{month}'

            with open('data/config.json', 'w') as f:
                json.dump(data, f, indent=4)