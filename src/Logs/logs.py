import os
from datetime import datetime

BASE_PATH = os.getcwd()
LOG_DIR = os.path.join(BASE_PATH, "Logs")
LOG_FILE = os.path.join(LOG_DIR, "activity.log")

class Logger:
    @staticmethod
    def write_log(action, actor="system", details=""):
        if not os.path.exists(LOG_DIR):
            os.makedirs(LOG_DIR)

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        entry = f"[{timestamp}] [{actor.upper()}] {action} - {details}\n"

        try:
            with open(LOG_FILE, "a") as f:
                f.write(entry)
        except Exception as e:
            print(f" Failed to write log: {e}")

    @staticmethod
    def view_logs(limit=10):
        try:
            with open(LOG_FILE, "r") as f:
                lines = f.readlines()
                print("\n Recent Logs:")
                for line in lines[-limit:]:
                    print(line.strip())
        except FileNotFoundError:
            print(" No logs found.")
