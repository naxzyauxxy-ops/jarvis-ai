import psutil
import time
import threading

class MemoryMonitor(threading.Thread):
    def __init__(self, threshold=75):
        super().__init__()
        self.threshold = threshold
        self.daemon = True

    def run(self):
        while True:
            memory = psutil.virtual_memory()
            if memory.percent > self.threshold:
                print(f"[Memory] Usage at {memory.percent}%. Optimizing...")
                # Logic to clear cache or alert user would go here
            time.sleep(60) # Check every minute
