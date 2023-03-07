import logging # log all info about execution and exceptions
import os
from datetime import datetime



LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # Create a log file with this name
logs_folder_path  = os.path.join(os.getcwd(),"logs", LOG_FILE)  # path for the log file
os.makedirs(logs_folder_path, exist_ok=True)  # even if it exists already, overwrite


LOG_FILE_PATH = os.path.join(logs_folder_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO, 
    format="[%(asctime)s] {%(pathname)s:%(lineno)d}] %(levelname)s - %(message)s"
    )

