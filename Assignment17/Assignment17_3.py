import schedule
import time

def remainder_coding():
    print("Do Coding...")


schedule.every(30).minutes.do(remainder_coding)


print("Scheduler is started..")

while True:
    schedule.run_pending()
    time.sleep(1)

