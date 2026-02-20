from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QDoubleSpinBox
from PySide6.QtGui import QIcon, QFont, QKeySequence
from PySide6.QtCore import Qt, Signal
import json

class userWindow(QMainWindow):
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

        # UI elements
        # Heading
        self.headingLabel = QLabel("""User
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

        self.enterName = QLineEdit()
        self.enterName.setPlaceholderText('Enter Your Name')
        self.enterName.setStyleSheet("""
            QLineEdit {
                background-color: #1e1e1e;
                color: #ededed;
                border: 2px solid #333;
                border-radius: 8px;
                padding: 8px 12px;
                font-size: 14px;
            }
            QLineEdit:hover {
                border-color: #ed7521;
            }
            QLineEdit:focus {
                border-color: #ed7521;
                background-color: #222;
            }
        """)

        self.budgetEntry = QDoubleSpinBox()
        self.budgetEntry.setDecimals(2)
        self.budgetEntry.setMaximum(10_000_000)

        with open('data/config.json') as f:
            data = json.load(f)
            currencySuffix = f' {data["CurrencySuffix"]}'
        self.budgetEntry.setSuffix(currencySuffix)
        self.budgetEntry.setStyleSheet('''
            QDoubleSpinBox {
                background-color: #222;
                color: #eee;
                border: 1px solid #444;
                border-radius: 8px;
                padding: 6px 10px;
                font-size: 16px;
            }
            
            QDoubleSpinBox:hover {
                border: 1px solid #666;
            }
            
            QDoubleSpinBox:focus {
                border: 1px solid #ed7521;
            }
            
            QDoubleSpinBox::up-button,
            QDoubleSpinBox::down-button {
                width: 0px;
                border: none;
            }''')

        submitBtn = QPushButton('Enter')
        submitBtn.setStyleSheet('''
            QPushButton {
                background-color: #ed7521;
                color: black;
                padding: 10px 20px 10px 20px;
                border-radius: 8px;
                border: 2px solid black;
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
        submitBtn.clicked.connect(self.changeName)


        pageLayout.addWidget(backButton)
        pageLayout.addWidget(self.headingLabel)
        pageLayout.addWidget(self.enterName)
        pageLayout.addWidget(self.budgetEntry)
        pageLayout.addWidget(submitBtn)


        pageLayout.addStretch()

        centralWidget = QWidget()
        centralWidget.setLayout(pageLayout)
        centralWidget.setStyleSheet('background-color: #141414; color: #ed7521;')
        self.setCentralWidget(centralWidget)  # <-- Stuff into Central Widget

    def changeName(self):
        newName = self.enterName.text()
        if len(newName) != 0:
            with open('data/data.json', 'r') as f:
                data = json.load(f)

            data['user'][0]['Name'] = newName

            with open('data/config.json', 'w') as f:
                json.dump(data, f, indent=4)
        if len(self.budgetEntry.text()) != 0:
            newBudget = self.budgetEntry.text()[0:-5]
            with open('data/config.json', 'r') as f:
                data = json.load(f)

            data['User'][1]['Budget'] = newBudget

            with open('data/config.json', 'w') as f:
                json.dump(data, f, indent=4)
        self.goHome_Signal.emit()