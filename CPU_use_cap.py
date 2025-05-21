import psutil
import datetime
import csv
import os
import pandas as pd
import matplotlib.pyplot as plt

CSV_FILE = "/home/ryutaro/system_log.csv"
IMG_FILE = "/home/ryutaro/system_graph.png"

def collect_data():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    # ファイルが存在しない場合、ヘッダーを追加
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["datetime", "cpu", "memory", "disk"])
        writer.writerow([now, cpu, mem, disk])

def plot_graph():
    df = pd.read_csv(CSV_FILE)
    df["datetime"] = pd.to_datetime(df["datetime"])

    plt.figure(figsize=(10, 5))
    plt.plot(df["datetime"], df["cpu"], label="CPU (%)", color="red")
    plt.plot(df["datetime"], df["memory"], label="Memory (%)", color="blue")
    plt.plot(df["datetime"], df["disk"], label="Disk (%)", color="green")

    plt.xlabel("Time")
    plt.ylabel("Usage (%)")
    plt.title("System Resource Usage Over Time")
    plt.legend()
    plt.tight_layout()
    plt.xticks(rotation=45)
    plt.savefig(IMG_FILE)
    plt.close()

if __name__ == "__main__":
    collect_data()
    plot_graph()
