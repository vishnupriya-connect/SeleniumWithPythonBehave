import os
import logging
from datetime import datetime


log_folder = 'logs'
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# Generate a timestamp for the log file
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Specify the path for your log file with timestamp
log_file_path = os.path.join(log_folder, f'test_logs_{timestamp}.log')

# Configure logging at the beginning of the test run
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
