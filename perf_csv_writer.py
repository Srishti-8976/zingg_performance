import csv
import os
from datetime import datetime


def write_perf_csv(test_name, results, output_dir="perf_reports"):
    

    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H-%M-%S")
    year = now.strftime("%Y")

    # Create directory: perf_reports/<test_name>/<year>/
    test_dir = os.path.join(output_dir, test_name, year)
    os.makedirs(test_dir, exist_ok=True)

    # CSV filename
    filename = f"{test_name}_{date_str}_{time_str}.csv"
    filepath = os.path.join(test_dir, filename)

    # Base columns
    headers = ["date", "time", "test"]

    # Dynamic phase columns (sorted for consistency)
    phase_names = sorted(results.keys())
    headers.extend(phase_names)

    # Row values
    row = [date_str, time_str, test_name]
    for phase in phase_names:
        row.append(results.get(phase))

    # Write CSV
    with open(filepath, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerow(row)

    return filepath
