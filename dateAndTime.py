from datetime import datetime
import random

def tdy():
    return datetime.today()

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