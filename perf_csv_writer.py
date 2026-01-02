
import csv
import os
from datetime import datetime


def write_perf_csv(test_name, results, output_dir="perf_reports"):
    """
    Writes a timestamped CSV performance report.

    - Generic: supports any number of phases dynamically
    - Folder structure: perf_reports/<test_name>/<year>/
    - Does NOT overwrite previous reports
    """

    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H-%M-%S")
    year = now.strftime("%Y")

    # Create directory structure
    test_dir = os.path.join(output_dir, test_name, year)
    os.makedirs(test_dir, exist_ok=True)

    # CSV filename
    filename = f"{test_name}_{date_str}_{time_str}.csv"
    filepath = os.path.join(test_dir, filename)

    # Base headers
    headers = ["date", "time", "test"]

    # Dynamic phase headers
    phase_names = sorted(results.keys())
    headers.extend(phase_names)

    # CSV row
    row = [date_str, time_str, test_name]
    for phase in phase_names:
        row.append(results.get(phase))

    # Write CSV
    with open(filepath, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerow(row)

    return filepath
