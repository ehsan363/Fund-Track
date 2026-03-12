'''
This file controls all the GUI elements of the Add Transaction Window.
This file will get opened by main.py when the add transaction button is pressed or when the shortcut button is pressed.
'''

# Importing GUI elements
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QDoubleSpinBox, QDateEdit, QComboBox, QTextEdit, QHBoxLayout, QFrame, QCheckBox
from PySide6.QtGui import QIcon, QFont, QKeySequence
from PySide6.QtCore import Qt, Signal, QDate

# Importing functions from other files
from helper.dateAndTime import todayDate, dateFormat
from data.database import DBmanager

# json to write and read json files
import json

class addTransactionWindow(QMainWindow):
    '''
    Controls all GUI elements and functions of Add Transaction Window.
    Includes:
    - Add a new transaction
    - Select or enter the date of the transaction
    - Enter amount of the transaction
    - Select between Income and Expense
    - Select the source of transaction
    - Select the means of transaction
    - Enter description for the transaction
    - Checkbox to no reset the value entered and selected
    '''
    goHome_Signal = Signal()

    def __init__(self, ThemeManager):
        super().__init__()
        self.setWindowTitle('FundTrack') # Title of the window

        # Window settings
        self.resize(1920, 1080)
        self.setMinimumSize(1170, 650)

        self.setWindowIcon(QIcon('img/iconOrange141414bgR.png'))

        # Font elements
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)

        # Layout
        pageLayout = QVBoxLayout()
        pageLayout.setAlignment(Qt.AlignTop)
        pageLayout.setSpacing(35)

        self.mainWidget = QWidget()
        self.mainWidget.setLayout(pageLayout)
        self.setCentralWidget(self.mainWidget)

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

        '''
        headingLabel is a label to display the heading of the window
        '''
        # UI elements
        # Theme
        with open('data/config.json', 'r') as f:
            data = json.load(f)
            currentTheme = data['CurrentTheme']

        self.themeManager = ThemeManager()
        self.themeManager.themeChanged.connect(self.refreshTheme)

        # Heading
        self.headingLabel = QLabel("""Add Transaction
──────────────────────────────────────────────────────────────────────────────────────────""")
        self.headingLabel.setAlignment(Qt.AlignLeft)
        self.headingLabelBaseStyle = """
            font-size: 36px;
            font-family: DejaVu Sans Mono;
            padding-top: 15px;
            padding-left: 10px;
        """


        '''
        buttonCard is the card to hold all the buttons of options which can be used to manipulate the transactions.

        The backButton allows the user to go back to the Homepage.
        It also has the shortcut key of Ctrl + W, doing either of these will let the user get to the Homepage.
        '''
        self.backButton = QPushButton(QIcon('img/back_icon.png'),'Back')
        self.backButton.setShortcut(QKeySequence('Ctrl+W'))
        self.backButtonBaseStyle = '''
            QPushButton {
                padding: 10px 20px 10px 20px;
                border-radius: 8px;
                font-size: 16px;
                text-align: left;
            }
        '''
        self.backButton.clicked.connect(self.goHome_Signal.emit)

        # Date
        '''
        row1Card is the card to hold all the elements that are at top most row to select for the transaction
        '''
        self.row1Card = QFrame()
        self.row1CardBaseStyle = '''
            font-size: 18px;
            padding-left: 15px;
            padding-top: 10px;
        '''

        '''
        dateEntry is an element that allows the user to select the date from a calander or enter it for the transaction
        '''
        self.dateEntry = QDateEdit()
        self.dateEntry.setDate(todayDate())
        self.dateEntry.setCalendarPopup(True)
        self.dateEntry.setDisplayFormat('dd-MM-yyyy')
        self.dateEntry.setFixedWidth(150)
        calendar = self.dateEntry.calendarWidget()
        calendar.setMinimumSize(360, 300)

        '''
        Layout for the row1Card, uses horizontal layout
        '''
        row1CardLayout = QHBoxLayout(self.row1Card)
        row1CardLayout.addWidget(self.dateEntry)

        # Amount
        '''
        row2Card is the card that holds all the elements that are in the row after date selection. 
        '''
        self.row2Card = QFrame()
        self.row2CardBaseStyle = '''
            font-size: 18px;
            padding-left: 15px;
        '''

        '''
                Fetching the suffix for the currency from the json file.
                '''
        with open('data/config.json') as f:
            data = json.load(f)
            currencySuffix = f' {data["CurrencySuffix"]}'

        '''
        To allow the user to enter the amount for the transaction
        '''
        self.amountEntry = QDoubleSpinBox()
        self.amountEntry.setDecimals(2)
        self.amountEntry.setMaximum(10_000_000)
        self.amountEntry.setSuffix(currencySuffix)
        self.amountEntryBaseStyle = '''
            QDoubleSpinBox {
                border-radius: 8px;
                padding: 6px 10px;
                font-size: 16px;
            }
        '''

        # Type
        '''
        Allows the user to select the type of transaction.
        '''
        self.typeEntry = QComboBox()
        self.typeEntry.addItems(['Income', 'Expense'])
        self.typeEntryBaseStyle = """
            QComboBox {
                font-size: 18px;
                padding: 8px;
                border-radius: 5px;
                font-family: Adwaita mono;
            }
        """

        '''
        Layout for the row2Card, uses horizontal layout
        '''
        row2CardLayout = QHBoxLayout(self.row2Card)
        row2CardLayout.setSpacing(40)
        row2CardLayout.addWidget(self.amountEntry)
        row2CardLayout.addWidget(self.typeEntry)

        # Category
        '''
        row3Card holds the elements that allows the user to enter or select data for the transaction that comes after amount entry and type choosing.
        '''
        self.row3Card = QFrame()
        self.row3CardBaseStyle = '''
            font-size: 18px;
            padding-left: 15px;
        '''

        '''
        categoryEntry is to enter the category of the transaction.
        '''
        self.categoryEntry = QComboBox()
        self.categoryEntryBaseStyle = """
            QComboBox {
                font-size: 18px;
                padding: 8px;
                border-radius: 5px;
                font-family: Adwaita mono;
            }
        """

        # Account
        '''
        accountEntry is to select the account through which the transaction is made
        '''
        self.accountEntry = QComboBox()
        self.accountEntry.addItems(["Cash", "Bank", "Credit Card"])
        self.accountEntryBaseStyle = """
            QComboBox {
                font-size: 18px;
                padding: 8px;
                border-radius: 5px;
                font-family: Adwaita mono;
            }
        """

        row3CardLayout = QHBoxLayout(self.row3Card)
        row3CardLayout.setSpacing(40)
        row3CardLayout.addWidget(self.categoryEntry)
        row3CardLayout.addWidget(self.accountEntry)

        self.typeEntry.currentTextChanged.connect(self.categoryChange)
        self.categoryChange(self.typeEntry.currentText())

        # Description
        '''
        row4Card holds all the elements that are in the row after category entry and account entry
        '''
        self.row4Card = QFrame()
        self.row4CardBaseStyle = '''
            font-size: 18px;
            padding-left: 10px;
            padding-top: 5px;
            font-family: Adwaita mono;
        '''

        '''
        descriptionLabel is to show the title of the area where the user can type in the description
        '''
        self.descriptionLabel = QLabel('Description')
        self.descriptionLabelBaseStyle = '''
            font-size: 18px;
        '''

        '''
        descriptionEntry is the area where the user enters the description
        '''
        self.descriptionEntry = QTextEdit()
        self.descriptionEntryBaseStyle = '''
            font-size: 18px;
            border-radius: 10px;
        '''

        row4CardLayout = QVBoxLayout(self.row4Card)
        row4CardLayout.addWidget(self.descriptionLabel)
        row4CardLayout.addWidget(self.descriptionEntry)

        # Add Button
        '''
        submitBtn is the button using which we can add the transaction
        '''
        self.submitBtn = QPushButton('Enter')
        self.submitBtn.setShortcut(QKeySequence('Alt+A'))
        self.submitBtn.clicked.connect(self.enterData)
        self.submitBtnBaseStyle = '''
            QPushButton {
                padding: 10px 20px 10px 20px;
                border-radius: 8px;
                font-size: 18px;
                text-align: center;  
            }
        '''

        '''
        resetCh is the chackbox that disables the values getting reset
        '''
        self.resetCh = QCheckBox('Do not reset')

        row1.addWidget(self.row1Card)
        row2.addWidget(self.row2Card)
        row3.addWidget(self.row3Card)
        row4.addWidget(self.row4Card)


        pageLayout.addWidget(self.backButton)
        pageLayout.addWidget(self.headingLabel)
        pageLayout.addLayout(row1)
        pageLayout.addLayout(row2)
        pageLayout.addLayout(row3)
        pageLayout.addLayout(row4)
        pageLayout.addWidget(self.submitBtn)
        pageLayout.addWidget(self.resetCh)
        self.refreshTheme()

        pageLayout.addStretch()

    def resetForm(self):
        '''
        Function to reset the value entered and selected after a transaction has been added
        '''
        self.dateEntry.setDate(QDate.currentDate())
        self.amountEntry.setValue(0.0)
        self.typeEntry.setCurrentIndex(0)
        self.categoryEntry.setCurrentIndex(0)
        self.accountEntry.setCurrentIndex(0)
        self.descriptionEntry.clear()

    def enterData(self):
        '''
        Function to add the transaction into the database with the data given
        '''
        db = DBmanager()
        amount = self.amountEntry.text()
        IorE = self.typeEntry.currentText()
        category = self.categoryEntry.currentText()
        date = self.dateEntry.text()
        new_date = dateFormat(date)
        description = self.descriptionEntry.toPlainText()
        account = self.accountEntry.currentText()

        with open('data/config.json') as f:
            data = json.load(f)
            currencySuffix = f' {data["CurrencySuffix"]}'
        amount = amount.rstrip(currencySuffix)

        db.addTransactionToDB(float(amount), IorE.lower(), category, new_date, description, account)
        if self.resetCh.isChecked():
            pass
        else:
            self.resetForm()

    def categoryChange(self, typeSelected):
        '''
        Function to change the options to select for category according to type selected
        '''
        self.categoryEntry.clear()

        db = DBmanager()
        self.categoryDBIncome = db.categories('income')
        self.categoryDBExpense = db.categories('expense')
        db.close()

        if typeSelected == 'Income':
            self.categoryEntry.addItems(self.categoryDBIncome)
        else:
            self.categoryEntry.addItems(self.categoryDBExpense)

    def refreshTheme(self):
        self.mainWidget.setStyleSheet(self.themeManager.get_stylesheet('PrimaryASecondary'))
        self.headingLabel.setStyleSheet(self.headingLabelBaseStyle + self.themeManager.get_stylesheet('QLabel'))
        self.backButton.setStyleSheet(self.backButtonBaseStyle + self.themeManager.get_stylesheet('QPushButton'))
        self.row1Card.setStyleSheet(self.row1CardBaseStyle)
        self.dateEntry.setStyleSheet(self.themeManager.get_stylesheet('QDateEdit'))
        self.row2Card.setStyleSheet(self.row2CardBaseStyle)
        self.amountEntry.setStyleSheet(self.amountEntryBaseStyle + self.themeManager.get_stylesheet('QDoubleSpinBox') + self.themeManager.get_stylesheet('font_color1'))
        self.typeEntry.setStyleSheet(self.typeEntryBaseStyle + self.themeManager.get_stylesheet('QComboBox') + self.themeManager.get_stylesheet('QLabel'))
        self.categoryEntry.setStyleSheet(self.categoryEntryBaseStyle + self.themeManager.get_stylesheet('QComboBox') + self.themeManager.get_stylesheet('QLabel'))
        self.accountEntry.setStyleSheet(self.accountEntryBaseStyle + self.themeManager.get_stylesheet('QComboBox') + self.themeManager.get_stylesheet('QLabel'))
        self.row3Card.setStyleSheet(self.row3CardBaseStyle)
        self.row4Card.setStyleSheet(self.row4CardBaseStyle)
        self.descriptionLabel.setStyleSheet(self.descriptionLabelBaseStyle + self.themeManager.get_stylesheet('QLabel'))
        self.descriptionEntry.setStyleSheet(self.descriptionEntryBaseStyle + self.themeManager.get_stylesheet('QFrame'))
        self.submitBtn.setStyleSheet(self.submitBtnBaseStyle + self.themeManager.get_stylesheet('QPushButton'))
        self.resetCh.setStyleSheet(self.themeManager.get_stylesheet('QCheckBox'))