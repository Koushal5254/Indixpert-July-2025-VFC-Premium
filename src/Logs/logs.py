import os
from datetime import datetime

BASE_PATH = os.getcwd()
LOG_FILE = os.path.join(BASE_PATH, "Logs", "activity.log")

# Ensure log folder exists
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

class Logger:
    @staticmethod
    def write_log(action, actor="system", details=""):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] [{actor.upper()}] {action} — {details}\n"

        try:
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(log_entry)
        except Exception as e:
            print(f"⚠️ Failed to write log: {e}")
