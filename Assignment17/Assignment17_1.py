import schedule
import time


def greeting():
    print("Jay Ganesh ....")

schedule.every(2).seconds.do(greeting)



while True:
    schedule.run_pending()
    time.sleep(1)