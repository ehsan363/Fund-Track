'''
This file controls all the other files opening, processing, etc.
Opening of all the application windows goes through this file.
'''
from PySide6.QtWidgets import QApplication  # Pyside6 for the GUI element of the program
import sys #  sys for proper opening and closing of the program

# Other Python files being imported
from windows.home import MainWindow
from windows.addTransaction import addTransactionWindow
from windows.editExpense import editExpenseWindow
from windows.editIncome import editIncomeWindow
from windows.history import historyWindow
from windows.user import userWindow
from windows.settings import settingsWindow
from helper.reportGenerator import monthlyReport


class AppController:
    '''
    Controls all the windows of GUI
    Includes:
    - Opening Windows
    - Closing Windows
    - Refreshing homepage
    '''
    def __init__(self):
        self.window = MainWindow()

        # Taskbar Buttons with functions linked
        self.window.refresh_Signal.connect(self.refresh)
        self.window.addTransaction_Signal.connect(self.open_addtransaction)
        self.window.editExpense_Signal.connect(self.open_editexpense)
        self.window.editIncome_Signal.connect(self.open_editincome)
        self.window.history_Signal.connect(self.open_history)
        self.window.user_Signal.connect(self.open_user)
        self.window.settings_Signal.connect(self.open_settings)
        self.window.show()
        monthlyReport()  # Automated finance report generator
        '''
        Monthly report is being called here so that the report generation will happen as soon as the application opened.
        The report will only be generated once a month, so it does not generate one every time you open the application.
        '''

    # To refresh the Homepage
    def refresh(self):
        self.window.refresh()

    # To go back to Homescreen using the back button
    def go_home(self):
        '''
            1, Closing the subwindow if it exists
            2, Showing the Homepage again
            3, Refreshing the homepage
        '''
        if self.sub_window:
            self.sub_window.close()

        self.window.show()
        self.window.refresh()

    def open_addtransaction(self):
        '''
            Opens Add Transaction Window
            1. Creates subwindow (Add Transaction Window)
            2. Creates the back button in the subwindow to come back to the Homepage
            3. Show the subwindow
            4, hide the Homepage (main window)
        '''
        self.sub_window = addTransactionWindow()
        self.sub_window.goHome_Signal.connect(self.go_home)
        self.sub_window.show()
        self.window.hide()


    def open_editexpense(self):
        '''
            Opens Edit Expenses Window
            1. Creates subwindow (Edit Expenses Window)
            2. Creates the back button in the subwindow to come back to the Homepage
            3. Show the subwindow
            4, hide the Homepage (main window)
        '''
        self.sub_window = editExpenseWindow()
        self.sub_window.goHome_Signal.connect(self.go_home)
        self.sub_window.show()
        self.window.hide()

    def open_editincome(self):
        '''
            Opens Edit Income Window
            1. Creates subwindow (Edit Income Window)
            2. Creates the back button in the subwindow to come back to the Homepage
            3. Show the subwindow
            4, hide the Homepage (main window)
        '''
        self.sub_window = editIncomeWindow()
        self.sub_window.goHome_Signal.connect(self.go_home)
        self.sub_window.show()
        self.window.hide()

    def open_history(self):
        '''
            Opens History Window
            1. Creates subwindow (History Window)
            2. Creates the back button in the subwindow to come back to the Homepage
            3. Show the subwindow
            4, hide the Homepage (main window)
        '''
        self.sub_window = historyWindow()
        self.sub_window.goHome_Signal.connect(self.go_home)
        self.sub_window.show()
        self.window.hide()

    def open_user(self):
        '''
            Opens User Window
            1. Creates subwindow (User Window)
            2. Creates the back button in the subwindow to come back to the Homepage
            3. Show the subwindow
            4, hide the Homepage (main window)
        '''
        self.sub_window = userWindow()
        self.sub_window.goHome_Signal.connect(self.go_home)
        self.sub_window.show()
        self.window.hide()

    def open_settings(self):
        '''
            Opens Settings Window
            1. Creates subwindow (Settings Window)
            2. Creates the back button in the subwindow to come back to the Homepage
            3. Show the subwindow
            4, hide the Homepage (main window)
        '''
        self.sub_window = settingsWindow()
        self.sub_window.goHome_Signal.connect(self.go_home)
        self.sub_window.show()
        self.window.hide()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    controller = AppController()
    sys.exit(app.exec())