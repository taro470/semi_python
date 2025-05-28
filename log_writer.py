import psutil     
import datetime   
import csv        
import os         

CSV_FILE = "/home/*1*/semi_python/system_log.csv"

*2* collect_data():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    cpu = psutil.cpu_percent(interval=1)                        
    mem = psutil.virtual_memory().percent                       
    disk = psutil.disk_usage('/').percent                       

    file_exists = os.path.isfile(*3*)
                                 
    with open(*4*, mode='a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:  
            writer.writerow(["datetime", "cpu", "memory", "disk"])
        writer.writerow([*5*])

if __name__ == "__main__":
    *6*