"""Provides NumberList and FrequencyDistribution, classes for statistics.

NumberList holds a sequence of numbers, and defines several statistical
operations (mean, stdev, etc.) FrequencyDistribution holds a mapping from
items (not necessarily numbers) to counts, and defines operations such as
Shannon entropy and frequency normalization.
"""

"""


"""

import serial
import os
import datetime

now = datetime.datetime.today()
now = now.strftime("%Y-%m-%d")
data_path = os.path.join("data", now+"_data")
os.makedirs(data_path, exist_ok=True)
now = datetime.datetime.today()
now = now.strftime("%Y-%m-%dT%H%M%S")
log_file_path = os.path.join(data_path, now+"_log")

with serial.Serial('/dev/ttyUSB3', baudrate=115200, timeout=1) as ser, \
    open(log_file_path, 'w') as file:
    
    ser.write(b"AT")
    read1 = ser.read(30)
    file.write(read1.decode())