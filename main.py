from PySide6.QtWidgets import QApplication, QFrame
from windows.home import MainWindow # Homepage window imported
from windows.addExpense import addExpenseWindow
from windows.editExpense import editExpenseWindow
from windows.editIncome import editIncomeWindow
from windows.history import historyWindow
from windows.user import userWindow
from windows.settings import settingsWindow
import sys

class AppController:
    def __init__(self):
        self.window = MainWindow() # Main window
        self.window.gohomepage_Signal.connect(self.refresh)
        self.window.addExpense_Signal.connect(self.open_addexpense)
        self.window.editExpense_Signal.connect(self.open_editexpense)
        self.window.editIncome_Signal.connect(self.open_editincome)
        self.window.history_Signal.connect(self.open_history)
        self.window.user_Signal.connect(self.open_user)
        self.window.settings_Signal.connect(self.open_settings)
        self.window.show()

        # self.app.exec()
    def refresh(self):
        self.window.refresh()

    def open_addexpense(self):
        self.sub_window = addExpenseWindow()
        self.sub_window.show()
        self.window.close()


    def open_editexpense(self):
        self.sub_window = editExpenseWindow()
        self.sub_window.show()
        self.window.close()

    def open_editincome(self):
        self.sub_window = editIncomeWindow()
        self.sub_window.show()
        self.window.close()

    def open_history(self):
        self.sub_window = historyWindow()
        self.sub_window.show()
        self.window.close()

    def open_user(self):
        self.sub_window = userWindow()
        self.sub_window.show()
        self.window.close()

    def open_settings(self):
        self.sub_window = settingsWindow()
        self.sub_window.show()
        self.window.close()



def start():
    global app
    app = QApplication(sys.argv)
    controller = AppController()
    sys.exit(app.exec())

start()