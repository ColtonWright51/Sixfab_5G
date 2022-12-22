import os
import datetime


def make_data_file():
    now = datetime.datetime.today()
    now = now.strftime("%Y-%m-%d")
    data_path = os.path.join("data", now+"_data")
    os.makedirs(data_path, exist_ok=True)
    now = datetime.datetime.today()
    now = now.strftime("%Y-%m-%dT%H%M%S")
    log_file_path = os.path.join(data_path, now+"_log")
    return(log_file_path)
