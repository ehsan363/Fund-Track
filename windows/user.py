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

    def __init__(self, ThemeManager):
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
        '''
            mainWidget is one in which all the elements that should be in the central widget is added
        '''
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(pageLayout)
        self.setCentralWidget(self.mainWidget)

        # Theme
        with open('data/config.json', 'r') as f:
            data = json.load(f)
            currentTheme = data['CurrentTheme']

        self.themeManager = ThemeManager()
        self.themeManager.themeChanged.connect(self.refreshTheme)

        # Heading
        self.headingLabel = QLabel("""User
──────────────────────────────────────────────────────────────────────────────────────────""")
        self.headingLabel.setAlignment(Qt.AlignLeft)
        self.headingLabelBaseStyle = """
            font-size: 36px;
            font-family: DejaVu Sans Mono;
            padding-top: 15px;
            padding-left: 10px;
        """

        # Back button to return to Homepage
        self.backButton = QPushButton(QIcon('img/back_icon.png'), 'Back')
        self.backButton.setShortcut(QKeySequence('Ctrl+W')) # Shortcut key instead of pressing the button
        self.backButtonBaseStyle = '''
            QPushButton {
                padding: 10px 20px 10px 20px;
                border-radius: 8px;
                font-size: 16px;
                text-align: left;
            }
        '''
        self.backButton.clicked.connect(self.goHome_Signal.emit)

        # Entry to enter the new name
        self.enterName = QLineEdit()
        self.enterName.setPlaceholderText('Enter Your Name')
        self.enterNameBaseStyle = """
            QLineEdit {
                border-radius: 8px;
                padding: 8px 12px;
                font-size: 14px;
            }
        """

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
        self.budgetEntryBaseStyle = '''
            QDoubleSpinBox {
                border-radius: 8px;
                padding: 6px 10px;
                font-size: 16px;
            }
        '''

        # Enter button to save the entered data
        self.submitBtn = QPushButton('Enter')
        self.submitBtnBaseStyle = '''
            QPushButton {
                padding: 10px 20px 10px 20px;
                border-radius: 8px;
                font-size: 18px;
                text-align: left;
            }
        '''
        self.submitBtn.clicked.connect(self.changeName)

        # Adding each element to the main page layout
        pageLayout.addWidget(self.backButton)
        pageLayout.addWidget(self.headingLabel)
        pageLayout.addWidget(self.enterName)
        pageLayout.addWidget(self.budgetEntry)
        pageLayout.addWidget(self.submitBtn)
        self.refreshTheme()


        pageLayout.addStretch()

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


    def refreshTheme(self):
        '''
            Function to refresh the theme color values of every element in this window using the class ThemeManager.
        '''
        self.headingLabel.setStyleSheet(self.headingLabelBaseStyle + self.themeManager.get_stylesheet("QLabel"))
        self.backButton.setStyleSheet(self.backButtonBaseStyle + self.themeManager.get_stylesheet("QPushButton"))
        self.enterName.setStyleSheet(self.enterNameBaseStyle + self.themeManager.get_stylesheet("QLineEdit") + self.themeManager.get_stylesheet("font_color1"))
        self.budgetEntry.setStyleSheet(self.budgetEntryBaseStyle + self.themeManager.get_stylesheet("QDoubleSpinBox") + self.themeManager.get_stylesheet("font_color1"))
        self.submitBtn.setStyleSheet(self.submitBtnBaseStyle + self.themeManager.get_stylesheet("QPushButton"))
        self.mainWidget.setStyleSheet(self.themeManager.get_stylesheet("PrimaryASecondary"))