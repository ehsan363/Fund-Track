from datetime import datetime, date
import random
from itertools import compress

def tdy():
    return datetime.now()

def greetingText():
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

def dateCompare(compareDate):
    year = ''
    month = ''
    day = ''
    for i in range(len(compareDate)):
        if i < 4:
            year += compareDate[i]
        elif i < 7 and compareDate[i] != '-':
            month += compareDate[i]
        elif i <=  9 and compareDate[i] != '-':
            day += compareDate[i]

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