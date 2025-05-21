import psutil
import datetime
import csv
import os

CSV_FILE = "/home/hogehoge/system_log.csv"

def collect_data():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["datetime", "cpu", "memory", "disk"])
        writer.writerow([now, cpu, mem, disk])

if __name__ == "__main__":
    collect_data()
