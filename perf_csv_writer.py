import csv
from datetime import datetime
import os

def write_perf_csv(test_name, train_time, match_time, output_dir="perf_reports"):
    

    os.makedirs(output_dir, exist_ok=True)

    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H-%M-%S")

    filename = f"{test_name}_{date}_{time}.csv"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "time", "test", "train", "match"])
        writer.writerow([date, time, test_name, train_time, match_time])

    return filepath
