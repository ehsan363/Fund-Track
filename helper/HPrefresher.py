from PySide6.QtWidgets import QLabel
from data.database import DBmanager
from helper.barchartMatplotlib import update_bar_chart
from helper.dateAndTime import greetingText, dateCompare
import json

def greetingRefresh(greetingLabel):
    with open('data/config.json', 'r') as f:
        data = json.load(f)
        username = data['User'][0]['Name']

    greeting = greetingText()
    if greeting[0] == 'G' or greeting[0] == 'W':
        greetingLabel.setStyleSheet('margin-top:25%;')
        greetingLabel.setText(f'{greeting} {username.title()}')
    else:
        greetingLabel.setStyleSheet('margin-top:0%;')
        greetingLabel.setText(greeting)

def summaryCardRefresher(budgetLabel):
    with open('data/config.json', 'r') as f:
        data = json.load(f)
        budgetRead = data['User'][1]['Budget']
        currencySuffix = data['CurrencySuffix']

    db = DBmanager()  # Expense from Database to summary card
    totalExpense = db.Expense()

    budget = f'''Budget: {float(budgetRead):,.2f} {currencySuffix}
Expense: {totalExpense:,} {currencySuffix}
─────────────────────────
Balance: {float(budgetRead) - totalExpense:,.2f} {currencySuffix}'''
    budgetLabel.setText(budget)

def clear_layout(layout):
    while layout.count():
        item = layout.takeAt(0)
        if item.widget():
            item.widget().deleteLater()

def transactionHistoryRefresher(historyLayout):
    clear_layout(historyLayout)
    db = DBmanager()  # Expense from Database to history card

    transactionHistory = db.history()  # Transaction history from DB

    transactionHistoryDate0 = dateCompare(transactionHistory[0][2])
    transactionHistoryDate1 = dateCompare(transactionHistory[0][2])
    transactionHistoryDate2 = dateCompare(transactionHistory[0][2])
    transactionHistoryDate3 = dateCompare(transactionHistory[0][2])
    transactionHistoryDate4 = dateCompare(transactionHistory[0][2])

    with open('data/config.json', 'r') as f:
        data = json.load(f)
        currencySuffix = data['CurrencySuffix']

    transactionHistory0 = f'''{transactionHistory[0][0]:<30}             {transactionHistory[0][1] + f' {currencySuffix}':>15}
{transactionHistoryDate0}'''
    transactionLabel0 = QLabel(f'{transactionHistory0}')
    if transactionHistory[0][3] == 'expense':
        transactionColorCode = '#c71413'
    elif transactionHistory[0][3] == 'income':
        transactionColorCode = '#11b343'
    transactionLabel0.setStyleSheet(f'''
                border: 3px solid {transactionColorCode};
                padding: 10px;
                margin-top: 10px;''')

    transactionHistory1 = f'''{transactionHistory[1][0]:<30}             {transactionHistory[1][1] + f' {currencySuffix}':>15}
{transactionHistoryDate1}'''
    transactionLabel1 = QLabel(f'{transactionHistory1}')
    if transactionHistory[1][3] == 'expense':
        transactionColorCode = '#c71413'
    elif transactionHistory[1][3] == 'income':
        transactionColorCode = '#11b343'
    transactionLabel1.setStyleSheet(f'''
                border: 3px solid {transactionColorCode};
                padding: 10px;
                margin-top: 10px;''')

    transactionHistory2 = f'''{transactionHistory[2][0]:<30}             {transactionHistory[2][1] + f' {currencySuffix}':>15}
{transactionHistoryDate2}'''
    transactionLabel2 = QLabel(f'{transactionHistory2}')
    if transactionHistory[2][3] == 'expense':
        transactionColorCode = '#c71413'
    elif transactionHistory[2][3] == 'income':
        transactionColorCode = '#11b343'
    transactionLabel2.setStyleSheet(f'''
                border: 3px solid {transactionColorCode};
                padding: 10px;
                margin-top: 10px;''')

    transactionHistory3 = f'''{transactionHistory[3][0]:<30}             {transactionHistory[3][1] + f' {currencySuffix}':>15}
{transactionHistoryDate3}'''
    transactionLabel3 = QLabel(f'{transactionHistory3}')
    if transactionHistory[3][3] == 'expense':
        transactionColorCode = '#c71413'
    elif transactionHistory[3][3] == 'income':
        transactionColorCode = '#11b343'
    transactionLabel3.setStyleSheet(f'''
                border: 3px solid {transactionColorCode};
                padding: 10px;
                margin-top: 10px;''')

    transactionHistory4 = f'''{transactionHistory[4][0]:<30}             {transactionHistory[4][1] + f' {currencySuffix}':>15}
{transactionHistoryDate4}'''
    transactionLabel4 = QLabel(f'{transactionHistory4}')
    if transactionHistory[4][3] == 'expense':
        transactionColorCode = '#c71413'
    elif transactionHistory[4][3] == 'income':
        transactionColorCode = '#11b343'
    transactionLabel4.setStyleSheet(f'''
                border: 3px solid {transactionColorCode};
                padding: 10px;
                margin-top: 10px;''')

    historyLayout.addWidget(transactionLabel0)
    historyLayout.addWidget(transactionLabel1)
    historyLayout.addWidget(transactionLabel2)
    historyLayout.addWidget(transactionLabel3)
    historyLayout.addWidget(transactionLabel4)

def barchartRefresher(plt, figure, canvas):
    update_bar_chart(plt, figure, canvas)