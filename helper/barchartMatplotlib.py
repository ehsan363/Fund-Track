from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from data.database import DBmanager
import json

def initiation():
    figure = Figure()  # Blank canvas
    canvas = FigureCanvas(figure) # Convertion of canvas for Qt widget
    return figure, canvas

def plot_bar_chart(figure, canvas):
    # Theme data
    with open('data/config.json', 'r') as f:
        data = json.load(f)
        currentTheme = data['CurrentTheme']

        for i in data['Themes']:
            themeSecondary = i[currentTheme]['Secondary']

            fontConfig = i[currentTheme]['Font']

            font_color0 = fontConfig['font-color0']
            font_color1 = fontConfig['font-color1']

    # Values for the barchart
    db = DBmanager()
    income = {
        'Jan': db.incomeExpense('01', 'I'),
        'Feb': db.incomeExpense('02', 'I'),
        'Mar': db.incomeExpense('03', 'I'),
        'Apr': db.incomeExpense('04', 'I'),
        'May': db.incomeExpense('05', 'I'),
        'Jun': db.incomeExpense('06', 'I'),
        'Jul': db.incomeExpense('07', 'I'),
        'Aug': db.incomeExpense('08', 'I'),
        'Sep': db.incomeExpense('09', 'I'),
        'Oct': db.incomeExpense('10', 'I'),
        'Nov': db.incomeExpense('11', 'I'),
        'Dec': db.incomeExpense('12', 'I')
    }
    expense = {
        'Jan': db.incomeExpense('01', 'E'),
        'Feb': db.incomeExpense('02', 'E'),
        'Mar': db.incomeExpense('03', 'E'),
        'Apr': db.incomeExpense('04', 'E'),
        'May': db.incomeExpense('05', 'E'),
        'Jun': db.incomeExpense('06', 'E'),
        'Jul': db.incomeExpense('07', 'E'),
        'Aug': db.incomeExpense('08', 'E'),
        'Sep': db.incomeExpense('09', 'E'),
        'Oct': db.incomeExpense('10', 'E'),
        'Nov': db.incomeExpense('11', 'E'),
        'Dec': db.incomeExpense('12', 'E')
    }

    plt = figure.add_subplot()  # <-- Don't use during update
    plt.clear()

    plt.bar(income.keys(), income.values(), color = '#3e9c35', width = 0.8)
    plt.bar(expense.keys(), expense.values(), color = '#c71413', width = 0.8)
    plt.tick_params(axis='x', colors=font_color1)
    plt.tick_params(axis='y', colors=font_color1)

    # UI editing
    plt.get_yaxis().get_major_formatter().set_scientific(False) # Scientific notation gone
    figure.patch.set_facecolor(themeSecondary) # Bg color changed (barchart surround area)
    plt.set_facecolor(themeSecondary) # (barchart area)
    canvas.draw()
    return plt

def update_bar_chart(plt, figure, canvas):
    # Theme data
    with open('data/config.json', 'r') as f:
        data = json.load(f)
        currentTheme = data['CurrentTheme']

        for i in data['Themes']:
            themeSecondary = i[currentTheme]['Secondary']

            fontConfig = i[currentTheme]['Font']

            font_color0 = fontConfig['font-color0']
            font_color1 = fontConfig['font-color1']

    plt.clear()
    db = DBmanager()
    income = {
        'Jan': db.incomeExpense('01', 'I'),
        'Feb': db.incomeExpense('02', 'I'),
        'Mar': db.incomeExpense('03', 'I'),
        'Apr': db.incomeExpense('04', 'I'),
        'May': db.incomeExpense('05', 'I'),
        'Jun': db.incomeExpense('06', 'I'),
        'Jul': db.incomeExpense('07', 'I'),
        'Aug': db.incomeExpense('08', 'I'),
        'Sep': db.incomeExpense('09', 'I'),
        'Oct': db.incomeExpense('10', 'I'),
        'Nov': db.incomeExpense('11', 'I'),
        'Dec': db.incomeExpense('12', 'I')
    }
    expense = {
        'Jan': db.incomeExpense('01', 'E'),
        'Feb': db.incomeExpense('02', 'E'),
        'Mar': db.incomeExpense('03', 'E'),
        'Apr': db.incomeExpense('04', 'E'),
        'May': db.incomeExpense('05', 'E'),
        'Jun': db.incomeExpense('06', 'E'),
        'Jul': db.incomeExpense('07', 'E'),
        'Aug': db.incomeExpense('08', 'E'),
        'Sep': db.incomeExpense('09', 'E'),
        'Oct': db.incomeExpense('10', 'E'),
        'Nov': db.incomeExpense('11', 'E'),
        'Dec': db.incomeExpense('12', 'E')
    }
    plt.bar(income.keys(), income.values(), color='#3e9c35', width=0.8)
    plt.bar(expense.keys(), expense.values(), color='#c71413', width=0.8)
    plt.tick_params(axis='x', colors=font_color1)
    plt.tick_params(axis='y', colors=font_color1)

    # UI editing
    plt.get_yaxis().get_major_formatter().set_scientific(False)  # Scientific notation gone
    figure.patch.set_facecolor(themeSecondary)  # Bg color changed (barchart surround area)
    plt.set_facecolor(themeSecondary)  # (barchart area)
    canvas.draw_idle()