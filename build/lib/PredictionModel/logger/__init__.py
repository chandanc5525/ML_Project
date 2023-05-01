from datetime import datetime
import logging
import os, sys   

# os - Allows us to run a command in the Python script
# sys - The python sys module provides functions and variables which are used to manipulate different parts of the Python Runtime Environment. It lets us access system-specific parameters and functions

LOG_DIR = "log"

CURRENT_TIME_STAMP = f"log{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"

# year, Month, Day, Hours, Mintue, Sec

log_file_name = f"logs{CURRENT_TIME_STAMP}.log"    # This will create log file

os.makedirs(LOG_DIR, exist_ok=True)                # This will ensure LOG_DIR is there or not if yes then this step will be skipped.

log_file_path = os.path.join(LOG_DIR, log_file_name)  # This will Define Log File 

logging.basicConfig(filename = log_file_path,        # This will be defined based on Python Documentation
                    filemode="w",
                    format = '[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO
                    )