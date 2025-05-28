*1* pandas as pd
*1* matplotlib.pyplot as plt
*1* matplotlib.dates as mdates

CSV_FILE = "/home/*2*/semi_python/system_log.csv"
IMG_FILE = "/home/*2*/semi_python/system_graph.png"

def plot_graph():
    df = pd.read_csv(CSV_FILE)
    df["datetime"] = pd.to_datetime(df["datetime"])

    plt.figure(figsize=(10, 5))
    plt.plot(df["datetime"], df[*3*], label="CPU (%)", color="red")
    plt.plot(df["datetime"], df[*4*], label="Memory (%)", color="blue")
    plt.plot(df["datetime"], df[*5*], label="Disk (%)", color="green")

    plt.xlabel("Time")
    plt.ylabel("Usage (%)")
    plt.title("System Resource Usage Over Time")
    plt.legend()
    plt.tight_layout()
    plt.xticks(rotation=45)
    plt.savefig(IMG_FILE)
    plt.close()

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))

if __name__ == "__main__":
    *6*
