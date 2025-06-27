import datetime
import schedule
import time

def date_time():
    current = datetime.datetime.now()
    print("current date and time : ",current.strftime("%y-%m-%d %H:%M:%S"))



schedule.every(1).minutes.do(date_time)

while True:
    schedule.run_pending()
    time.sleep(1)