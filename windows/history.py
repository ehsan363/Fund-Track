from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QFrame, QScrollArea, QComboBox
from PySide6.QtGui import QIcon, QFont, QKeySequence
from PySide6.QtCore import Qt, Signal
from data.database import DBmanager
from helper.dateAndTime import dateExtraction
from helper.HPrefresher import clear_layout
import json

class historyWindow(QMainWindow):
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
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        pageLayout = QVBoxLayout(centralWidget)
        pageLayout.setAlignment(Qt.AlignTop)
        pageLayout.setSpacing(35)

        # UI elements
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

            label.setSizePolicy(label.sizePolicy().horizontalPolicy(), label.sizePolicy().verticalPolicy())
            self.contentLayout.insertWidget(self.contentLayout.count() - 1, label)