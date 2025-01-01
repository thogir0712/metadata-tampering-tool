from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from main import process_file

class RealTimeHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"New file detected: {event.src_path}")
            process_file(event.src_path)

def monitor_directory(directory_path):
    event_handler = RealTimeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=directory_path, recursive=False)
    observer.start()
    print(f"Monitoring directory: {directory_path}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
