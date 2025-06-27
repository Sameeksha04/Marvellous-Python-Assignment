import schedule
import time


def greeting():
    print("Namskar..")

schedule.every().day.at("09:00").do(greeting)

print("Schedular started and every day at 09:aa AM daily to say namaskar...")

while True:
    schedule.run_pending()
    time.sleep(1)