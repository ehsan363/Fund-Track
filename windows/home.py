# Importing modules from PySide6 library
from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QToolBar, QFrame
from PySide6.QtGui import QAction, QFont, QIcon
from PySide6.QtCore import Qt
from data.database import DBmanager
from dateAndTime import greetingText

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('FundTrack') # Title of the window
        # Window size
        self.resize(1920, 1080)
        self.setMinimumSize(1170, 650)

        # Window icon
        self.setWindowIcon(QIcon('img/iconOrange#141414bgR.png'))

        # Font elements
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)

        # Layout
        pageLayout = QVBoxLayout()
        pageLayout.setAlignment(Qt.AlignTop)
        pageLayout.setSpacing(35)

        topRow = QHBoxLayout()
        topRow.setAlignment(Qt.AlignLeft)
        topRow.setSpacing(350)

        bottomRow = QHBoxLayout()
        bottomRow.setAlignment(Qt.AlignLeft)
        bottomRow.setSpacing(20)

        # Create UI elements

        # Toolbar options
        toolbar = QToolBar("Main Toolbar", self)
        self.addToolBar(toolbar)
        toolbar.setStyleSheet('Background-color: #e78c4d; font-size: 20px;')
        action_add = QAction("Add Expense", self)
        toolbar.addAction(action_add)

        action_add = QAction("Edit Expense", self)
        toolbar.addAction(action_add)

        action_add = QAction("Edit Income", self)
        toolbar.addAction(action_add)

        action_add = QAction("History", self)
        toolbar.addAction(action_add)

        action_add = QAction("User", self)
        toolbar.addAction(action_add)

        action_add = QAction("Settings", self)
        toolbar.addAction(action_add)

        # Connect button click to function
        # #self.button.clicked.connect(self.increase_count)

        # No row
        self.headingLabel = QLabel("HomePage")
        self.headingLabel.setAlignment(Qt.AlignLeft)
        self.headingLabel.setStyleSheet("""
            font-size: 36px;
            font-family: DejaVu Sans Mono;
            padding-top: 15px;
            padding-left: 10px;""")

        # Top row
        summaryCard = QFrame() # Summary card
        summaryCard.setFixedWidth(350)
        summaryCard.setStyleSheet("""
            background-color: #222222;
            font-family: Noto Sans Mono Thin;
            font-weight: bold;
            padding: 10px;
            border-radius: 20px;
            margin-left: 20px;""")

        self.summaryLabel = QLabel('Summary')
        self.summaryLabel.setStyleSheet("""
            font-size: 28px;
            color: White;
            font-weight: bold;
            margin-left: 30px;
            padding-top: 5px;
            margin-top: 20px;""")

        with open('data/budget.txt', 'r') as file:
            self.budgetRead = file.readline()

        db = DBmanager()  # Expense from Database to summary card
        totalExpense = db.Expense()

        self.budget = f'''Budget: {int(self.budgetRead):,} AED
Expense: {totalExpense:,} AED'''
        self.budgetLabel = QLabel(self.budget)
        self.budgetLabel.setAlignment(Qt.AlignTop)
        self.budgetLabel.setStyleSheet('font-size: 18px;')

        summaryLayout = QVBoxLayout(summaryCard)
        summaryLayout.addWidget(self.summaryLabel)
        summaryLayout.addWidget(self.budgetLabel)

        topRow.addWidget(summaryCard)


        # Greeting card
        greetingCard = QFrame()
        greetingCard.setFixedWidth(1050)
        greetingCard.setFixedHeight(100)
        greetingCard.setStyleSheet('''
            font-family: Caladea;
            font-weight: bold;
            background-color: #222222;
            color: White;
            font-size: 26px;
            border-radius: 15px;''')

        with open('data/user.txt', 'r') as file:
            self.username = file.read()

        greeting = greetingText()
        if greeting[0] == 'G' or greeting[0] == 'W':
            self.greetingLabel = QLabel(f'{greeting} {self.username.title()}')
            self.greetingLabel.setStyleSheet('margin-top:25%;')

        else:
            self.greetingLabel = QLabel(greeting)

        self.greetingLabel.setAlignment(Qt.AlignCenter)

        greetingLayout = QVBoxLayout(greetingCard)
        greetingLayout.addWidget(self.greetingLabel)

        topRow.addWidget(greetingCard)

        # Bottom row
        historyCard = QFrame()
        historyCard.setFixedWidth(900)
        historyCard.setStyleSheet('''
            font-size: 22px;
            color: White;
            background-color: #222222;
            border-radius: 10px;
            margin-left: 20px;
            font-family: Noto Sans Mono Thin;
            font-weight: bold;
            padding-bottom: 10px;
            padding-right: 10px;''')

        self.historyLabel = QLabel('Transaction History')
        self.historyLabel.setStyleSheet('padding-top: 10px;')

        self.transactionHistory = db.history() # Transaction history from DB

        self.transactionHistory0 = f'''{self.transactionHistory[0][0]:<30}             {self.transactionHistory[0][1]:>15}
{self.transactionHistory[0][2]}'''
        self.transactionLabel0 = QLabel(f'{self.transactionHistory0}')
        if self.transactionHistory[0][3] == 'expense':
            transactionColorCode = '#c71413'
        elif self.transactionHistory[0][3] == 'income':
            transactionColorCode = '#11b343'
        self.transactionLabel0.setStyleSheet(f'''
            border: 3px solid {transactionColorCode};
            padding: 10px;
            margin-top: 10px;''')


        self.transactionHistory1 = f'''{self.transactionHistory[1][0]:<30}             {self.transactionHistory[1][1]:>15}
{self.transactionHistory[1][2]}'''
        self.transactionLabel1 = QLabel(f'{self.transactionHistory1}')
        if self.transactionHistory[1][3] == 'expense':
            transactionColorCode = '#c71413'
        elif self.transactionHistory[1][3] == 'income':
            transactionColorCode = '#11b343'
        self.transactionLabel1.setStyleSheet(f'''
            border: 3px solid {transactionColorCode};
            padding: 10px;
            margin-top: 10px;''')

        self.transactionHistory2 = f'''{self.transactionHistory[2][0]:<30}             {self.transactionHistory[2][1]:>15}
{self.transactionHistory[2][2]}'''
        self.transactionLabel2 = QLabel(f'{self.transactionHistory2}')
        if self.transactionHistory[2][3] == 'expense':
            transactionColorCode = '#c71413'
        elif self.transactionHistory[2][3] == 'income':
            transactionColorCode = '#11b343'
        self.transactionLabel2.setStyleSheet(f'''
            border: 3px solid {transactionColorCode};
            padding: 10px;
            margin-top: 10px;''')

        self.transactionHistory3 = f'''{self.transactionHistory[3][0]:<30}             {self.transactionHistory[3][1]:>15}
{self.transactionHistory[3][2]}'''
        self.transactionLabel3 = QLabel(f'{self.transactionHistory3}')
        if self.transactionHistory[3][3] == 'expense':
            transactionColorCode = '#c71413'
        elif self.transactionHistory[3][3] == 'income':
            transactionColorCode = '#11b343'
        self.transactionLabel3.setStyleSheet(f'''
            border: 3px solid {transactionColorCode};
            padding: 10px;
            margin-top: 10px;''')

        self.transactionHistory4 = f'''{self.transactionHistory[4][0]:<30}             {self.transactionHistory[4][1]:>15}
{self.transactionHistory[4][2]}'''
        self.transactionLabel4 = QLabel(f'{self.transactionHistory4}')
        if self.transactionHistory[4][3] == 'expense':
            transactionColorCode = '#c71413'
        elif self.transactionHistory[4][3] == 'income':
            transactionColorCode = '#11b343'
        self.transactionLabel4.setStyleSheet(f'''
            border: 3px solid {transactionColorCode};
            padding: 10px;
            margin-top: 10px;''')

        historyLayout = QVBoxLayout(historyCard)
        historyLayout.addWidget(self.historyLabel)
        historyLayout.addWidget(self.transactionLabel0)
        historyLayout.addWidget(self.transactionLabel1)
        historyLayout.addWidget(self.transactionLabel2)
        historyLayout.addWidget(self.transactionLabel3)
        historyLayout.addWidget(self.transactionLabel4)

        bottomRow.addWidget(historyCard)

        pageLayout.addWidget(self.headingLabel)
        pageLayout.addLayout(topRow)
        pageLayout.addLayout(bottomRow)

        pageLayout.addStretch() # <-- Should be last! To make everything in layout align to the left

        centralWidget = QWidget()
        centralWidget.setLayout(pageLayout)
        centralWidget.setStyleSheet('background-color: #141414; color: #e78c4d;')
        self.setCentralWidget(centralWidget) # <-- Stuff into Central Widget