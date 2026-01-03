from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QDoubleSpinBox, QDateEdit, QComboBox, QTextEdit, QHBoxLayout, QFrame
from PySide6.QtGui import QIcon, QFont, QKeySequence
from PySide6.QtCore import Qt, Signal, QDate
from helper.dateAndTime import todayDate

class addExpenseWindow(QMainWindow):
    goHome_Signal = Signal()

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

        row1 = QHBoxLayout()
        row1.setAlignment(Qt.AlignLeft)

        row2 = QHBoxLayout()
        row2.setAlignment(Qt.AlignLeft)
        row2.setSpacing(450)

        row3 = QHBoxLayout()
        row3.setAlignment(Qt.AlignLeft)
        row3.setSpacing(450)

        row4 = QHBoxLayout()
        row4.setAlignment(Qt.AlignLeft)

        row5 = QHBoxLayout()
        row5.setAlignment(Qt.AlignLeft)

        # UI elements
        # Heading
        self.headingLabel = QLabel("""Add Expense
──────────────────────────────────────────────────────────────────────────────────────────""")
        self.headingLabel.setAlignment(Qt.AlignLeft)
        self.headingLabel.setStyleSheet("""
            font-size: 36px;
            font-family: DejaVu Sans Mono;
            padding-top: 15px;
            padding-left: 10px;""")

        backButton = QPushButton(QIcon('img/back_icon.png'),'Back')
        backButton.setShortcut(QKeySequence('Ctrl+W'))
        backButton.setStyleSheet('''
        QPushButton {
            background-color: #ed7521;
            color: black;
            padding: 10px 20px 10px 20px;
            border-radius: 8px;
            font-size: 16px;
            text-align: left;
        }
        QPushButton:hover {
            background-color: #f08337;
        }
        QPushButton:pressed {
            background-color: #ed6709;
        }
        ''')
        backButton.clicked.connect(self.goHome_Signal.emit)

        # Date
        row1Card = QFrame()
        row1Card.setStyleSheet('''
            font-size: 18px;
            padding-left: 15px;
            padding-top: 10px;''')

        self.dateEntry = QDateEdit()
        self.dateEntry.setDate(todayDate())
        self.dateEntry.setCalendarPopup(True)
        self.dateEntry.setStyleSheet('''
            background-color: #222222;
            border-radius: 10px;
            border: 1px solid #404040;
            padding-bottom: 10px;''')

        row1CardLayout = QHBoxLayout(row1Card)
        row1CardLayout.addWidget(self.dateEntry)

        # Amount
        row2Card = QFrame()
        row2Card.setStyleSheet('''
            font-size: 18px;
            padding-left: 15px;''')

        self.amountEntry = QDoubleSpinBox()
        self.amountEntry.setDecimals(2)
        self.amountEntry.setMaximum(10_000_000)
        self.amountEntry.setPrefix('AED ')
        self.amountEntry.setStyleSheet('''
            font-size: 18px;
            padding-left: 25px;
            background-color: #222222;
            border-radius: 5px;
            border: 1px solid #404040;
            padding: 5px;''')

        # Type
        self.typeEntry = QComboBox()
        self.typeEntry.addItems(['Income', 'Expense'])
        self.typeEntry.setStyleSheet('''
            font-size: 18px;
            padding: 8px;
            border-radius: 5px;
            border: 1px solid #404040;
            background-color: #222222;''')

        row2CardLayout = QHBoxLayout(row2Card)
        row2CardLayout.setSpacing(40)
        row2CardLayout.addWidget(self.amountEntry)
        row2CardLayout.addWidget(self.typeEntry)

        # Category
        row3Card = QFrame()
        row3Card.setStyleSheet('''
            font-size: 18px;
            padding-left: 15px;''')

        self.categoryEntry = QComboBox()
        # Should change this to be extracted from the file and the selected "type"
        self.categoryEntry.addItems(["Salary", "Freelance", "Bonus", "Interest", "Food", "Rent", "Transport", "Shopping", "Utilities", "Entertainment"])
        self.categoryEntry.setStyleSheet('''
            font-size: 18px;
            padding: 5px;
            border-radius: 5px;
            border: 1px solid #404040;
            background-color: #222222;''')

        # Account
        self.accountEntry = QComboBox()
        self.accountEntry.addItems(["Cash", "Bank", "Credit Card"])
        self.accountEntry.setStyleSheet('''
            font-size: 18px;
            padding: 5px;
            border-radius: 5px;
            border: 1px solid #404040;
            background-color: #222222;''')

        row3CardLayout = QHBoxLayout(row3Card)
        row3CardLayout.setSpacing(40)
        row3CardLayout.addWidget(self.categoryEntry)
        row3CardLayout.addWidget(self.accountEntry)

        # Description
        row4Card = QFrame()
        row4Card.setStyleSheet('''
            font-size: 18px;''')

        self.descriptionLabel = QLabel('Description')
        self.descriptionLabel.setStyleSheet('''
            font-size: 18px;''')

        self.descriptionEntry = QTextEdit()
        self.descriptionEntry.setStyleSheet('''
            font-size: 18px;
            background-color: #222222;
            border-radius: 10px;
            border: 2px solid #ed7521;''')

        row4CardLayout = QVBoxLayout(row4Card)
        row4CardLayout.addWidget(self.descriptionLabel)
        row4CardLayout.addWidget(self.descriptionEntry)

        # Add Button
        self.submitBtn = QPushButton('Enter')
        self.submitBtn.setShortcut(QKeySequence('Alt+A'))
        self.submitBtn.clicked.connect(self.enterDate)
        self.submitBtn.setStyleSheet('''
            QPushButton {
                background-color: #ed7521;
                color: black;
                padding: 10px 20px 10px 20px;
                border-radius: 8px;
                font-size: 18px;
                text-align: center;
                
            }
            QPushButton:hover {
                background-color: #f08337;
            }
            QPushButton:pressed {
                background-color: #ed6709;
            }
        ''')

        row1.addWidget(row1Card)
        row2.addWidget(row2Card)
        row3.addWidget(row3Card)
        row4.addWidget(row4Card)


        pageLayout.addWidget(backButton)
        pageLayout.addWidget(self.headingLabel)
        pageLayout.addLayout(row1)
        pageLayout.addLayout(row2)
        pageLayout.addLayout(row3)
        pageLayout.addLayout(row4)
        pageLayout.addWidget(self.submitBtn)

        pageLayout.addStretch()

        centralWidget = QWidget()
        centralWidget.setLayout(pageLayout)
        centralWidget.setStyleSheet('background-color: #141414; color: #ed7521;')
        self.setCentralWidget(centralWidget)  # <-- Stuff into Central Widget

    def enterDate(self):
        print(self.categoryEntry.text())