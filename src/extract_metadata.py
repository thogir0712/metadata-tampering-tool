import os
from datetime import datetime
import hashlib

def extract_metadata(file_path):
    stat = os.stat(file_path)
    return {
        "File": file_path,
        "Size (Bytes)": stat.st_size,
        "Created": datetime.fromtimestamp(stat.st_ctime),
        "Modified": datetime.fromtimestamp(stat.st_mtime),
        "Accessed": datetime.fromtimestamp(stat.st_atime),
    }


def calculate_file_hash(file_path, algorithm="sha256"):
    hash_func = hashlib.new(algorithm)
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def extract_metadata(file_path):
    stat = os.stat(file_path)
    return {
        "File": file_path,
        "Size (Bytes)": stat.st_size,
        "Created": datetime.fromtimestamp(stat.st_ctime),
        "Modified": datetime.fromtimestamp(stat.st_mtime),
        "Accessed": datetime.fromtimestamp(stat.st_atime),
        "Hash (SHA256)": calculate_file_hash(file_path),
    }
