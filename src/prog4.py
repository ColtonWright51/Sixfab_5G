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

    modem_helper.automate_test_read(ser, file, "CIMI")
    modem_helper.automate_test_read(ser, file, "CLCK", 5)
    modem_helper.automate_test_read(ser, file, "CPIN", 5)
    modem_helper.automate_test_read(ser, file, "CPWD", 5)
    modem_helper.automate_test_read(ser, file, "CSIM")
    modem_helper.automate_test_read(ser, file, "CRSM")
    modem_helper.automate_test_read(ser, file, "CCHO")
    modem_helper.automate_test_read(ser, file, "CCHC")
    modem_helper.automate_test_read(ser, file, "CGLA")
    modem_helper.automate_test_read(ser, file, "QPINC")
    modem_helper.automate_test_read(ser, file, "QINSTAT")
    modem_helper.automate_test_read(ser, file, "QSIMDET")
    modem_helper.automate_test_read(ser, file, "QSIMSTAT")
    modem_helper.automate_test_read(ser, file, "QUIMSLOT")
    