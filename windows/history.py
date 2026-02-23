'''
This file controls all the GUI elements of the history window.
This file will be opened by main.py whenever history button is clicked on the taskbar,
or when the shortcut key is pressed.
'''

# Importing GUI elements
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QFrame, QScrollArea, QComboBox
from PySide6.QtGui import QIcon, QFont, QKeySequence
from PySide6.QtCore import Qt, Signal
from data.database import DBmanager
from helper.dateAndTime import dateExtraction
from helper.HPrefresher import clear_layout
import json

class historyWindow(QMainWindow):
    '''
    Controls all the GUI elements and functions of the history window.
    Include:
    - Function to change report export path
    - Function to change the suffix currency symbol
    - Display all the available shortcuts in the program
    '''
    goHome_Signal = Signal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('FundTrack')

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

        # UI elements
        '''
        headingLabel is the label for the heading text.
        
        backButton is the button on the top part of the window that allows user to return to the HomePage.
        
        scroll is the varibale which allows the user to scroll through the page of recent transactions.
        '''
        # Heading
        self.headingLabel = QLabel("""History
──────────────────────────────────────────────────────────────────────────────────────────""")
        self.headingLabel.setAlignment(Qt.AlignLeft)
        self.headingLabel.setStyleSheet("""
            font-size: 36px;
            font-family: DejaVu Sans Mono;
            padding-top: 15px;
            padding-left: 10px;""")

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

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        content = QWidget()
        self.contentLayout = QVBoxLayout(content)
        self.contentLayout.setSpacing(30)

        scroll.setWidget(content)

        # Sort Feature
        '''
        sortMenu is the menu in which all the options in which you can sort the transaction are.
        trasanctionSort, the function will be called whenever the option inside the menu is changed.
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
             'Amount L->H',
             'Income -> Expense',
             'Expense -> Income'])
        pageLayout.addWidget(self.sortMenu)

        self.sortMenu.currentTextChanged.connect(self.transactionSort)
        self.transactionSort(self.sortMenu.currentText())

        pageLayout.addWidget(backButton)
        pageLayout.addWidget(self.headingLabel)
        pageLayout.addWidget(self.sortMenu)
        pageLayout.addWidget(scroll, 1)
        pageLayout.addStretch()

        centralWidget.setStyleSheet('background-color: #141414; color: #ed7521;')
        self.setCentralWidget(centralWidget)  # <-- Stuff into Central Widget

    def transactionSort(self, sortedTo):
        '''
        This function is to sort out the transaction history according to the option selected from the menu.
        This function will be called whenever the history windows is opened,
        and when the option inside the sorter is changed.

        - First clears out layout with another function imported.
        - Fetches the suffix from the JSON file.
        - Converts the date format, selects border color accoridng to the transaction type and
          creates Label with content.
        '''
        clear_layout(self.contentLayout)
        db = DBmanager()
        data = db.transactionHistory(sortedTo)

        with open('data/config.json') as f:
            read = json.load(f)
            currencySuffix = f' {read["CurrencySuffix"]}'

        for i in data:
            year, month, day = dateExtraction(i['date'])
            fullDate = day+'-'+month+'-'+year

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

            self.contentLayout.addWidget(label)