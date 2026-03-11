'''
This file controls all the GUI elements of Settings window.
This file will get opened by main.py whenever the Settings button is clicked or the shortcut used.
'''

# Importing GUI elements
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QFrame, QLineEdit, QHBoxLayout, QFileDialog, QComboBox
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

    def __init__(self, ThemeManager):
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
        # Theme
        with open('data/config.json', 'r') as f:
            data = json.load(f)
            currentTheme = data['CurrentTheme']
            themes = []
            for i in data['Themes'][0].keys():
                themes.append(i)

        self.themeManager = ThemeManager()
        self.themeManager.themeChanged.connect(self.refreshTheme)

        # Heading
        self.headingLabel = QLabel("""Settings
─────────────────────────────────────────────────────────────────────────────────────────""")
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

        # Card for all the settings elements
        pathCard = QFrame()
        pathCard.setStyleSheet('''
            font-size: 18px;
            font-family: Adwaita mono;
        ''')

        # Layout for the settings elements (Horizontal)
        pathCardLayout = QHBoxLayout(pathCard)
        pathCardLayout.setAlignment(Qt.AlignLeft)
        pathCardLayout.setSpacing(100)

        # Button to change the report exporting path
        self.exportBtn = QPushButton('Export Path')
        self.exportBtnBaseStyle = '''
            QPushButton {
                padding: 10px 20px 10px 20px;
                border-radius: 8px;
                font-size: 16px;
                text-align: left;
            }
        '''
        self.exportBtn.clicked.connect(self.pathChanger)

        # 'Entry' to enter new currency symbol
        self.currencyEntry = QLineEdit()
        self.currencyEntry.setPlaceholderText('Currency Symbol')
        self.currencyEntry.setFixedWidth(230)
        self.currencyEntryBaseStyle = '''
                QLineEdit {
                font-size: 18px;
                font-family: Adwaita mono;
                padding-top: 7px;
                padding-bottom: 7px;
                padding-left: 15px;
                border-radius: 10px;
            }
            '''

        # Card to hold currency entry and and save button
        currencyCard = QFrame()
        currencyCard.setStyleSheet('''
            font-size: 18px;
            font-family: Adwaita mono;
        ''')

        # Button to save the new currency
        self.saveBtn = QPushButton('Save')
        self.saveBtn.setFixedWidth(85)
        self.saveBtnBaseStyle = '''
            QPushButton {
                padding: 10px 20px 10px 20px;
                border-radius: 8px;
                font-size: 16px;
                text-align: left;
            }
        '''
        self.saveBtn.clicked.connect(self.saveSettings)

        # Layout to hold currency entry and and save button
        currencyCardLayout = QHBoxLayout(currencyCard)
        currencyCardLayout.setAlignment(Qt.AlignLeft)
        currencyCardLayout.addWidget(self.currencyEntry)
        currencyCardLayout.addWidget(self.saveBtn)

        # Theme changing option
        self.themeCard = QFrame()
        self.themeCardBaseStyle = '''
            border-radius: 10px;
            font-size: 24px;
            font-family: Adwaita mono;
            padding-top: 10px;
            padding-bottom: 10px;
            margin-left: 5px;
            margin-right: 5px;
        '''

        themeCardLayout = QHBoxLayout(self.themeCard)
        themeCardLayout.setAlignment(Qt.AlignLeft)
        themeCardLayout.setSpacing(50)
        self.themeLabel = QLabel('Theme')

        # shortcutCard, creation made earlier so that the element added later can have the card to be added onto
        self.shortcutsCard = QFrame()
        self.shortcutsCardBaseStyle = '''
            font-size: 18px;
            font-family: Adwaita mono;
            border-radius: 10px;
        '''

        shortcutsDisplayLayout = QVBoxLayout(self.shortcutsCard)
        shortcutsDisplayLayout.setAlignment(Qt.AlignLeft)
        shortcutsDisplayLayout.setSpacing(10)

        self.themeMenu = QComboBox()
        self.themeMenuBaseStyle = """
            QComboBox {
                font-size: 18px;
                padding: 8px;
                border-radius: 5px;
                font-family: Adwaita mono;
            }
        """

        themes.remove(currentTheme)
        themes.insert(0, currentTheme)
        self.themeMenu.addItems(themes)
        self.themeMenu.currentTextChanged.connect(self.changeTheme)

        themeCardLayout.addWidget(self.themeLabel)
        themeCardLayout.addWidget(self.themeMenu)


        '''
        Export button and card that holds currency entry and save button added to pathCardLayout.
        currencyCard was added PathCardLayout so that the elements inside currencyCardLayout will,
        stay in the same horizontal line with export button.
        '''
        pathCardLayout.addWidget(self.exportBtn)
        pathCardLayout.addWidget(currencyCard)

        # Shortcuts
        '''
        All the available shortcuts in the program being displayed in the settings window.
        '''

        self.shortcutHeading1 = QLabel('Homepage')
        self.shortcutHeading1BaseStyle = 'font-size: 22px;'

        self.shortcutLabel1 = QLabel('Ctrl + R: Refresh')
        self.shortcutLabel1BaseStyle = '''
            padding-left: 15px;
        '''
        self.shortcutLabel2 = QLabel('Alt + 1: Add Transaction')
        self.shortcutLabel2BaseStyle = '''
            padding-left: 15px;
        '''
        self.shortcutLabel3 = QLabel('Alt + 2: Edit Expense')
        self.shortcutLabel3BaseStyle = '''
            padding-left: 15px;
        '''
        self.shortcutLabel4 = QLabel('Alt + 3: Edit Income')
        self.shortcutLabel4BaseStyle = '''
            padding-left: 15px;
        '''
        self.shortcutLabel5 = QLabel('Alt + 4: History')
        self.shortcutLabel5BaseStyle = '''
            padding-left: 15px;
        '''
        self.shortcutLabel6 = QLabel('Alt + 5: User')
        self.shortcutLabel6BaseStyle = '''
            padding-left: 15px;
        '''
        self.shortcutLabel7 = QLabel('Alt + 6: Settings')
        self.shortcutLabel7BaseStyle = '''
            padding-left: 15px;
        '''

        self.shortcutHeading2 = QLabel('Edit Expense/Edit Income')
        self.shortcutHeading2BaseStyle = '''
            font-size: 22px;
            padding-top: 20px;
        '''

        self.shortcutLabel8 = QLabel('Ctrl + D: Delete')
        self.shortcutLabel8BaseStyle = '''
            padding-left: 15px;
        '''

        self.shortcutHeading3 = QLabel('Add Transactions / Edit Expense / Edit Income / User / Settings')
        self.shortcutHeading3BaseStyle = '''
            font-size: 22px;
            padding-top: 20px;
        '''

        self.shortcutLabel9 = QLabel('Ctrl + W: Close')
        self.shortcutLabel9BaseStyle = '''
            padding-left: 15px;
        '''

        self.dividerLine1 = QLabel('──────────────────────────────────────────────────────────────────────────────────────────')
        self.dividerLine1BaseStyle = '''
            font-size: 20px;
            font-weight: bold;
        '''

        self.dividerLine2 = QLabel('──────────────────────────────────────────────────────────────────────────────────────────')
        self.dividerLine2BaseStyle = '''
            font-size: 20px;
            font-weight: bold;
        '''

        shortcutsDisplayLayout.addWidget(self.shortcutHeading1)
        shortcutsDisplayLayout.addWidget(self.shortcutLabel1)
        shortcutsDisplayLayout.addWidget(self.shortcutLabel2)
        shortcutsDisplayLayout.addWidget(self.shortcutLabel3)
        shortcutsDisplayLayout.addWidget(self.shortcutLabel4)
        shortcutsDisplayLayout.addWidget(self.shortcutLabel5)
        shortcutsDisplayLayout.addWidget(self.shortcutLabel6)
        shortcutsDisplayLayout.addWidget(self.shortcutLabel7)
        shortcutsDisplayLayout.addWidget(self.dividerLine1)
        shortcutsDisplayLayout.addWidget(self.shortcutHeading2)
        shortcutsDisplayLayout.addWidget(self.shortcutLabel8)
        shortcutsDisplayLayout.addWidget(self.dividerLine2)
        shortcutsDisplayLayout.addWidget(self.shortcutHeading3)
        shortcutsDisplayLayout.addWidget(self.shortcutLabel9)

        pageLayout.addWidget(self.backButton)
        pageLayout.addWidget(self.headingLabel)
        pageLayout.addWidget(pathCard)
        pageLayout.addWidget(self.themeCard)
        pageLayout.addWidget(self.shortcutsCard)

        pageLayout.addStretch()

        self.centralWidget = QWidget()
        self.centralWidget.setLayout(pageLayout)
        self.setCentralWidget(self.centralWidget)
        self.changeTheme(self.themeMenu.currentText()) # This is here so that QComboBox won't get activated before everything is setup

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

    def changeTheme(self, newTheme):
        '''with open('data/config.json', 'r') as f:
            data = json.load(f)
            data['CurrentTheme'] = newTheme

        with open('data/config.json', 'w') as f:
            json.dump(data, f, indent=4)'''

        self.themeManager.apply_theme(newTheme)

    def refreshTheme(self):
        self.headingLabel.setStyleSheet(self.headingLabelBaseStyle + self.themeManager.get_stylesheet("QLabel"))
        self.backButton.setStyleSheet(self.backButtonBaseStyle + self.themeManager.get_stylesheet("QPushButton"))
        self.exportBtn.setStyleSheet(self.exportBtnBaseStyle + self.themeManager.get_stylesheet("QPushButton"))
        self.currencyEntry.setStyleSheet(self.currencyEntryBaseStyle + self.themeManager.get_stylesheet("QLineEdit"))
        self.saveBtn.setStyleSheet(self.saveBtnBaseStyle + self.themeManager.get_stylesheet("QPushButton"))
        self.themeCard.setStyleSheet(self.themeCardBaseStyle + self.themeManager.get_stylesheet("QFrame"))
        self.themeLabel.setStyleSheet(self.themeManager.get_stylesheet("BorderDelete3px"))
        self.themeMenu.setStyleSheet(self.themeMenuBaseStyle + self.themeManager.get_stylesheet("QComboBox"))
        self.shortcutsCard.setStyleSheet(self.shortcutsCardBaseStyle + self.themeManager.get_stylesheet("QFrame"))
        self.shortcutHeading1.setStyleSheet(self.shortcutHeading1BaseStyle + self.themeManager.get_stylesheet("QLabel") + self.themeManager.get_stylesheet("BorderDelete3px"))
        self.shortcutLabel1.setStyleSheet(self.shortcutLabel1BaseStyle + self.themeManager.get_stylesheet("QLabel") + self.themeManager.get_stylesheet("BorderDelete1px"))
        self.shortcutLabel2.setStyleSheet(self.shortcutLabel2BaseStyle + self.themeManager.get_stylesheet("QLabel") + self.themeManager.get_stylesheet("BorderDelete1px"))
        self.shortcutLabel3.setStyleSheet(self.shortcutLabel3BaseStyle + self.themeManager.get_stylesheet("QLabel") + self.themeManager.get_stylesheet("BorderDelete1px"))
        self.shortcutLabel4.setStyleSheet(self.shortcutLabel4BaseStyle + self.themeManager.get_stylesheet("QLabel") + self.themeManager.get_stylesheet("BorderDelete1px"))
        self.shortcutLabel5.setStyleSheet(self.shortcutLabel5BaseStyle + self.themeManager.get_stylesheet("QLabel") + self.themeManager.get_stylesheet("BorderDelete1px"))
        self.shortcutLabel6.setStyleSheet(self.shortcutLabel6BaseStyle + self.themeManager.get_stylesheet("QLabel") + self.themeManager.get_stylesheet("BorderDelete1px"))
        self.shortcutLabel7.setStyleSheet(self.shortcutLabel7BaseStyle + self.themeManager.get_stylesheet("QLabel") + self.themeManager.get_stylesheet("BorderDelete1px"))
        self.shortcutHeading2.setStyleSheet(self.shortcutHeading2BaseStyle + self.themeManager.get_stylesheet("QLabel") + self.themeManager.get_stylesheet("BorderDelete1px"))
        self.shortcutLabel8.setStyleSheet(self.shortcutLabel8BaseStyle + self.themeManager.get_stylesheet("QLabel") + self.themeManager.get_stylesheet("BorderDelete1px"))
        self.shortcutHeading3.setStyleSheet(self.shortcutHeading3BaseStyle + self.themeManager.get_stylesheet("QLabel") + self.themeManager.get_stylesheet("BorderDelete1px"))
        self.shortcutLabel9.setStyleSheet(self.shortcutLabel9BaseStyle + self.themeManager.get_stylesheet("QLabel") + self.themeManager.get_stylesheet("BorderDelete1px"))
        self.dividerLine1.setStyleSheet(self.dividerLine1BaseStyle + self.themeManager.get_stylesheet("QLabel"))
        self.dividerLine2.setStyleSheet(self.dividerLine2BaseStyle + self.themeManager.get_stylesheet("QLabel"))
        self.centralWidget.setStyleSheet(self.themeManager.get_stylesheet("PrimaryASecondary"))