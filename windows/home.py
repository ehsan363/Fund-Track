'''
This file controls all the GUI elements of the homepage window.
This file will get opened by the main.py file when the application is started, and when
the back button is pressed form any of the subwindows.
This window does not give the data for the labels which can update their info, they are done by another file, HPrefresher.py.
This is so that when you click the refresh button or when you come back to the Homepage after you made some changes,
we can update the changes onto the homepage
'''

# Importing GUI elements
from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QToolBar, QFrame
from PySide6.QtGui import QAction, QFont, QIcon, QKeySequence
from PySide6.QtCore import Qt, Signal

# Importing functions from other files
from data.database import DBmanager
from helper.barchartMatplotlib import initiation, plot_bar_chart
from helper.HPrefresher import summaryCardRefresher, transactionHistoryRefresher, greetingRefresh, barchartRefresher

# json to write and read json files
import json

class MainWindow(QMainWindow):
    '''
    Controls all the GUI elements and functions of the homepage.
    Include:
    - Displaying a greeting for the user
    - A barchart using matplotlib of Income and Expense
    - Five recent transactions
    - Displays budget, expense and whats left under summary
    '''
    refresh_Signal = Signal()
    addTransaction_Signal = Signal()
    editExpense_Signal = Signal()
    editIncome_Signal = Signal()
    history_Signal = Signal()
    user_Signal = Signal()
    settings_Signal = Signal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('FundTrack')

        # Window settings
        self.resize(1920, 1080)

        self.setWindowIcon(QIcon('img/iconOrange141414bgR.png'))

        # Font elements
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)

        # Layouts
        '''
        The final layout in which all the elements are at last added on to
        '''
        pageLayout = QVBoxLayout()
        pageLayout.setAlignment(Qt.AlignTop)
        pageLayout.setSpacing(35)

        '''
        Layout for the elements that are the top row of the whole windows. Such as the 'Summary' and greeting
        '''
        topRow = QHBoxLayout()
        topRow.setAlignment(Qt.AlignLeft)
        topRow.setSpacing(350)

        '''
        Layout for the elements on the bottom row of the window. Such as the recent transaction list and the barchart
        '''
        bottomRow = QHBoxLayout()
        bottomRow.setAlignment(Qt.AlignLeft)
        bottomRow.setSpacing(210)

        # Create UI elements
        # Theme
        with open('data/config.json', 'r') as f:
            data = json.load(f)
            currentTheme = data['CurrentTheme']
            for i in data['Themes']:
                themePrimary = i[currentTheme]['Primary']
                themeSecondary = i[currentTheme]['Secondary']

                buttonConfig = i[currentTheme]['Button']
                buttonBgColor = buttonConfig['bgcolor']

                fontConfig = i[currentTheme]["Font"]

                font_color0 = fontConfig['font-color0']
                font_color1 = fontConfig['font-color1']


        # Toolbar options
        toolbar = QToolBar("Main Toolbar", self)
        self.addToolBar(toolbar)
        toolbar.setMovable(False)
        toolbar.setStyleSheet(f'''
            Background-color: {buttonBgColor};
            font-size: 20px;
            border-radius: 15px;
            margin: 5px;
            padding-top: 5px;
        ''')
        toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        '''
        1. Icon and text for the option
        2. Adding the option to the toolbar
        3. Adding function to the option
        4. Adding shortcut key to the option
        '''
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
        '''
        Homepage text added without any rows.
        '''
        self.headingLabel = QLabel("HomePage")
        self.headingLabel.setAlignment(Qt.AlignLeft)
        self.headingLabel.setStyleSheet(f"""
            font-size: 36px;
            font-family: DejaVu Sans Mono;
            padding-top: 15px;
            padding-left: 10px;
            color: {font_color0}
        """)

        # Top row
        '''
        Top row is after the "HomePage" text on the top of the window.
        summaryCard is to hold the elements inside the summary.
        summaryLayout is the layout of the card. I used vertical and therefore the elements inside are vertical in order.
        
        greetingCard is the card in which the label with the greeting text shows in the window.
        greetingLayout is the layout of the greetingCard. The card greets the user whenever they enter the homepage.
        '''
        summaryCard = QFrame() # Summary card
        summaryCard.setFixedWidth(450)
        summaryCard.setStyleSheet(f"""
            background-color: {themeSecondary};
            font-family: Noto Sans Mono Thin;
            font-weight: bold;
            padding: 10px;
            border-radius: 20px;
            margin-left: 20px;
        """)

        self.summaryLabel = QLabel('Summary')
        self.summaryLabel.setStyleSheet(f"""
            font-size: 28px;
            color: {font_color1};
            font-weight: bold;
            margin-left: 30px;
            padding-top: 5px;
            margin-top: 20px;
        """)

        self.budgetLabel = QLabel()
        self.budgetLabel.setAlignment(Qt.AlignTop)
        self.budgetLabel.setStyleSheet(f'''
            font-size: 18px;
            color: {font_color0};
        ''')

        summaryLayout = QVBoxLayout(summaryCard)
        summaryLayout.addWidget(self.summaryLabel)
        summaryLayout.addWidget(self.budgetLabel)

        topRow.addWidget(summaryCard)


        # Card for Greeting
        greetingCard = QFrame()
        greetingCard.setFixedWidth(1050)
        greetingCard.setFixedHeight(100)
        greetingCard.setStyleSheet(f'''
            font-family: Caladea;
            font-weight: bold;
            background-color: {themeSecondary};
            color: {font_color1};
            font-size: 26px;
            border-radius: 15px;''')

        self.greetingLabel = QLabel()
        self.greetingLabel.setAlignment(Qt.AlignCenter)

        greetingLayout = QVBoxLayout(greetingCard)
        greetingLayout.addWidget(self.greetingLabel)

        topRow.addWidget(greetingCard)

        # Bottom row
        '''
        Bottom Row is after the top row, obviously and here the elements on the bottom part of the window are added.
        historyCard is the card in which the five most recent transactions will be shown.
        historyLayout is layout for historyCard. It is vertical, therefore the labels in vertical order.
        
        barCard is the card in which the canvas for matplotlib goes.
        barLayout is the layout for barCard to display the barchart.
        The barchart is drawn using functions which are located in other file. Only the final data is being used
        in this file.
        '''
        historyCard = QFrame()
        historyCard.setFixedWidth(900)
        historyCard.setStyleSheet(f'''
            font-size: 22px;
            color: {font_color1};
            background-color: {themeSecondary};
            border-radius: 15px;
            margin-left: 20px;
            font-family: Noto Sans Mono Thin;
            font-weight: bold;
            padding-bottom: 10px;
            padding-right: 10px;
        ''')

        self.historyLabel = QLabel('Transaction History')
        self.historyLabel.setStyleSheet('padding-top: 10px;')

        self.historyLayout = QVBoxLayout(historyCard)
        self.historyLayout.addWidget(self.historyLabel)

        # Bar chart with Matplotlib
        barCard = QFrame()
        barCard.setFixedWidth(750)
        barCard.setStyleSheet(f'''
            background-color: {themeSecondary};
            border: 2px solid {themeSecondary};
            border-radius: 20px;
        ''')


        self.figure, self.canvas = initiation()
        self.plt = plot_bar_chart(self.figure, self.canvas)

        barLayout = QVBoxLayout(barCard)
        barLayout.addWidget(self.canvas)

        bottomRow.addWidget(historyCard)
        bottomRow.addWidget(barCard)

        pageLayout.addWidget(self.headingLabel)
        pageLayout.addLayout(topRow)
        pageLayout.addLayout(bottomRow)

        pageLayout.addStretch()

        centralWidget = QWidget()
        centralWidget.setLayout(pageLayout)
        centralWidget.setStyleSheet(f'background-color: {themePrimary}; color: {font_color1};')
        self.setCentralWidget(centralWidget)

        self.refresh()

    def refresh(self):
        '''
        Function to refresh every data inside the homepage window.
        This function calls other individual functions which are assigned to refresh the data of each element
        in the homepage window.
        '''
        summaryCardRefresher(self.budgetLabel)
        transactionHistoryRefresher(self.historyLayout)
        greetingRefresh(self.greetingLabel)
        barchartRefresher(self.plt, self.figure, self.canvas)
