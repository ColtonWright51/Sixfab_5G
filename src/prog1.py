"""
Communicates to the Quectel RM502Q-AE modem through a serial port. The modem
uses the standard "Hayes command set" popular with modems.

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
    ser.write(b"AT&F0")
    file.write(ser.read(100))
    time.sleep(.3)

    # Set command echo mode
    ser.write(b"ATE1\r")
    file.write(ser.read(100))
    time.sleep(.3)


    # Display MT identification information
    ser.write(b"ATI\r")
    file.write(ser.read(100))
    time.sleep(.3)

    # Request manufacturer identification
    ser.write(b"AT+GMI\r")
    file.write(ser.read(100))
    time.sleep(.3)

    # Request model identification
    ser.write(b"AT+GMM\r")
    file.write(ser.read(100))
    time.sleep(.3)

    # Request international mobile equipment identity
    ser.write(b"AT+GSN\r")
    file.write(ser.read(100))
    time.sleep(.3)

    # Display current configuration
    ser.write(b"AT&V\r")
    file.write(ser.read(100))
    file.write(ser.read(100))
    time.sleep(.3)

    # Test command extended config settings
    ser.write(b"AT+QCFG=?\r")
    file.write(ser.read(100))
    file.write(ser.read(100))
    file.write(ser.read(100))
    file.write(ser.read(100))
    file.write(ser.read(100))
    file.write(ser.read(100))
    file.write(ser.read(100))
    time.sleep(.3)

    # Test command Request International Mobile Subscriber Identity (IMSI)
    ser.write(b"AT+CIMI=?\r")
    file.write(ser.read(100))
    time.sleep(.3)

    # Request International Mobile Subscriber Identity (IMSI)
    ser.write(b"AT+CIMI\r")
    file.write(ser.read(100))
    time.sleep(.3)

