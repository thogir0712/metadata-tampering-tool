import os
import json
from extract_metadata import extract_metadata
from blockchain_api import fetch_blockchain_data
from anomaly_detection import detect_anomalies, validate_file_hash
from reporting import save_report
from visualization import plot_timeline
from real_time_monitoring import monitor_directory

def process_file(file_path, transaction_map, infura_api_key, output_directory):
    metadata = extract_metadata(file_path)
    file_name = os.path.basename(file_path)

    if file_name in transaction_map:
        tx_hash = transaction_map[file_name]
        blockchain_data = fetch_blockchain_data(tx_hash, infura_api_key)
        
        anomalies = detect_anomalies(metadata, blockchain_data)
        hash_anomalies = validate_file_hash(metadata, blockchain_data)
        anomalies.extend(hash_anomalies)

        save_report(anomalies, os.path.join(output_directory, "anomaly_report.csv"))
        
        plot_timeline(metadata, blockchain_data, f"{output_directory}/{file_name}_timeline.png")
        print(f"Processed: {file_name}")
    else:
        print(f"No transaction hash found for {file_name}")

def main():
   
    with open("./config/settings.json", "r") as f:
        settings = json.load(f)

    data_directory = settings["data_directory"]
    output_directory = settings["output_directory"]
    infura_api_key = settings["infura_api_key"]

    transaction_map = {
        #"wallet.dat": "0x...transaction_hash...",
       # "invoice.pdf": "0x...another_hash...",
    }

    for file_name in os.listdir(data_directory):
        file_path = os.path.join(data_directory, file_name)
        process_file(file_path, transaction_map, infura_api_key, output_directory)


    monitor_directory(data_directory)

if __name__ == "__main__":
    main()
