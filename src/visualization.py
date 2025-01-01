import matplotlib.pyplot as plt

def plot_timeline(file_metadata, blockchain_data, output_file="timeline.png"):
    labels = ["Created", "Modified", "Accessed", "Blockchain"]
    timestamps = [
        file_metadata["Created"],
        file_metadata["Modified"],
        file_metadata["Accessed"],
        blockchain_data["Timestamp"],
    ]
    
    plt.figure(figsize=(10, 6))
    plt.scatter(timestamps, [1, 2, 3, 4], color="blue")
    plt.yticks([1, 2, 3, 4], labels)
    plt.xlabel("Timestamps")
    plt.title(f"Timeline for {file_metadata['File']}")
    plt.grid(True)
    plt.savefig(output_file)
    plt.close()
    print(f"Timeline saved to {output_file}")
