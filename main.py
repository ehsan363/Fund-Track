from PySide6.QtWidgets import QApplication, QFrame
from windows.home import MainWindow # Homepage window imported
from windows.addTransaction import addTransactionWindow
from windows.editExpense import editExpenseWindow
from windows.editIncome import editIncomeWindow
from windows.history import historyWindow
from windows.user import userWindow
from windows.settings import settingsWindow
from helper.dateAndTime import reportDateCompare
from data.database import DBmanager
import sys

class AppController:
    def __init__(self):
        self.window = MainWindow() # Main window

        # Taskbar Buttons
        self.window.refresh_Signal.connect(self.refresh)
        self.window.addTransaction_Signal.connect(self.open_addtransaction)
        self.window.editExpense_Signal.connect(self.open_editexpense)
        self.window.editIncome_Signal.connect(self.open_editincome)
        self.window.history_Signal.connect(self.open_history)
        self.window.user_Signal.connect(self.open_user)
        self.window.settings_Signal.connect(self.open_settings)
        self.window.show()
        self.monthlyReport()

    def refresh(self):
        self.window.refresh()

    def go_home(self):
        if self.sub_window:
            self.sub_window.close()

        self.window.show()
        self.window.refresh()

    def open_addtransaction(self):
        self.sub_window = addTransactionWindow()
        self.sub_window.goHome_Signal.connect(self.go_home)
        self.sub_window.show()
        self.window.hide()


    def open_editexpense(self):
        self.sub_window = editExpenseWindow()
        self.sub_window.goHome_Signal.connect(self.go_home)
        self.sub_window.show()
        self.window.hide()

    def open_editincome(self):
        self.sub_window = editIncomeWindow()
        self.sub_window.goHome_Signal.connect(self.go_home)
        self.sub_window.show()
        self.window.hide()

    def open_history(self):
        self.sub_window = historyWindow()
        self.sub_window.goHome_Signal.connect(self.go_home)
        self.sub_window.show()
        self.window.hide()

    def open_user(self):
        self.sub_window = userWindow()
        self.sub_window.goHome_Signal.connect(self.go_home)
        self.sub_window.show()
        self.window.hide()

    def open_settings(self):
        self.sub_window = settingsWindow()
        self.sub_window.goHome_Signal.connect(self.go_home)
        self.sub_window.show()
        self.window.hide()

    def monthlyReport(self):
        with open('helper/reportGenerationDate.txt','r') as reportLog:
            data = reportLog.read()
        update, year, month = reportDateCompare(data)
        if update == 'Outdated':
            db = DBmanager()
            categories, total_income = db.ReportData(year, month)
            total_expense = db.Expense()

            with open('data/budget.txt', 'r') as file:
                budgetRead = file.readline()

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
            with open('helper/reportSavingPath.txt', 'r') as pathFile:
                path = pathFile.read()

            with open(path+f'Report{year}-{month}.txt','a') as report:
                report.write(TXT)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    controller = AppController()
    sys.exit(app.exec())