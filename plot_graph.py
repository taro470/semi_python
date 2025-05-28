import pandas as pd                # ライブラリのインポート
import matplotlib.pyplot as plt    # ライブラリのインポート
import matplotlib.dates as mdates

CSV_FILE = "/home/ryutaro/semi_python/system_log.csv"
IMG_FILE = "/home/ryutaro/semi_python/system_graph.png"

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

    # x軸を秒を除いたフォーマットに設定
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))

if __name__ == "__main__":
    plot_graph()
