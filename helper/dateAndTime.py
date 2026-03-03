# Importing Modules
from datetime import datetime, date
import random

def tdy():
    '''
    Function to get the current date and time.
    '''
    return datetime.now()

def greetingText():
    '''
    Function to generate the greeting text according to the time of opening or refreshing the homepage.
    '''
    time = datetime.now()
    hour = time.hour

    if 5 <= hour < 12:
        return 'Good Morning'
    elif 12 <= hour < 17:
        return 'Good Afternoon'
    elif 17 <= hour < 21:
        return 'Good Evening'
    else:
        nightgreets = ["Night shift mode: ON","After hours finance check" ,"The numbers never sleep.", "Welcome back"]
        randomgreeting = random.choice(nightgreets)
        return randomgreeting

def dateExtraction(dateToE):
    '''
    Function to extract the year and month and day from the given date.
    '''
    year = ''
    month = ''
    day = ''
    for i in range(len(dateToE)):
        if i < 4:
            year += dateToE[i]
        elif i < 7 and dateToE[i] != '-':
            month += dateToE[i]
        elif i <=  9 and dateToE[i] != '-':
            day += dateToE[i]
    return year, month, day

def dateCompare(compareDate):
    '''
    Function to compare the given date to current date and return string accordingly.
    '''
    year, month, day = dateExtraction(compareDate)
    today = date.today()
    diffInDays = (date.today() - date(int(year), int(month), int(day))).days
    if diffInDays == 0:
        return 'Today'
    elif diffInDays == 1:
        return 'Yesturday'
    elif diffInDays < 6:
        return f'{diffInDays} days ago'
    else:
        return f'{day}/{month}/{year}'

def todayDate():
    '''
    Function that returns current date.
    '''
    tdyDate = date.today()
    return tdyDate

def dateFormat(ch):
    '''
    Function to format the given date from dd-mm-yyyy to yyyy-mm-dd.
    '''
    dt = datetime.strptime(ch, "%d-%m-%Y")

    # Re-format datetime → string
    new_date = dt.strftime("20%y-%m-%d")
    return new_date

def NdateToFormattedDate(newDate):
    '''
    Function to reformat the date from dd-mm-yyyy to yyyy-mm-dd and a string type
    '''
    formatted_date = datetime.strptime(newDate, "%d-%m-%Y").strftime("%Y-%m-%d")
    return formatted_date

def reportDateCompare(lastDate):
    '''
    Function to compare the date at which the last report was made and the current date to make the decision on if we have to make a new report.
    '''
    currentDate = todayDate().strftime('%Y-%m')
    year1 = lastDate[0:4]
    year2 = currentDate[0:4]

    month1 = lastDate[5:7]
    month2 = currentDate[5:7]
    if int(year1) < int(year2) or int(month1) < int(month2):
        return 'Outdated', year2, month2
    else:
        return 'Uptodate', year2, month2