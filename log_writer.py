import psutil     # リソースの情報を取得するためのライブラリ
import datetime   # 現在時刻取得に使用するライブラリ
import csv        # csvファイルのデータを読み書きするためのライブラリ
import os         # ファイル操作に関するライブラリ

# データを格納するcsvファイル(system_log.csv)のパスを定義
CSV_FILE = "/home/[①自分のユーザ名]/semi_python/system_log.csv"

# 使用しているリソースのデータを取得しcsvファイルに記述する関数を定義
[②] collect_data():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # 現在時刻の取得
    cpu = psutil.cpu_percent(interval=1)                        # CPU使用率の取得
    mem = psutil.virtual_memory().percent                       # メモリ使用率の取得
    disk = psutil.disk_usage('/').percent                       # ディスク使用率の取得

    # csvファイルが存在すれば1,そうでなければ0
    file_exists = os.path.isfile([③])
                                 
    # csvファイルを開いてデータの書き込み
    with open([④], mode='a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:  # パスにファイルが無かった場合、最初にヘッダ追加
            writer.writerow(["datetime", "cpu", "memory", "disk"])
        writer.writerow([⑤■■,■■,■■,■■])

# ファイルが直接実行された場合にのみ、collect_data関数を実行
if __name__ == "__main__":
    [⑥関数の実行]