import schedule
import time

def Lunch_reminder():
    print("Lunch time..")


def wrap_time():
    print("wrap up work")


schedule.every().day.at("13:00").do(Lunch_reminder)
schedule.every().day.at("18:00").do(wrap_time)

print("Scheduler started . tasks will get performed simultaneously at 1 pm and 6 pm...")

while True:
    schedule.run_pending()
    time.sleep(1)