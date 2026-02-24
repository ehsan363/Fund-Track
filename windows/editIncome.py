'''
This file controls all the GUI elements of the Edit Income Window.
This file will get opened by main.py when the edit income button is pressed or when the shortcut key is pressed.
'''

# Importing GUI elements
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QFrame, QScrollArea, QComboBox, QCheckBox, QHBoxLayout, QLineEdit
from PySide6.QtGui import QIcon, QFont, QKeySequence
from PySide6.QtCore import Qt, Signal, QSize

# Importing functions from other files
from data.database import DBmanager
from helper.dateAndTime import dateExtraction, NdateToFormattedDate
from helper.HPrefresher import clear_layout

# json to write and read json files
import json

class editIncomeWindow(QMainWindow):
    '''
    Controls all the GUI elements and functions of Edit Income window.
    Includes:
    - Delete Transactions
    - Change Amount
    - Change Type
    - Change Category
    - Change Date
    - Change Description
    '''
    goHome_Signal = Signal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('FundTrack') # Title of the window

        # Window settings
        self.resize(1920, 1080)
        self.setMinimumSize(1170, 650)

        self.setWindowIcon(QIcon('img/iconOrange#141414bgR.png'))

        # Font elements
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)

        # Layout
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        pageLayout = QVBoxLayout(centralWidget)
        pageLayout.setAlignment(Qt.AlignTop)
        pageLayout.setSpacing(35)

        topRow = QHBoxLayout()
        topRow.setAlignment(Qt.AlignLeft)

        '''
        headingLabel is label for to display the heading of the window
        '''

        # UI elements
        # Heading
        self.headingLabel = QLabel("""Edit Income
──────────────────────────────────────────────────────────────────────────────────────────""")
        self.headingLabel.setAlignment(Qt.AlignLeft)
        self.headingLabel.setStyleSheet("""
            font-size: 36px;
            font-family: DejaVu Sans Mono;
            padding-top: 15px;
            padding-left: 10px;""")

        '''
        buttonCard is the card to hold all the buttons of options which can be used to manipulate the transactions.
        
        The backButton allows the user to go back to the Homepage.
        It also has the shortcut key of Crtl + W, doing either of these will let the user get to the Homepage.
        '''

        buttonCard = QFrame()
        buttonCardLayout = QHBoxLayout(buttonCard)

        backButton = QPushButton(QIcon('img/back_icon.png'), 'Back')
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

        '''
        deleteButton is a button that has the function linked to delete trasanctions that are selected.
        '''

        deleteButton = QPushButton(QIcon('img/bin_icon.png'), 'Delete')
        deleteButton.setIconSize(QSize(18, 18))
        deleteButton.setShortcut(QKeySequence('Ctrl+D'))
        deleteButton.setStyleSheet('''
            QPushButton {
                background-color: #ed7521;
                color: black;
                padding: 10px 20px 10px 20px;
                border-radius: 8px;
                font-size: 18px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #f08337;
            }
            QPushButton:pressed {
                background-color: #ed6709;
            }
            ''')
        deleteButton.clicked.connect(lambda: self.handleSelected('del'))

        '''
        changeAmountButton allows the user to change the amount of the transactions that are selected.
        '''
        changeAmountButton = QPushButton(QIcon('img/editAmount_icon.png'), 'Change Amount')
        changeAmountButton.setIconSize(QSize(22, 22))
        changeAmountButton.setStyleSheet('''
            QPushButton {
                background-color: #ed7521;
                color: black;
                padding: 10px 20px 10px 20px;
                border-radius: 8px;
                font-size: 18px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #f08337;
            }
            QPushButton:pressed {
                background-color: #ed6709;
            }
            ''')
        changeAmountButton.clicked.connect(lambda: self.handleSelected('chAmnt'))

        '''
        changeTypeButton allows the user to change the type of transaction for the transactions selected.
        The type will be changed to the opposite type with instantly with nothing else to do.
        '''
        changeTypeButton = QPushButton(QIcon('img/changeType_icon.png'), 'Change Type')
        changeTypeButton.setIconSize(QSize(26, 26))
        changeTypeButton.setStyleSheet('''
            QPushButton {
                background-color: #ed7521;
                color: black;
                padding: 10px 20px 10px 20px;
                border-radius: 8px;
                font-size: 18px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #f08337;
            }
            QPushButton:pressed {
                background-color: #ed6709;
            }
            ''')
        changeTypeButton.clicked.connect(lambda: self.handleSelected('chType'))

        '''
        changeCategoryButton allows the user to change the category of the transactions selected.
        '''
        changeCategoryButton = QPushButton(QIcon('img/changeCategory_icon.png'), 'Change Category')
        changeCategoryButton.setIconSize(QSize(26, 26))
        changeCategoryButton.setStyleSheet('''
            QPushButton {
                background-color: #ed7521;
                color: black;
                padding: 10px 20px 10px 20px;
                border-radius: 8px;
                font-size: 18px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #f08337;
            }
            QPushButton:pressed {
                background-color: #ed6709;
            }
            ''')
        changeCategoryButton.clicked.connect(lambda: self.handleSelected('chCate'))

        '''
        changeDateButton allows the user to change the date of the transactions that are selected.
        '''
        changeDateButton = QPushButton(QIcon('img/changeDate_icon.png'), 'Change Date')
        changeDateButton.setIconSize(QSize(26, 26))
        changeDateButton.setStyleSheet('''
            QPushButton {
                background-color: #ed7521;
                color: black;
                padding: 10px 20px 10px 20px;
                border-radius: 8px;
                font-size: 18px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #f08337;
            }
            QPushButton:pressed {
                background-color: #ed6709;
            }
            ''')
        changeDateButton.clicked.connect(lambda: self.handleSelected('chDate'))

        '''
        changeDescriptionButton allows the user to change the description of the transactions that are selected.
        '''
        changeDescriptionButton = QPushButton(QIcon('img/changeDescription_icon.png'), 'Change Description')
        changeDescriptionButton.setIconSize(QSize(26, 26))
        changeDescriptionButton.setStyleSheet('''
            QPushButton {
                background-color: #ed7521;
                color: black;
                padding: 10px 20px 10px 20px;
                border-radius: 8px;
                font-size: 18px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #f08337;
            }
            QPushButton:pressed {
                background-color: #ed6709;
            }
            ''')
        changeDescriptionButton.clicked.connect(lambda: self.handleSelected('chDesc'))

        '''
        textEntry is to enter the new data to replace the current one with the selected transactions.
        '''
        self.textEntry = QLineEdit()
        self.textEntry.setPlaceholderText('Amount: Number | Date: DD-MM-YYYY ')
        self.textEntry.setAlignment(Qt.AlignLeft)
        self.textEntry.setStyleSheet('''
            font-size: 18px;
            font-family: Adwaita mono;''')

        buttonCardLayout.addWidget(deleteButton)
        buttonCardLayout.addWidget(changeAmountButton)
        buttonCardLayout.addWidget(changeTypeButton)
        buttonCardLayout.addWidget(changeCategoryButton)
        buttonCardLayout.addWidget(changeDateButton)
        buttonCardLayout.addWidget(changeDescriptionButton)
        buttonCardLayout.addWidget(self.textEntry)

        topRow.addWidget(buttonCard)

        '''
        scroll, to allow scrolling function to view all the transactions.
        '''
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        content = QWidget()
        self.contentLayout = QVBoxLayout(content)
        self.contentLayout.setSpacing(30)

        scroll.setWidget(content)

        # Sort Feature
        '''
        menu to sort the transactions in order.
        '''
        self.sortMenu = QComboBox()
        self.sortMenu.setStyleSheet("""
            QComboBox {
                font-size: 18px;
                padding: 8px;
                border-radius: 5px;
                border: 1px solid #404040;
                background-color: #222222;
                font-family: Adwaita mono;
            }

            QComboBox QAbstractItemView::item:hover {
                background-color: #404040;
                color: #ed7521;
            }

            QComboBox QAbstractItemView::item:selected {
                background-color: #222222;
                color: #ed7521;
            }

            QComboBox:focus {
                border: 1px solid #ed7521;
            }""")
        self.sortMenu.addItems(
            ['Date DESC',
             'Date ASC',
             'Created ASC',
             'Created DESC',
             'Amount H->L',
             'Amount L->H'])
        pageLayout.addWidget(self.sortMenu)

        self.transactionCheckBoxes = []
        self.selectedIDs = []
        self.sortToSaver = ''

        self.sortMenu.currentTextChanged.connect(self.transactionSort)
        self.transactionSort(self.sortMenu.currentText())

        pageLayout.addWidget(backButton)
        pageLayout.addWidget(self.headingLabel)
        pageLayout.addLayout(topRow)
        pageLayout.addWidget(self.sortMenu)
        pageLayout.addWidget(scroll, 1)
        pageLayout.addStretch()

        centralWidget.setStyleSheet('background-color: #141414; color: #ed7521;')
        self.setCentralWidget(centralWidget)  # <-- Stuff into Central Widget

    def transactionSort(self, sortedTo):
        '''
        Function to sort the transactions in order according to what is selected in the menu.
        '''
        self.sortToSaver = sortedTo
        self.selectedIDs.clear()
        self.transactionCheckBoxes.clear()
        self.deleteSelectedIDs()
        clear_layout(self.contentLayout)
        with open('data/config.json') as f:
            data = json.load(f)
            currencySuffix = f' {data["CurrencySuffix"]}'
        db = DBmanager()
        data = db.editingTransactionHistory(sortedTo, 'income')
        for i in data:
            year, month, day = dateExtraction(i['date'])
            fullDate = day + '-' + month + '-' + year

            if i['type'] == 'income':
                transactionColorCode = '#11b343'
            elif i['type'] == 'expense':
                transactionColorCode = '#c71413'

            label = QLabel(f'''{fullDate:<10}                    {i['category']:^22}              {i['account']:^20}                        {i['amount']:>8}{currencySuffix}

{i['description']}                                                                                     {i['created_at']:>20}''')
            label.setStyleSheet(f'''
                font-size: 24px;
                border: 3px solid {transactionColorCode};
                border-radius: 15px;
                color: #e8e8e8;''')

            label.setSizePolicy(
                label.sizePolicy().horizontalPolicy(),
                label.sizePolicy().verticalPolicy()
            )
            self.contentLayout.insertWidget(self.contentLayout.count() - 1, label)
            selectCheckbox = QCheckBox('Select')
            selectCheckbox.setStyleSheet('''
                QCheckBox {
                    spacing: 10px;
                    font-size: 14px;
                    color: #ed7521;
                    font-family: Adwaita mono;
                }
                QCheckBox::indicator {
                    width: 20px;
                    height: 20px;
                }
                QCheckBox::indicator:unchecked {
                    border: 2px solid #888;
                    background: white;
                    border-radius: 4px;
                }
                QCheckBox::indicator:checked {
                    border: 2px solid #ed7521;
                    border-radius: 4px;
                    background-color: #222222;
                }''')
            selectCheckbox.setProperty('transaction_id', i['id'])
            self.transactionCheckBoxes.append(selectCheckbox)
            self.contentLayout.insertWidget(self.contentLayout.count() - 1, selectCheckbox)

    def handleSelected(self, function):
        '''
        Function to make changes to the transaction which are selected, and to make changes according to the option clicked.
        '''
        self.selectedIDs.clear()
        for checkbox in self.transactionCheckBoxes:
            if checkbox.isChecked():
                transactionID = checkbox.property('transaction_id')
                self.selectedIDs.append(transactionID)
        if not self.selectedIDs:
            print('none selected')
            return
        print('DONE')
        db = DBmanager()
        if function == 'del':
            db.deleteSelected(self.selectedIDs)
            self.transactionSort(self.sortToSaver)
            self.deleteSelectedIDs()

        elif function == 'chAmnt':
            newAmount = self.textEntry.text()
            if newAmount.isnumeric():
                db.changeAmount(self.selectedIDs, float(newAmount))
            self.transactionSort(self.sortToSaver)
            self.deleteSelectedIDs()

        elif function == 'chType':
            db.changeType(self.selectedIDs)
            self.transactionSort(self.sortToSaver)
            self.deleteSelectedIDs()

        elif function == 'chCate':
            newCategory = self.textEntry.text().title()
            fetchedType = db.getType(self.selectedIDs)
            fetchedCategories = db.categories(fetchedType)
            if newCategory in fetchedCategories:
                db.changeCategory(self.selectedIDs, newCategory)
            self.transactionSort(self.sortToSaver)
            self.deleteSelectedIDs()

        elif function == 'chDate':
            newDate = self.textEntry.text()
            points = 0
            if newDate[2] == '-' and newDate[5] == '-':
                points += 1
            if newDate[0].isnumeric() and newDate[1].isnumeric() and newDate[3].isnumeric() and newDate[4].isnumeric() and newDate[6].isnumeric() and newDate[7].isnumeric() and newDate[8].isnumeric() and newDate[9].isnumeric():
                points += 1
            if points == 2:
                formattedDate = NdateToFormattedDate(newDate)
                db.changeDate(self.selectedIDs, formattedDate)
            self.transactionSort(self.sortToSaver)
            self.deleteSelectedIDs()

        elif function == 'chDesc':
            newDecription = self.textEntry.text()
            db.changeDecription(self.selectedIDs, newDecription)
            self.transactionSort(self.sortToSaver)
            self.deleteSelectedIDs()

    def deleteSelectedIDs(self):
        '''
        FUnction to delete the selected transactions.
        '''
        self.selectedIDs.clear()