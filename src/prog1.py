"""
Communicates to the Quectel RM502Q-AE modem through a serial port. The modem
uses the standard "Hayes command set" popular with modems.

https://en.wikipedia.org/wiki/Hayes_command_set

"""

import serial
import os
import datetime
import modules.modem_helper as modem_helper

# Setup data directory & file name to save responses from modem
log_file_path = modem_helper.make_data_file()

time_to_read = .1
time_to_end = datetime.datetime.today().timestamp() + 60*time_to_read

with serial.Serial('/dev/ttyUSB3', baudrate=115200, timeout=1) as ser, \
    open(log_file_path, 'ab') as file:
    
    # All commands must start with AT or at and end with carriage return!
    ser.write(b"ATE1\r")
    file.write(ser.read(100))
    ser.write(b"ATI\r")
    file.write(ser.read(100))
    ser.write(b"AT+GMI\r")
    file.write(ser.read(100))
    ser.write(b"AT+GMM\r")
    file.write(ser.read(100))
    ser.write(b"AT+GSN\r")
    file.write(ser.read(100))
    ser.write(b"AT+CGSN\r")
    file.write(ser.read(100))
    ser.write(b"AT&V\r")
    file.write(ser.read(150))
    # while datetime.datetime.today().timestamp() < time_to_end:
        # file.write(ser.read(100))
