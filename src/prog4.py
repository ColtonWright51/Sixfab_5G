"""
Created by Colton Wright on 1/4/2023
Communicates to the Quectel RM502Q-AE modem through a serial port. The modem
uses the standard "Hayes command set" popular with modems. Attempt 
initialize the (U)SIM card in the modem.

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


    ser.write(b"AT+COPS=?\r")
    time.sleep(180)
    file.write(ser.read(100))
    file.write(ser.read(100))
    file.write(ser.read(100))
    file.write(ser.read(100))


    # MT returns an alphanumeric string indicating whether or not a password
    # is required.
    ser.write(b"AT+CPIN?\r")
    time.sleep(.3)
    file.write(ser.read(100))

    # ser.write(b"AT+CNUM?\r")
    # time.sleep(.3)
    # file.write(ser.read(100))

    # ser.write(b"AT+COPS?\r")
    # time.sleep(.3)
    # file.write(ser.read(100))

    # ser.write(b"AT+CPIN?\r")
    # time.sleep(.3)
    # file.write(ser.read(100))

    # ser.write(b"AT+CPIN?\r")
    # time.sleep(.3)
    # file.write(ser.read(100))