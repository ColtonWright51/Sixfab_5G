"""
Created by Colton Wright on 1/4/2023
Communicates to the Quectel RM502Q-AE modem through a serial port. The modem
uses the standard "Hayes command set" popular with modems. Attempt to read
some broadband data through the modem without actually connecting to a tower.
This is done with the "Network Service Commands" given in the modem's
documentation.

https://en.wikipedia.org/wiki/Hayes_command_set

"""

import serial
import os
import datetime
import modules.modem_helper as modem_helper
import time

# Setup data directory & file name to save responses from modem
log_file_path = modem_helper.make_data_file()

time_to_read = .1
time_to_end = datetime.datetime.today().timestamp() + 60*time_to_read

with serial.Serial('/dev/ttyUSB3', baudrate=115200, timeout=1) as ser, \
    open(log_file_path, 'ab') as file:
    

    # All commands must start with AT or at and end with carriage return!

    # Reset AT command settings to factory settings
    ser.write(b"AT&F0\r")
    time.sleep(.3)
    file.write(ser.read(100))
