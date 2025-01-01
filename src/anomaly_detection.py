def detect_anomalies(file_metadata, blockchain_data):
    anomalies = []
    if file_metadata["Created"] > blockchain_data["Timestamp"]:
        anomalies.append({
            "File": file_metadata["File"],
            "Issue": "File created after blockchain transaction",
            "Blockchain Timestamp": blockchain_data["Timestamp"]
        })
    return anomalies

def validate_file_hash(file_metadata, blockchain_data):
    anomalies = []
    
    if file_metadata.get("Hash (SHA256)") != blockchain_data.get("File Hash (SHA256)"):
        anomalies.append({
            "File": file_metadata["File"],
            "Issue": "File hash mismatch",
            "Blockchain Hash": blockchain_data.get("File Hash (SHA256)"),
        })
    
    return anomalies

