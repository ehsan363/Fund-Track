# Importing modules from PySide6 library
from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QToolBar, QFrame
from PySide6.QtGui import QAction, QFont, QIcon, QKeySequence
from PySide6.QtCore import Qt, Signal
from data.database import DBmanager
from helper.barchartMatplotlib import initiation, plot_bar_chart
from helper.HPrefresher import summaryCardRefresher, transactionHistoryRefresher, greetingRefresh, barchartRefresher

class MainWindow(QMainWindow):
    refresh_Signal = Signal()
    addTransaction_Signal = Signal()
    editExpense_Signal = Signal()
    editIncome_Signal = Signal()
    history_Signal = Signal()
    user_Signal = Signal()
    settings_Signal = Signal()

    def __init__(self):
        super().__init__()

        self.setWindowTitle('FundTrack') # Title of the window
        # Window size
        self.resize(1920, 1080)
        self.setMinimumSize(1170, 650)

        # Window icon
        self.setWindowIcon(QIcon('img/iconOrange#141414bgR.png'))
        self.setStyleSheet('background-color: #141414;')

        # Font elements
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)

        # Layout
        pageLayout = QVBoxLayout()
        pageLayout.setAlignment(Qt.AlignTop)
        pageLayout.setSpacing(35)

        topRow = QHBoxLayout()
        topRow.setAlignment(Qt.AlignLeft)
        topRow.setSpacing(350)

        bottomRow = QHBoxLayout()
        bottomRow.setAlignment(Qt.AlignLeft)
        bottomRow.setSpacing(210)

        # Create UI elements

        # Toolbar options
        toolbar = QToolBar("Main Toolbar", self)
        self.addToolBar(toolbar)
        toolbar.setMovable(False)
        toolbar.setStyleSheet('''
            Background-color: #ed7521; 
            font-size: 20px;
            border-radius: 15px;
            margin: 5px;
            padding-top: 5px;''')
        toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        action_add = QAction(QIcon('img/refresh_icon.png'),"Refresh", self)
        toolbar.addAction(action_add)
        action_add.triggered.connect(self.refresh_Signal.emit)
        action_add.setShortcut(QKeySequence('Ctrl+R'))

        action_add = QAction(QIcon('img/more_icon.png'),"Add Transaction", self)
        toolbar.addAction(action_add)
        action_add.triggered.connect(self.addTransaction_Signal.emit)
        action_add.setShortcut(QKeySequence('Alt+1'))

        action_add = QAction(QIcon('img/edit_icon(1).png'),"Edit Expense", self)
        toolbar.addAction(action_add)
        action_add.triggered.connect(self.editExpense_Signal.emit)
        action_add.setShortcut(QKeySequence('Alt+2'))

        action_add = QAction(QIcon('img/edit_icon.png'), "Edit Income", self)
        toolbar.addAction(action_add)
        action_add.triggered.connect(self.editIncome_Signal.emit)
        action_add.setShortcut(QKeySequence('Alt+3'))

    action_add = QAction(QIcon('img/edit_icon.png'),"Edit Income", self)
    toolbar.addAction(action_add)
    action_add.triggered.connect(self.editIncome_Signal.emit)
    action_add.setShortcut(QKeySequence('Alt+3'))
    action_add = QAction(QIcon('img/edit_icon.png'), "Edit Income", self)
    toolbar.addAction(action_add)
    action_add.triggered.connect(self.editIncome_Signal.emit)
    action_add.setShortcut(QKeySequence('Alt+3'))
    action_add = QAction(QIcon('img/edit_icon.png'),"Edit Income", self)
    toolbar.addAction(action_add)
    action_add.triggered.connect(self.editIncome_Signal.emit)
    action_add.setShortcut(QKeySequence('Alt+3'))

    action_add = QAction(QIcon('img/history_icon.png'),"History", self)
        toolbar.addAction(action_add)
        action_add.triggered.connect(self.history_Signal.emit)
        action_add.setShortcut(QKeySequence('Alt+4'))

        action_add = QAction(QIcon('img/user_icon.png'),"User", self)
        action_add.triggered.connect(self.user_Signal.emit)
        toolbar.addAction(action_add)
        action_add.setShortcut(QKeySequence('Alt+5'))

        action_add = QAction(QIcon('img/settings_icon.png'),"Settings", self)
        toolbar.addAction(action_add)
        action_add.triggered.connect(self.settings_Signal.emit)
        action_add.setShortcut(QKeySequence('Alt+6'))


        # No row
        self.headingLabel = QLabel("HomePage")
        self.headingLabel.setAlignment(Qt.AlignLeft)
        self.headingLabel.setStyleSheet("""
            font-size: 36px;
            font-family: DejaVu Sans Mono;
            padding-top: 15px;
            padding-left: 10px;""")

        # Top row
        summaryCard = QFrame() # Summary card
        summaryCard.setFixedWidth(450)
        summaryCard.setStyleSheet("""
            background-color: #222222;
            font-family: Noto Sans Mono Thin;
            font-weight: bold;
            padding: 10px;
            border-radius: 20px;
            margin-left: 20px;""")

        self.summaryLabel = QLabel('Summary')
        self.summaryLabel.setStyleSheet("""
            font-size: 28px;
            color: White;
            font-weight: bold;
            margin-left: 30px;
            padding-top: 5px;
            margin-top: 20px;""")

        self.budgetLabel = QLabel()
        self.budgetLabel.setAlignment(Qt.AlignTop)
        self.budgetLabel.setStyleSheet('font-size: 18px;')

        summaryLayout = QVBoxLayout(summaryCard)
        summaryLayout.addWidget(self.summaryLabel)
        summaryLayout.addWidget(self.budgetLabel)

        topRow.addWidget(summaryCard)


        # Greeting card
        greetingCard = QFrame()
        greetingCard.setFixedWidth(1050)
        greetingCard.setFixedHeight(100)
        greetingCard.setStyleSheet('''
            font-family: Caladea;
            font-weight: bold;
            background-color: #222222;
            color: White;
            font-size: 26px;
            border-radius: 15px;''')

        self.greetingLabel = QLabel()
        self.greetingLabel.setAlignment(Qt.AlignCenter)

        greetingLayout = QVBoxLayout(greetingCard)
        greetingLayout.addWidget(self.greetingLabel)

        topRow.addWidget(greetingCard)

        # Bottom row
        historyCard = QFrame()
        historyCard.setFixedWidth(900)
        historyCard.setStyleSheet('''
            font-size: 22px;
            color: White;
            background-color: #222222;
            border-radius: 15px;
            margin-left: 20px;
            font-family: Noto Sans Mono Thin;
            font-weight: bold;
            padding-bottom: 10px;
            padding-right: 10px;''')

        self.historyLabel = QLabel('Transaction History')
        self.historyLabel.setStyleSheet('padding-top: 10px;')

        self.historyLayout = QVBoxLayout(historyCard)
        self.historyLayout.addWidget(self.historyLabel)

        # Bargraph with Matplotlib
        barCard = QFrame()
        barCard.setFixedWidth(700)
        barCard.setStyleSheet('''
            border-radius: 20px;''')


        self.figure, self.canvas = initiation()
        self.plt = plot_bar_chart(self.figure, self.canvas)

        barLayout = QVBoxLayout(barCard)
        barLayout.addWidget(self.canvas)

        bottomRow.addWidget(historyCard)
        bottomRow.addWidget(barCard)

        pageLayout.addWidget(self.headingLabel)
        pageLayout.addLayout(topRow)
        pageLayout.addLayout(bottomRow)

        pageLayout.addStretch() # <-- Should be last! To make everything in layout align to the left

        centralWidget = QWidget()
        centralWidget.setLayout(pageLayout)
        centralWidget.setStyleSheet('background-color: #141414; color: #ed7521;')
        self.setCentralWidget(centralWidget) # <-- Stuff into Central Widget

        self.refresh()

    def showHomepage(self):
        self.show()
        self.refresh()

    def refresh(self):
        summaryCardRefresher(self.budgetLabel)
        transactionHistoryRefresher(self.historyLayout)
        greetingRefresh(self.greetingLabel)
        barchartRefresher(self.plt, self.figure, self.canvas)