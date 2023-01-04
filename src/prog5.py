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

start_time = time.time()


with serial.Serial('/dev/ttyUSB3', baudrate=115200, timeout=1) as ser, \
    open(log_file_path, 'ab') as file:


    # All commands must start with AT or at and end with carriage return!

    # Section 2 General Commands    
    modem_helper.automate_test_read(ser, file, "ATI", is_read_com=False)

\

    # This will give errors if command does not exist. Just will have
    # another error in the text file, it's fine.
    # modem_helper.automate_test_read(ser, file, "AT+GMI")
    # modem_helper.automate_test_read(ser, file, "AT+GMM")
    # modem_helper.automate_test_read(ser, file, "AT+GMR")
    # modem_helper.automate_test_read(ser, file, "AT+CGMI")
    # modem_helper.automate_test_read(ser, file, "AT+CGMM")
    # modem_helper.automate_test_read(ser, file, "AT+CGMR")
    # modem_helper.automate_test_read(ser, file, "AT+GSN")
    # modem_helper.automate_test_read(ser, file, "AT+CGSN")
    # # modem_helper.automate_test_read(ser, file, "AT&F")
    # modem_helper.automate_test_read(ser, file, "AT&V")
    # # modem_helper.automate_test_read(ser, file, "AT&W")
    # # modem_helper.automate_test_read(ser, file, "ATZ")
    # modem_helper.automate_test_read(ser, file, "ATQ")
    # modem_helper.automate_test_read(ser, file, "ATV")
    # modem_helper.automate_test_read(ser, file, "ATE")
    # # modem_helper.automate_test_read(ser, file, "A/")
    # # modem_helper.automate_test_read(ser, file, "ATS3")
    # # modem_helper.automate_test_read(ser, file, "ATS4")
    # # modem_helper.automate_test_read(ser, file, "ATS5")
    # # modem_helper.automate_test_read(ser, file, "ATX")
    # modem_helper.automate_test_read(ser, file, "AT+CFUN", t_sleep=15)
    # modem_helper.automate_test_read(ser, file, "AT+CMEE")
    # modem_helper.automate_test_read(ser, file, "AT+CSCS")
    # modem_helper.automate_test_read(ser, file, "AT+QURCCFG")
    # modem_helper.automate_test_read(ser, file, "AT+QMBNCFG")



print("Runtime: " + str(time.time()-start_time))