import schedule
import time
from datetime import datetime


def write_Time():
    current = datetime.now()
    with open("Marvellous.txt","a")as file:
        file.write("Current Time: "+current.strftime("%Y-%m-%d %H:%M:%S") + "\n")
    
    print("Time written to marvellous.txt")


schedule.every(5).minutes.do(write_Time)

print("scheduler started . writing time to marvellous.txt every 5 minutes..")


while True:
    schedule.run_pending()
    time.sleep(1)
