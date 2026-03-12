from PySide6.QtCore import QObject, Signal
import json

class ThemeManager(QObject):
    themeChanged = Signal()
    _instance = None

    def __new__(cls):
        '''
        Function to create the instance in the memeory so that it can be used by every window.
        '''
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        '''
        Function checks if there is "_initialized" attribute inside the object.
        Only configures the object if attribute "_initialized" is False, and loads the current theme.
        '''
        if not hasattr(self, "_initialized"):
            super().__init__()
            self._initialized = True
            self.colors = {}
            self.load_theme()

    def load_theme(self):
        '''
        Function to load the current theme.
        This function will fetch all the theme values from the config.json file.
        '''
        with open('data/config.json', 'r') as f:
            data = json.load(f)
        self.currentTheme = data["CurrentTheme"]
        self.colors = data["Themes"][0][self.currentTheme]

    def apply_theme(self, chosen_theme):
        '''
        1, This function will apply the chosen theme to the current theme.
        2, Then fetches the values for the new theme selected.
        3, Changes the current theme to the newly chosen theme.
        4, Emits signal of changed theme.
        '''
        with open('data/config.json', 'r') as f:
            data = json.load(f)

        data['CurrentTheme'] = chosen_theme
        self.colors = data['Themes'][0][chosen_theme]

        with open('data/config.json', 'w') as f:
            json.dump(data, f, indent=4)

        self.themeChanged.emit()

    def get_stylesheet(self, type):
        '''
        This function returns the stylesheet for the selected theme.
        The function returns theme colors for the element type that is inside the variable 'type'
        '''
        with open('data/config.json', 'r') as f:
            data = json.load(f)
            currentTheme = data['CurrentTheme']
            for i in data['Themes']:
                themePrimary = i[currentTheme]['Primary']
                themeSecondary = i[currentTheme]['Secondary']

                buttonConfig = i[currentTheme]['Button']
                entryConfig = i[currentTheme]['Entry']
                fontConfig = i[currentTheme]["Font"]
                sortConfig = i[currentTheme]["Sortmenu"]

                buttonBgColor = buttonConfig['bgcolor']
                buttonHoverBgColor = buttonConfig['hoverbgcolor']
                buttonClickedBgColor = buttonConfig['clickbgcolor']
                buttonColor = buttonConfig['color']

                entryBgColor = entryConfig['bgcolor']
                entryColor = entryConfig['color']
                entryBorderColor = entryConfig['bordercolor']

                font_color0 = fontConfig['font-color0']
                font_color1 = fontConfig['font-color1']
                font_color2 = fontConfig['font-color2']

                sortNormalBgColor = sortConfig["bgcolor"]

        if type == 'QFrame':
            return f'''
                        background-color: {themeSecondary};
                        border: 3px solid {font_color0};
                        color: {font_color0};
                    '''

        elif type == 'Toolbar':
            return f'''
                        background-color: {font_color0};
                        color: {font_color2}
                    '''

        elif type == 'QLabel':
            return f'''
                        color: {font_color0};
                    '''

        elif type == 'QComboBox':
            return f'''
                        color: {font_color0};
                        border: 2px solid {font_color0};
                        background-color: {sortNormalBgColor};
                    '''

        elif type == 'PrimaryASecondary':
            return f'''
                        background-color: {themePrimary}; 
                        color: {font_color1};
                    '''

        elif type == 'QPushButton':
            return f'''
                        QPushButton {{
                            background-color: {buttonBgColor};
                            color: {buttonColor};
                        }}
                        QPushButton:hover {{
                            background-color: {buttonHoverBgColor};
                        }}
                        QPushButton:pressed {{
                            background-color: {buttonClickedBgColor};
                        }}
                    '''

        elif type == 'QLineEdit':
            return f'''
                        QLineEdit {{
                            background-color: {entryBgColor};
                            border: 2px solid {entryColor};
                            color: {font_color0};
                        }}
                        QLineEdit:focus {{
                            border: 2px solid {entryBorderColor};
                        }}
                        QLineEdit:hover {{
                            border: 2px solid {entryBorderColor};
                        }}
                    '''

        elif type == 'QDoubleSpinBox':
            return f'''
                        QDoubleSpinBox {{
                            background-color: {entryBgColor};
                            border: 2px solid {entryColor};
                        }}
                        QDoubleSpinBox:focus {{
                            border: 2px solid {entryBorderColor};
                        }}
                        QDoubleSpinBox:hover {{
                            border: 2px solid {entryBorderColor};
                        }}
                    '''

        elif type == 'BorderDelete1px':
            return f'border: 1px solid {themeSecondary};'

        elif type == 'BorderDelete3px':
            return f'border: 3px solid {themeSecondary};'

        elif type == 'font_color1':
            return f'color: {font_color1};'

        elif type == 'QDateEdit':
            return f'''
                        QDateEdit {{
                            background-color: {entryBgColor};
                            border: 2px solid {entryColor};
                            border-radius: 8px;
                            padding: 6px 10px;
                            font-size: 14px;
                        }}
                        
                        QDateEdit:hover {{
                            border: 2px solid {entryBorderColor};
                        }}
                        
                        QDateEdit:focus {{
                            border: 2px solid {entryBorderColor};
                        }}
                        
                        QDateEdit::drop-down {{
                            subcontrol-origin: padding;
                            subcontrol-position: top right;
                            width: 24px;
                            border-left: 2px solid {entryBorderColor};
                        }}
                        
                        QDateEdit::down-arrow {{
                            image: url(themes/{currentTheme}/down_icon.png);
                            width: 14px;
                            height: 14px;
                        }}
                        
                        QCalendarWidget QToolButton#qt_calendar_prevmonth {{
                            qproperty-icon: url(themes/{currentTheme}/chevron-left.png);
                            qproperty-iconSize: 16px;
                        }}
                        
                        QCalendarWidget QToolButton#qt_calendar_nextmonth {{
                            qproperty-icon: url(themes/{currentTheme}/chevron-right.png);
                            qproperty-iconSize: 16px;
                        }}
                        
                        QCalendarWidget QAbstractItemView {{
                           font-size: 16px;
                        }}
                    '''

        elif type == 'QCheckBox':
            return f'''
                        QCheckBox {{
                            spacing: 10px;
                            font-size: 14px;
                            color: {font_color0};
                            font-family: Adwaita mono;
                        }}
                        
                        QCheckBox::indicator {{
                            width: 20px;
                            height: 20px;
                        }}
                        
                        QCheckBox::indicator:unchecked {{
                            border: 2px solid {font_color0};
                            background: {themeSecondary};
                            border-radius: 4px;
                        }}
                        
                        QCheckBox::indicator:checked {{
                            border: 2px solid {font_color1};
                            border-radius: 4px;
                            background-color: {font_color0};
                        }}
                    '''