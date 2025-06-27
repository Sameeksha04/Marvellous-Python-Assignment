import schedule
import time
import shutil
from datetime import datetime

source_file = "important_data.txt"
backup_file = "backup/important_data_backup.txt"
log_file = "backup_log.txt"

def backup_file():
    try:
        shutil.copy2(source_file, backup_file)

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_file, "a") as log:
            log.write(f"[{now}] Backup completed successfully.\n")

        print(f"Backup completed at {now}")

    except Exception as e:
        with open(log_file, "a") as log:
            log.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Backup failed: {str(e)}\n")
        print(f"Backup failed: {str(e)}")

schedule.every().hour.do(backup_file)

print("Hourly backup is started....")

while True:
    schedule.run_pending()
    time.sleep(1)
