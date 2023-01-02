"""
Created by Colton Wright on 12/21/2022
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
    ser.write(b"AT&F0\r")
    time.sleep(.3)
    file.write(ser.read(100))

    # Set command echo mode
    ser.write(b"ATE1\r")
    time.sleep(.3)
    file.write(ser.read(100))

    # Display MT identification information
    ser.write(b"ATI\r")
    time.sleep(.3)
    file.write(ser.read(100))

    # Request manufacturer identification
    ser.write(b"AT+GMI\r")
    time.sleep(.3)
    file.write(ser.read(100))

    # Request model identification
    ser.write(b"AT+GMM\r")
    time.sleep(.3)
    file.write(ser.read(100))

    # Request international mobile equipment identity
    ser.write(b"AT+GSN\r")
    time.sleep(.3)
    file.write(ser.read(100))

    # Display current configuration
    ser.write(b"AT&V\r")
    time.sleep(.3)
    file.write(ser.read(100))
    file.write(ser.read(100))

    # Test command extended config settings
    ser.write(b"AT+QCFG=?\r")
    time.sleep(.3)
    file.write(ser.read(100))
    file.write(ser.read(100))
    file.write(ser.read(100))
    file.write(ser.read(100))
    file.write(ser.read(100))
    file.write(ser.read(100))
    file.write(ser.read(100))

    # Test command Request International Mobile Subscriber Identity (IMSI)
    ser.write(b"AT+CIMI=?\r")
    time.sleep(.3)
    file.write(ser.read(100))

    # Query for (U)SIM card status report
    ser.write(b"AT+QSIMSTAT?\r")
    time.sleep(.3)
    file.write(ser.read(100))

    # Enable (U)SIM card detection
    ser.write(b"AT+QSIMDET=1,0\r")
    time.sleep(.3)
    file.write(ser.read(100))

    # Enable (U)SIM card insertion status report
    ser.write(b"AT+QSIMSTAT=0\r")
    time.sleep(.3)
    file.write(ser.read(100))

    # Query for (U)SIM card status report
    ser.write(b"AT+QSIMSTAT?\r")
    time.sleep(.3)
    file.write(ser.read(100))

    # 
    ser.write(b"AT+QUIMSLOT=?\r")
    time.sleep(.3)
    file.write(ser.read(100))

    ser.write(b"AT+QUIMSLOT?\r")
    time.sleep(.3)
    file.write(ser.read(100))

    ser.write(b"AT+QUIMSLOT=2\r")
    time.sleep(.3)
    file.write(ser.read(100))

    # Query for (U)SIM card status report
    ser.write(b"AT+QSIMSTAT?\r")
    time.sleep(.3)
    file.write(ser.read(100))

    #Reset
    ser.write(b"AT+CFUN=1,1")
    time.sleep(15)
    file.write(ser.read(100))

    # Enable (U)SIM card detection
    ser.write(b"AT+QSIMDET=1,0\r")
    time.sleep(.3)
    file.write(ser.read(100))

    # Query for (U)SIM card status report
    ser.write(b"AT+QSIMSTAT?\r")
    time.sleep(.3)
    file.write(ser.read(100))

    # Enable (U)SIM card detection
    ser.write(b"AT+QSIMDET=?\r")
    time.sleep(.3)
    file.write(ser.read(100))

    # 
    ser.write(b"AT+CPIN?\r")
    time.sleep(.3)
    file.write(ser.read(100))

    # 
    ser.write(b"AT+CPIN?\r")
    time.sleep(.3)
    file.write(ser.read(100))

    # 
    ser.write(b"AT+CPIN=1234\r")
    time.sleep(.3)
    file.write(ser.read(100))


















