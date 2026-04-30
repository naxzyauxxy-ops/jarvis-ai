import psutil
import gc
import time
import threading

class MemoryMonitor:
    def __init__(self, threshold=75):
        self.threshold = threshold
        self.running = True

    def start(self):
        thread = threading.Thread(target=self._monitor, daemon=True)
        thread.start()

    def _monitor(self):
        while self.running:
            usage = psutil.virtual_memory().percent
            if usage > self.threshold:
                gc.collect()
            time.sleep(30) # Check every 30s
