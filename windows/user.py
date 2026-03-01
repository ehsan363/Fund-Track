'''
This file controls all the GUI elements of User window.
This file will get opened by main.py whenever the User button is clicked  or the shortcut used.
'''

# Importing GUI elements
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QDoubleSpinBox
from PySide6.QtGui import QIcon, QFont, QKeySequence
from PySide6.QtCore import Qt, Signal

# json to read and write json file for the options selected
import json

class userWindow(QMainWindow):
    '''
    Controls all the GUI elements and functions of User window.
    Includes:
    - Change in name
    - Change in budget
    '''
    goHome_Signal = Signal()

    def __init__(self):
        super().__init__()

        # Window settings
        self.setWindowTitle('FundTrack')

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

                buttonBgColor = buttonConfig['bgcolor']
                buttonHoverBgColor = buttonConfig['hoverbgcolor']
                buttonClickedBgColor = buttonConfig['clickbgcolor']
                buttonColor = buttonConfig['color']

                entryBgColor = entryConfig['bgcolor']
                entryColor = entryConfig['color']
                entryBorderColor = entryConfig['bordercolor']

                font_color0 = fontConfig['font-color0']
                font_color1 = fontConfig['font-color1']

        # Heading
        self.headingLabel = QLabel("""User
──────────────────────────────────────────────────────────────────────────────────────────""")
        self.headingLabel.setAlignment(Qt.AlignLeft)
        self.headingLabel.setStyleSheet(f"""
            font-size: 36px;
            font-family: DejaVu Sans Mono;
            padding-top: 15px;
            padding-left: 10px;
            color: {font_color0}
        """)

        # Back button to return to Homepage
        backButton = QPushButton(QIcon('img/back_icon.png'), 'Back')
        backButton.setShortcut(QKeySequence('Ctrl+W')) # Shortcut key instead of pressing the button
        backButton.setStyleSheet(f'''
        QPushButton {{
            background-color: {buttonBgColor};
            color: {buttonColor};
            padding: 10px 20px 10px 20px;
            border-radius: 8px;
            font-size: 16px;
            text-align: left;
        }}
        QPushButton:hover {{
            background-color: {buttonHoverBgColor};
        }}
        QPushButton:pressed {{
            background-color: {buttonClickedBgColor};
        }}
        ''')
        backButton.clicked.connect(self.goHome_Signal.emit)

        # Entry to enter the new name
        self.enterName = QLineEdit()
        self.enterName.setPlaceholderText('Enter Your Name')
        self.enterName.setStyleSheet(f"""
            QLineEdit {{
                background-color: {entryBgColor};
                color: {font_color1};
                border: 2px solid {entryColor};
                border-radius: 8px;
                padding: 8px 12px;
                font-size: 14px;
            }}
            QLineEdit:hover {{
                border-color: {entryBorderColor};
            }}
            QLineEdit:focus {{
                border-color: {entryBorderColor};
                background-color: {entryBgColor};
            }}
        """)

        # Entry to enter the new budget
        self.budgetEntry = QDoubleSpinBox()
        self.budgetEntry.setDecimals(2)
        self.budgetEntry.setMaximum(10_000_000)

        # Getting suffix from json file
        # TODO: Option to select between sufix and prefix
        with open('data/config.json', 'r') as f:
            data = json.load(f)
            currencySuffix = f' {data["CurrencySuffix"]}'
        self.budgetEntry.setSuffix(currencySuffix)
        self.budgetEntry.setStyleSheet(f'''
            QDoubleSpinBox {{
                background-color: {entryBgColor};
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
            
            ''')

        # Enter button to save the entered data
        submitBtn = QPushButton('Enter')
        submitBtn.setStyleSheet(f'''
            QPushButton {{
                background-color: {buttonBgColor};
                color: black;
                padding: 10px 20px 10px 20px;
                border-radius: 8px;
                border: 2px solid black;
                font-size: 18px;
                text-align: left;
            }}
            QPushButton:hover {{
                background-color: {buttonHoverBgColor};
            }}
            QPushButton:pressed {{
                background-color: {buttonClickedBgColor};
            }}
            ''')
        submitBtn.clicked.connect(self.changeName)

        # Adding each element to the main page layout
        pageLayout.addWidget(backButton)
        pageLayout.addWidget(self.headingLabel)
        pageLayout.addWidget(self.enterName)
        pageLayout.addWidget(self.budgetEntry)
        pageLayout.addWidget(submitBtn)


        pageLayout.addStretch()

        centralWidget = QWidget()
        centralWidget.setLayout(pageLayout)
        centralWidget.setStyleSheet(f'background-color: {themePrimary}; color: {font_color1};')
        self.setCentralWidget(centralWidget)

    def changeName(self):
        '''
        Function to change the name of the user in the json file.
        '''
        newName = self.enterName.text()
        if len(newName) != 0:
            with open('data/config.json', 'r') as f:
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