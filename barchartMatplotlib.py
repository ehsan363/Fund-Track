from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from data.database import DBmanager

def initiation():
    figure = Figure()  # Blank canvas
    canvas = FigureCanvas(figure) # Convertion of canvas for Qt widget
    return figure, canvas

def plot_bar_chart(figure, canvas):
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
    plt.tick_params(axis='x', colors='white')
    plt.tick_params(axis='y', colors='white')

    # UI editing
    plt.get_yaxis().get_major_formatter().set_scientific(False) # Scientific notation gone
    figure.patch.set_facecolor("#222222") # Bg color changed (barchart surround area)
    plt.set_facecolor("#222222") # (barchart area)
    canvas.draw()