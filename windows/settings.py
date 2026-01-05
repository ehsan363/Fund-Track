from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QFrame, QLineEdit, QHBoxLayout
from PySide6.QtGui import QIcon, QFont, QKeySequence
from PySide6.QtCore import Qt, Signal

class settingsWindow(QMainWindow):
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
        self.headingLabel = QLabel("""Settings
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

        pathCard = QFrame()
        pathCard.setStyleSheet('''
            font-size: 18px;
            font-family: Adwaita mono;
            background-color: #222222;
            border-radius: 10px;
            border: 2px solid #ed7521;''')

        pathCardLayout = QHBoxLayout(pathCard)
        pathCardLayout.setAlignment(Qt.AlignLeft)

        self.pathEnter = QLineEdit()
        self.pathEnter.setPlaceholderText('Enter Path')
        self.pathEnter.setStyleSheet("""
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
        enterBtn = QPushButton('Enter')
        enterBtn.setStyleSheet('''
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
        enterBtn.clicked.connect(self.pathChanger)

        pathCardLayout.addWidget(self.pathEnter)
        pathCardLayout.addWidget(enterBtn)

        # Shortcuts
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
        self.setCentralWidget(centralWidget)  # <-- Stuff into Central Widget

    def pathChanger(self):
        with open('helper/reportSavingPath.txt', 'w') as Path:
            Path.write(self.pathEnter.text())
        self.goHome_Signal.emit()