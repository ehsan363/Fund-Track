'''
This file controls all the GUI elements of Settings window.
This file will get opened by main.py whenever the Settings button is clicked or the shortcut used.
'''

# Importing GUI elements
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QFrame, QLineEdit, QHBoxLayout, QFileDialog
from PySide6.QtGui import QIcon, QFont, QKeySequence
from PySide6.QtCore import Qt, Signal

# json to read and write json file for the options selected
import json

class settingsWindow(QMainWindow):
    '''
    Controls all the GUI elements and functions of Settings window.
    Includes:
    - Changing the finance report path
    - Changing the currency suffix
    '''
    goHome_Signal = Signal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('FundTrack')

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

        # UI elements
        # Heading
        self.headingLabel = QLabel("""Settings
──────────────────────────────────────────────────────────────────────────────────────────""")
        self.headingLabel.setAlignment(Qt.AlignLeft)
        self.headingLabel.setStyleSheet("""
            font-size: 36px;
            font-family: DejaVu Sans Mono;
            padding-top: 15px;
            padding-left: 10px;""")

        # Back button to return to Homepage
        backButton = QPushButton(QIcon('img/back_icon.png'), 'Back')
        backButton.setShortcut(QKeySequence('Ctrl+W')) # Shortcut key instead of pressing the button
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

        # Card for all the settings elements
        pathCard = QFrame()
        pathCard.setStyleSheet('''
            font-size: 18px;
            font-family: Adwaita mono;''')

        # Layout for the settings elements (Horizontal)
        pathCardLayout = QHBoxLayout(pathCard)
        pathCardLayout.setAlignment(Qt.AlignLeft)

        # Button to change the report exporting path
        exportBtn = QPushButton('Export Path')
        exportBtn.setStyleSheet('''
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
        exportBtn.clicked.connect(self.pathChanger)

        # 'Entry' to enter new currency symbol
        self.currencyEntry = QLineEdit()
        self.currencyEntry.setPlaceholderText('Currency Symbol')
        self.currencyEntry.setFixedWidth(230)
        self.currencyEntry.setStyleSheet('''
            font-size: 18px;
            font-family: Adwaita mono;
            margin-left: 35px;
            border: 2px solid #ed7521;
            border-radius: 10px;
            padding: 5px 10px 5px;
            ''')

        # Card to hold currency entry and and save button
        currencyCard = QFrame()
        currencyCard.setStyleSheet('''
            font-size: 18px;
            font-family: Adwaita mono;
        ''')

        # Button to save the new currency
        saveBtn = QPushButton('Save')
        saveBtn.setFixedWidth(85)
        saveBtn.setStyleSheet('''
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
        saveBtn.clicked.connect(self.saveSettings)

        # Layout to hold currency entry and and save button
        currencyCardLayout = QHBoxLayout(currencyCard)
        currencyCardLayout.setAlignment(Qt.AlignLeft)
        currencyCardLayout.addWidget(self.currencyEntry)
        currencyCardLayout.addWidget(saveBtn)

        '''
        Export button and card that holds currency entry and save button added to pathCardLayout.
        currencyCard was added PathCardLayout so that the elements inside currencyCardLayout will,
        stay in the same horizontal line with export button.
        '''
        pathCardLayout.addWidget(exportBtn)
        pathCardLayout.addWidget(currencyCard)

        # Shortcuts
        '''
        All the available shortcuts in the program being displayed in the settings window.
        '''
        shortcutsCard = QFrame()
        shortcutsCard.setStyleSheet('''
            font-size: 18px;
            font-family: Adwaita mono;
            background-color: #222222;
            border-radius: 10px;
            border: 2px solid #ed7521;''')

        shortcutsDisplayLayout = QVBoxLayout(shortcutsCard)
        shortcutsDisplayLayout.setAlignment(Qt.AlignLeft)
        shortcutsDisplayLayout.setSpacing(10)

        shortcutHeading1 = QLabel('Homepage')
        shortcutHeading1.setStyleSheet('''
            font-size: 22px;
            border-radius: 0px;
            border: 2px solid #222222;''')

        shortcutLabel1 = QLabel('Ctrl + R: Refresh')
        shortcutLabel1.setStyleSheet('''
            border-radius: 0px;
            border: 2px solid #222222;
            padding-left: 15px;''')
        shortcutLabel2 = QLabel('Alt + 1: Add Transaction')
        shortcutLabel2.setStyleSheet('''
            border-radius: 0px;
            border: 2px solid #222222;
            padding-left: 15px;''')
        shortcutLabel3 = QLabel('Alt + 2: Edit Expense')
        shortcutLabel3.setStyleSheet('''
            border-radius: 0px;
            border: 2px solid #222222;
            padding-left: 15px;''')
        shortcutLabel4 = QLabel('Alt + 3: Edit Income')
        shortcutLabel4.setStyleSheet('''
            border-radius: 0px;
            border: 2px solid #222222;
            padding-left: 15px;''')
        shortcutLabel5 = QLabel('Alt + 4: History')
        shortcutLabel5.setStyleSheet('''
            border-radius: 0px;
            border: 2px solid #222222;
            padding-left: 15px;''')
        shortcutLabel6 = QLabel('Alt + 5: User')
        shortcutLabel6.setStyleSheet('''
            border-radius: 0px;
            border: 2px solid #222222;
            padding-left: 15px;''')
        shortcutLabel7 = QLabel('Alt + 6: Settings')
        shortcutLabel7.setStyleSheet('''
            border-radius: 0px;
            border: 2px solid #222222;
            padding-left: 15px;''')

        shortcutHeading2 = QLabel('Edit Expense/Edit Income')
        shortcutHeading2.setStyleSheet('''
            font-size: 22px;
            border-radius: 0px;
            border: 2px solid #222222;
            padding-top: 20px;''')

        shortcutLabel8 = QLabel('Ctrl + D: Delete')
        shortcutLabel8.setStyleSheet('''
            border-radius: 0px;
            border: 2px solid #222222;
            padding-left: 15px;''')

        shortcutHeading3 = QLabel('Add Transactions / Edit Expense / Edit Income / User / Settings')
        shortcutHeading3.setStyleSheet('''
            font-size: 22px;
            border-radius: 0px;
            border: 2px solid #222222;
            padding-top: 20px;''')

        shortcutLabel9 = QLabel('Ctrl + W: Close')
        shortcutLabel9.setStyleSheet('''
            border-radius: 0px;
            border: 2px solid #222222;
            padding-left: 15px;''')

        dividerLine1 = QLabel('──────────────────────────────────────────────────────────────────────────────────────────')
        dividerLine1.setStyleSheet('''
            font-size: 20px;
            font-weight: bold;''')

        dividerLine2 = QLabel('──────────────────────────────────────────────────────────────────────────────────────────')
        dividerLine2.setStyleSheet('''
            font-size: 20px;
            font-weight: bold;''')

        shortcutsDisplayLayout.addWidget(shortcutHeading1)
        shortcutsDisplayLayout.addWidget(shortcutLabel1)
        shortcutsDisplayLayout.addWidget(shortcutLabel2)
        shortcutsDisplayLayout.addWidget(shortcutLabel3)
        shortcutsDisplayLayout.addWidget(shortcutLabel4)
        shortcutsDisplayLayout.addWidget(shortcutLabel5)
        shortcutsDisplayLayout.addWidget(shortcutLabel6)
        shortcutsDisplayLayout.addWidget(shortcutLabel7)
        shortcutsDisplayLayout.addWidget(dividerLine1)
        shortcutsDisplayLayout.addWidget(shortcutHeading2)
        shortcutsDisplayLayout.addWidget(shortcutLabel8)
        shortcutsDisplayLayout.addWidget(dividerLine2)
        shortcutsDisplayLayout.addWidget(shortcutHeading3)
        shortcutsDisplayLayout.addWidget(shortcutLabel9)

        pageLayout.addWidget(backButton)
        pageLayout.addWidget(self.headingLabel)
        pageLayout.addWidget(pathCard)
        pageLayout.addWidget(shortcutsCard)

        pageLayout.addStretch()

        centralWidget = QWidget()
        centralWidget.setLayout(pageLayout)
        centralWidget.setStyleSheet('background-color: #141414; color: #ed7521;')
        self.setCentralWidget(centralWidget)

    def pathChanger(self):
        '''
        Function to change the path of the report exporting in the json file
        '''
        folder = QFileDialog.getExistingDirectory(self, 'Select Directory', '', QFileDialog.ShowDirsOnly)

        with open('data/config.json', 'r') as f:
            data = json.load(f)

        data['Report'][0]['Path'] = folder

        with open('data/config.json', 'w') as f:
            json.dump(data, f, indent=4)

    def saveSettings(self):
        '''
        Function to save the new currency suffix and any new settings that will be saved using the "save" button
        '''
        newCurrency = self.currencyEntry.text()

        with open('data/config.json', 'r') as f:
            data = json.load(f)

        data['CurrencySuffix'] = newCurrency

        with open('data/config.json', 'w') as f:
            json.dump(data, f, indent=4)

        self.currencyEntry.clear()