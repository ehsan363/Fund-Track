from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QDoubleSpinBox, QDateEdit, QComboBox, QTextEdit, QHBoxLayout, QFrame, QCheckBox
from PySide6.QtGui import QIcon, QFont, QKeySequence
from PySide6.QtCore import Qt, Signal, QDate
from helper.dateAndTime import todayDate, dateFormat
from data.database import DBmanager

class addTransactionWindow(QMainWindow):
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

        row5 = QHBoxLayout()
        row5.setAlignment(Qt.AlignLeft)

        # UI elements
        # Heading
        self.headingLabel = QLabel("""Add Transaction
──────────────────────────────────────────────────────────────────────────────────────────""")
        self.headingLabel.setAlignment(Qt.AlignLeft)
        self.headingLabel.setStyleSheet("""
            font-size: 36px;
            font-family: DejaVu Sans Mono;
            padding-top: 15px;
            padding-left: 10px;""")

        backButton = QPushButton(QIcon('img/back_icon.png'),'Back')
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

        # Date
        row1Card = QFrame()
        row1Card.setStyleSheet('''
            font-size: 18px;
            padding-left: 15px;
            padding-top: 10px;''')

        self.dateEntry = QDateEdit()
        self.dateEntry.setDate(todayDate())
        self.dateEntry.setCalendarPopup(True)
        self.dateEntry.setDisplayFormat('dd-MM-yyyy')
        self.dateEntry.setFixedWidth(150)
        calendar = self.dateEntry.calendarWidget()
        calendar.setMinimumSize(360, 300)
        self.dateEntry.setStyleSheet("""
        QDateEdit {
            background-color: #222;
            color: #eee;
            border: 1px solid #444;
            border-radius: 8px;
            padding: 6px 10px;
            font-size: 14px;
        }
        
        QDateEdit:hover {
            border: 1px solid #666;
        }
        
        QDateEdit:focus {
            border: 1px solid #ed7521;
        }
        
        QDateEdit::drop-down {
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 24px;
            border-left: 1px solid #444;
        }
        
        QDateEdit::down-arrow {
            image: url(img/down_icon.png);
            width: 14px;
            height: 14px;
        }
        QCalendarWidget QToolButton#qt_calendar_prevmonth {
            qproperty-icon: url(img/chevron-left.png);
            qproperty-iconSize: 16px;
        }
        
        QCalendarWidget QToolButton#qt_calendar_nextmonth {
            qproperty-icon: url(img/chevron-right.png);
            qproperty-iconSize: 16px;
        }
        QCalendarWidget QAbstractItemView {
           font-size: 16px;
        }""")

        row1CardLayout = QHBoxLayout(row1Card)
        row1CardLayout.addWidget(self.dateEntry)

        # Amount
        row2Card = QFrame()
        row2Card.setStyleSheet('''
            font-size: 18px;
            padding-left: 15px;''')

        self.amountEntry = QDoubleSpinBox()
        self.amountEntry.setDecimals(2)
        self.amountEntry.setMaximum(10_000_000)
        self.amountEntry.setSuffix(' AED')
        self.amountEntry.setStyleSheet('''
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

        # Type
        self.typeEntry = QComboBox()
        self.typeEntry.addItems(['Income', 'Expense'])
        self.typeEntry.setStyleSheet("""
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

        row2CardLayout = QHBoxLayout(row2Card)
        row2CardLayout.setSpacing(40)
        row2CardLayout.addWidget(self.amountEntry)
        row2CardLayout.addWidget(self.typeEntry)

        # Category
        row3Card = QFrame()
        row3Card.setStyleSheet('''
            font-size: 18px;
            padding-left: 15px;''')

        self.categoryEntry = QComboBox()
        # Should change this to be extracted from the file and the selected "type"
        self.categoryEntry.setStyleSheet("""
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

        # Account
        self.accountEntry = QComboBox()
        self.accountEntry.addItems(["Cash", "Bank", "Credit Card"])
        self.accountEntry.setStyleSheet("""
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

        row3CardLayout = QHBoxLayout(row3Card)
        row3CardLayout.setSpacing(40)
        row3CardLayout.addWidget(self.categoryEntry)
        row3CardLayout.addWidget(self.accountEntry)

        self.typeEntry.currentTextChanged.connect(self.categoryChange)
        self.categoryChange(self.typeEntry.currentText())

        # Description
        row4Card = QFrame()
        row4Card.setStyleSheet('''
            font-size: 18px;
            padding-left: 10px;
            padding-top: 5px;
            font-family: Adwaita mono;''')

        self.descriptionLabel = QLabel('Description')
        self.descriptionLabel.setStyleSheet('''
            font-size: 18px;''')

        self.descriptionEntry = QTextEdit()
        self.descriptionEntry.setStyleSheet('''
            font-size: 18px;
            background-color: #222222;
            border-radius: 10px;
            border: 2px solid #ed7521;''')

        row4CardLayout = QVBoxLayout(row4Card)
        row4CardLayout.addWidget(self.descriptionLabel)
        row4CardLayout.addWidget(self.descriptionEntry)

        # Add Button
        self.submitBtn = QPushButton('Enter')
        self.submitBtn.setShortcut(QKeySequence('Alt+A'))
        self.submitBtn.clicked.connect(self.enterDate)
        self.submitBtn.setStyleSheet('''
            QPushButton {
                background-color: #ed7521;
                color: black;
                padding: 10px 20px 10px 20px;
                border-radius: 8px;
                font-size: 18px;
                text-align: center;
                
            }
            QPushButton:hover {
                background-color: #f08337;
            }
            QPushButton:pressed {
                background-color: #ed6709;
            }
        ''')

        self.resetCh = QCheckBox('Do not reset')
        self.resetCh.setStyleSheet('''
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
        centralWidget.setStyleSheet('background-color: #141414; color: #ed7521;')
        self.setCentralWidget(centralWidget)  # <-- Stuff into Central Widget

    def resetForm(self):
        self.dateEntry.setDate(QDate.currentDate())
        self.amountEntry.setValue(0.0)
        self.typeEntry.setCurrentIndex(0)
        self.categoryEntry.setCurrentIndex(0)
        self.accountEntry.setCurrentIndex(0)
        self.descriptionEntry.clear()

    def enterDate(self):
        db = DBmanager()
        amount = self.amountEntry.text()
        IorE = self.typeEntry.currentText()
        category = self.categoryEntry.currentText()
        date = self.dateEntry.text()
        new_date = dateFormat(date)
        description = self.descriptionEntry.toPlainText()
        account = self.accountEntry.currentText()
        amount = amount.rstrip(' AED')

        db.addTransactionToDB(float(amount), IorE.lower(), category, new_date, description, account)
        if self.resetCh.isChecked():
            pass
        else:
            self.resetForm()

    def categoryChange(self, typeSelected):
        self.categoryEntry.clear()

        db = DBmanager()
        self.categoryDBIncome = db.categories('income')
        self.categoryDBExpense = db.categories('expense')
        db.close()

        if typeSelected == 'Income':
            self.categoryEntry.addItems(self.categoryDBIncome)
        else:
            self.categoryEntry.addItems(self.categoryDBExpense)