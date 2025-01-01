import csv

def save_report(anomalies, output_file):
    with open(output_file, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["File", "Issue", "Blockchain Timestamp"])
        writer.writeheader()
        writer.writerows(anomalies)
    print(f"Report saved to {output_file}")
