from PySide6.QtWidgets import QLabel, QVBoxLayout
from PySide6.QtCore import Qt
from data.database import DBmanager
from helper.barchartMatplotlib import update_bar_chart
from helper.dateAndTime import greetingText

def greetingRefresh(greetingLabel):
    with open('data/user.txt', 'r') as file:
        username = file.read()

    greeting = greetingText()
    if greeting[0] == 'G' or greeting[0] == 'W':
        greetingLabel.setText(f'{greeting} {username.title()}')
    else:
        greetingLabel.setText(greeting)

def summaryCardRefresher(budgetLabel):
    with open('data/budget.txt', 'r') as file:
        budgetRead = file.readline()

    db = DBmanager()  # Expense from Database to summary card
    totalExpense = db.Expense()

    budget = f'''Budget: {int(budgetRead):,} AED
Expense: {totalExpense:,} AED
─────────────────────────
Balance: {int(budgetRead) - totalExpense:,.2f} AED'''
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

    transactionHistory0 = f'''{transactionHistory[0][0]:<30}             {transactionHistory[0][1] + ' AED':>15}
    {transactionHistory[0][2]}'''
    transactionLabel0 = QLabel(f'{transactionHistory0}')
    if transactionHistory[0][3] == 'expense':
        transactionColorCode = '#c71413'
    elif transactionHistory[0][3] == 'income':
        transactionColorCode = '#11b343'
    transactionLabel0.setStyleSheet(f'''
                border: 3px solid {transactionColorCode};
                padding: 10px;
                margin-top: 10px;''')

    transactionHistory1 = f'''{transactionHistory[1][0]:<30}             {transactionHistory[1][1] + ' AED':>15}
    {transactionHistory[1][2]}'''
    transactionLabel1 = QLabel(f'{transactionHistory1}')
    if transactionHistory[1][3] == 'expense':
        transactionColorCode = '#c71413'
    elif transactionHistory[1][3] == 'income':
        transactionColorCode = '#11b343'
    transactionLabel1.setStyleSheet(f'''
                border: 3px solid {transactionColorCode};
                padding: 10px;
                margin-top: 10px;''')

    transactionHistory2 = f'''{transactionHistory[2][0]:<30}             {transactionHistory[2][1] + ' AED':>15}
    {transactionHistory[2][2]}'''
    transactionLabel2 = QLabel(f'{transactionHistory2}')
    if transactionHistory[2][3] == 'expense':
        transactionColorCode = '#c71413'
    elif transactionHistory[2][3] == 'income':
        transactionColorCode = '#11b343'
    transactionLabel2.setStyleSheet(f'''
                border: 3px solid {transactionColorCode};
                padding: 10px;
                margin-top: 10px;''')

    transactionHistory3 = f'''{transactionHistory[3][0]:<30}             {transactionHistory[3][1] + ' AED':>15}
    {transactionHistory[3][2]}'''
    transactionLabel3 = QLabel(f'{transactionHistory3}')
    if transactionHistory[3][3] == 'expense':
        transactionColorCode = '#c71413'
    elif transactionHistory[3][3] == 'income':
        transactionColorCode = '#11b343'
    transactionLabel3.setStyleSheet(f'''
                border: 3px solid {transactionColorCode};
                padding: 10px;
                margin-top: 10px;''')

    transactionHistory4 = f'''{transactionHistory[4][0]:<30}             {transactionHistory[4][1] + ' AED':>15}
    {transactionHistory[4][2]}'''
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