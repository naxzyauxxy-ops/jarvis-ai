import psutil
import gc
import chromadb

class MemoryMonitor:
    def __init__(self, threshold=75):
        self.threshold = threshold
        self.db = chromadb.PersistentClient(path="./assets/history")
    
    def check_ram(self):
        usage = psutil.virtual_memory().percent
        if usage > self.threshold:
            print(f"RAM Alert: {usage}%. Purging cache...")
            gc.collect()
            return True
        return False

    def retrieve_context(self, query):
        # Keeps context window small by only fetching relevant history
        return self.db.query(query_texts=[query], n_results=3)
