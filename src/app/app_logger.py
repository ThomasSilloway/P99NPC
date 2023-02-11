import os
import glob
import logging
from datetime import datetime
import shutil


class AppLogger:
    def __init__(self):
        self.folder = ".\\logs"

    def configure(self):
        # Get the current time
        now = datetime.now()

        # Format the timestamp
        timestamp = now.strftime("%Y-%m-%d--%H-%M-%S")

        log_file_name = f"{self.folder}\\npc.log"

        # Copy the npc.log file to log_timestamp.log
        if os.path.exists(log_file_name):
            shutil.move(log_file_name, f"{self.folder}\\log_{timestamp}.log")

        # Remove previous logs
        log_files = sorted(glob.glob(os.path.join(self.folder, "*log_*.log")), key=lambda x: os.path.getctime(x))

        # Remove all but the last 10 log files
        for log_file in log_files[:-10]:
            os.remove(log_file)

        # Configure the logging
        logging.basicConfig(filename=log_file_name, level=logging.DEBUG,
                            format="%(asctime)s [%(threadName)s] %(levelname)s: %(message)s", datefmt="%M:%S")

        # Add a handler to write log messages to the console
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(levelname)s: %(message)s")
        console.setFormatter(formatter)
        logging.getLogger().addHandler(console)
