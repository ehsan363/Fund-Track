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

    def __init__(self):
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
            for i in data['Themes']:
                themePrimary = i[currentTheme]['Primary']
                themeSecondary = i[currentTheme]['Secondary']

                buttonConfig = i[currentTheme]['Button']
                entryConfig = i[currentTheme]['Entry']
                fontConfig = i[currentTheme]["Font"]
                sortConfig = i[currentTheme]["Sortmenu"]

                buttonBgColor = buttonConfig['bgcolor']
                buttonHoverBgColor = buttonConfig['hoverbgcolor']
                buttonClickedBgColor = buttonConfig['clickbgcolor']
                buttonColor = buttonConfig['color']

                entryBgColor = entryConfig['bgcolor']
                entryColor = entryConfig['color']
                entryBorderColor = entryConfig['bordercolor']

                font_color0 = fontConfig['font-color0']
                font_color1 = fontConfig['font-color1']
                font_color2 = fontConfig['font-color2']

                sortNormalBorder = sortConfig["border"]
                sortNormalBgColor = sortConfig["bgcolor"]

        # Heading
        self.headingLabel = QLabel("""Add Transaction
──────────────────────────────────────────────────────────────────────────────────────────""")
        self.headingLabel.setAlignment(Qt.AlignLeft)
        self.headingLabel.setStyleSheet(f"""
            font-size: 36px;
            font-family: DejaVu Sans Mono;
            padding-top: 15px;
            padding-left: 10px;
            color: {font_color0}
        """)


        '''
        buttonCard is the card to hold all the buttons of options which can be used to manipulate the transactions.

        The backButton allows the user to go back to the Homepage.
        It also has the shortcut key of Ctrl + W, doing either of these will let the user get to the Homepage.
        '''
        backButton = QPushButton(QIcon('img/back_icon.png'),'Back')
        backButton.setShortcut(QKeySequence('Ctrl+W'))
        backButton.setStyleSheet(f'''
            QPushButton {{
                background-color: {buttonBgColor};
                padding: 10px 20px 10px 20px;
                border-radius: 8px;
                font-size: 16px;
                text-align: left;
                color: {buttonColor}
            }}
            QPushButton:hover {{
                background-color: {buttonHoverBgColor};
            }}
            QPushButton:pressed {{
                background-color: {buttonClickedBgColor};
            }}
        ''')
        backButton.clicked.connect(self.goHome_Signal.emit)

        # Date
        '''
        row1Card is the card to hold all the elements that are at top most row to select for the transaction
        '''
        row1Card = QFrame()
        row1Card.setStyleSheet('''
            font-size: 18px;
            padding-left: 15px;
            padding-top: 10px;
        ''')

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
        self.dateEntry.setStyleSheet(f"""
            QDateEdit {{
                background-color: {entryBgColor};
                border: 2px solid {entryColor};
                border-radius: 8px;
                padding: 6px 10px;
                font-size: 14px;
            }}
            
            QDateEdit:hover {{
                border: 2px solid {entryBorderColor};
            }}
            
            QDateEdit:focus {{
                border: 2px solid {entryBorderColor};
            }}
            
            QDateEdit::drop-down {{
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 24px;
                border-left: 2px solid {entryBorderColor};
            }}
            
            QDateEdit::down-arrow {{
                image: url(themes/{currentTheme}/down_icon.png);
                width: 14px;
                height: 14px;
            }}
            
            QCalendarWidget QToolButton#qt_calendar_prevmonth {{
                qproperty-icon: url(themes/{currentTheme}/chevron-left.png);
                qproperty-iconSize: 16px;
            }}
            
            QCalendarWidget QToolButton#qt_calendar_nextmonth {{
                qproperty-icon: url(themes/{currentTheme}/chevron-right.png);
                qproperty-iconSize: 16px;
            }}
            
            QCalendarWidget QAbstractItemView {{
               font-size: 16px;
            }}
        """)

        '''
        Layout for the row1Card, uses horizontal layout
        '''
        row1CardLayout = QHBoxLayout(row1Card)
        row1CardLayout.addWidget(self.dateEntry)

        # Amount
        '''
        row2Card is the card that holds all the elements that are in the row after date selection. 
        '''
        row2Card = QFrame()
        row2Card.setStyleSheet('''
            font-size: 18px;
            padding-left: 15px;''')

        '''
        To allow the user to enter the amount for the transaction
        '''
        self.amountEntry = QDoubleSpinBox()
        self.amountEntry.setDecimals(2)
        self.amountEntry.setMaximum(10_000_000)

        '''
        Fetching the suffix for the currency from the json file.
        '''
        with open('data/config.json') as f:
            data = json.load(f)
            currencySuffix = f' {data["CurrencySuffix"]}'

        '''
        Allows the user to enter the amount for the transaction.
        '''
        self.amountEntry.setSuffix(currencySuffix)
        self.amountEntry.setStyleSheet(f'''
            QDoubleSpinBox {{
                background-color: {sortNormalBgColor};
                color: {font_color1};
                border: 2px solid {entryColor};
                border-radius: 8px;
                padding: 6px 10px;
                font-size: 16px;
            }}
            
            QDoubleSpinBox:hover {{
                border: 2px solid {entryBorderColor};
            }}
            
            QDoubleSpinBox:focus {{
                border: 2px solid {entryBorderColor};
            }}
            
            QDoubleSpinBox::up-button,
            QDoubleSpinBox::down-button {{
                width: 0px;
                border: none;
            }}''')

        # Type
        '''
        Allows the user to select the type of transaction.
        '''
        self.typeEntry = QComboBox()
        self.typeEntry.addItems(['Income', 'Expense'])
        self.typeEntry.setStyleSheet(f"""
            QComboBox {{
                font-size: 18px;
                padding: 8px;
                border-radius: 5px;
                border: 2px solid {sortNormalBorder};
                background-color: {sortNormalBgColor};
                color: {font_color0};
                font-family: Adwaita mono;
            }}
            
            QComboBox:hover {{
                border: 2px solid {entryBorderColor};
            }}
            
            QComboBox:focus {{
                border: 2px solid {entryBorderColor};
            }}
        """)

        '''
        Layout for the row2Card, uses horizontal layout
        '''
        row2CardLayout = QHBoxLayout(row2Card)
        row2CardLayout.setSpacing(40)
        row2CardLayout.addWidget(self.amountEntry)
        row2CardLayout.addWidget(self.typeEntry)

        # Category
        '''
        row3Card holds the elements that allows the user to enter or select data for the transaction that comes after amount entry and type choosing.
        '''
        row3Card = QFrame()
        row3Card.setStyleSheet('''
            font-size: 18px;
            padding-left: 15px;
        ''')

        '''
        categoryEntry is to enter the category of the transaction.
        '''
        self.categoryEntry = QComboBox()
        self.categoryEntry.setStyleSheet(f"""
            QComboBox {{
                font-size: 18px;
                padding: 8px;
                border-radius: 5px;
                border: 2px solid {sortNormalBorder};
                background-color: {sortNormalBgColor};
                color: {font_color0};
                font-family: Adwaita mono;
            }}
            
            QComboBox:hover {{
                border: 2px solid {entryBorderColor};
            }}
            
            QComboBox:focus {{
                border: 2px solid {entryBorderColor};
            }}
        """)

        # Account
        '''
        accountEntry is to select the account through which the transaction is made
        '''
        self.accountEntry = QComboBox()
        self.accountEntry.addItems(["Cash", "Bank", "Credit Card"])
        self.accountEntry.setStyleSheet(f"""
            QComboBox {{
                font-size: 18px;
                padding: 8px;
                border-radius: 5px;
                border: 2px solid {sortNormalBorder};
                background-color: {sortNormalBgColor};
                color: {font_color0};
                font-family: Adwaita mono;
            }}
            
            QComboBox:hover {{
                border: 2px solid {entryBorderColor};
            }}
            
            QComboBox:focus {{
                border: 2px solid {entryBorderColor};
            }}
        """)

        row3CardLayout = QHBoxLayout(row3Card)
        row3CardLayout.setSpacing(40)
        row3CardLayout.addWidget(self.categoryEntry)
        row3CardLayout.addWidget(self.accountEntry)

        self.typeEntry.currentTextChanged.connect(self.categoryChange)
        self.categoryChange(self.typeEntry.currentText())

        # Description
        '''
        row4Card holds all the elements that are in the row after category entry and account entry
        '''
        row4Card = QFrame()
        row4Card.setStyleSheet('''
            font-size: 18px;
            padding-left: 10px;
            padding-top: 5px;
            font-family: Adwaita mono;
        ''')

        '''
        descriptionLabel is to show the title of the area where the user can type in the description
        '''
        self.descriptionLabel = QLabel('Description')
        self.descriptionLabel.setStyleSheet(f'''
            font-size: 18px;
            color: {font_color0}
        ''')

        '''
        descriptionEntry is the area where the user enters the description
        '''
        self.descriptionEntry = QTextEdit()
        self.descriptionEntry.setStyleSheet(f'''
            font-size: 18px;
            background-color: {themeSecondary};
            border-radius: 10px;
            border: 2px solid {entryBorderColor};
        ''')

        row4CardLayout = QVBoxLayout(row4Card)
        row4CardLayout.addWidget(self.descriptionLabel)
        row4CardLayout.addWidget(self.descriptionEntry)

        # Add Button
        '''
        submitBtn is the button using which we can add the transaction
        '''
        self.submitBtn = QPushButton('Enter')
        self.submitBtn.setShortcut(QKeySequence('Alt+A'))
        self.submitBtn.clicked.connect(self.enterData)
        self.submitBtn.setStyleSheet(f'''
            QPushButton {{
                background-color: {buttonBgColor};
                color: {buttonColor};
                padding: 10px 20px 10px 20px;
                border-radius: 8px;
                font-size: 18px;
                text-align: center;  
            }}
            
            QPushButton:hover {{
                background-color: {buttonHoverBgColor};
            }}
            
            QPushButton:pressed {{
                background-color: {buttonClickedBgColor};
            }}
        ''')

        '''
        resetCh is the chackbox that disables the values getting reset
        '''
        self.resetCh = QCheckBox('Do not reset')
        self.resetCh.setStyleSheet(f'''
            QCheckBox {{
                spacing: 10px;
                font-size: 14px;
                color: {font_color0};
                font-family: Adwaita mono;
            }}
            
            QCheckBox::indicator {{
                width: 20px;
                height: 20px;
            }}
            
            QCheckBox::indicator:unchecked {{
                border: 2px solid {sortNormalBorder};
                background: {themeSecondary};
                border-radius: 4px;
            }}
            
            QCheckBox::indicator:checked {{
                border: 2px solid {entryBorderColor};
                border-radius: 4px;
            }}''')

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
        pageLayout.addWidget(self.resetCh)

        pageLayout.addStretch()

        centralWidget = QWidget()
        centralWidget.setLayout(pageLayout)
        centralWidget.setStyleSheet(f'background-color: {themePrimary}; color: {font_color1};')
        self.setCentralWidget(centralWidget)

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