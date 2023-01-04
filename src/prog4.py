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
    modem_helper.automate_test_read(ser, file, "ATI")
    modem_helper.automate_test_read(ser, file, "AT+GMI")
    modem_helper.automate_test_read(ser, file, "AT+GMM")
    modem_helper.automate_test_read(ser, file, "AT+GMR")
    modem_helper.automate_test_read(ser, file, "AT+CGMI")
    modem_helper.automate_test_read(ser, file, "AT+CGMM")
    modem_helper.automate_test_read(ser, file, "AT+CGMR")
    modem_helper.automate_test_read(ser, file, "AT+GSN")
    modem_helper.automate_test_read(ser, file, "AT+CGSN")
    # modem_helper.automate_test_read(ser, file, "AT&F")
    modem_helper.automate_test_read(ser, file, "AT&V")
    # modem_helper.automate_test_read(ser, file, "AT&W")
    # modem_helper.automate_test_read(ser, file, "ATZ")
    modem_helper.automate_test_read(ser, file, "ATQ")
    modem_helper.automate_test_read(ser, file, "ATV")
    modem_helper.automate_test_read(ser, file, "ATE")
    # modem_helper.automate_test_read(ser, file, "A/")
    # modem_helper.automate_test_read(ser, file, "ATS3")
    # modem_helper.automate_test_read(ser, file, "ATS4")
    # modem_helper.automate_test_read(ser, file, "ATS5")
    # modem_helper.automate_test_read(ser, file, "ATX")
    modem_helper.automate_test_read(ser, file, "AT+CFUN", True, 15)
    modem_helper.automate_test_read(ser, file, "AT+CMEE")
    modem_helper.automate_test_read(ser, file, "AT+CSCS")
    modem_helper.automate_test_read(ser, file, "AT+QURCCFG")
    modem_helper.automate_test_read(ser, file, "AT+QMBNCFG")



    # Section 3 Status Control Commands
    modem_helper.automate_test_read(ser, file, "AT+CPAS")
    modem_helper.automate_test_read(ser, file, "AT+CEER")
    modem_helper.automate_test_read(ser, file, "AT+QCFG")
    modem_helper.automate_test_read(ser, file, "AT+QINDCFG")





    # Section 4 (U)SIM Related Commands
    modem_helper.automate_test_read(ser, file, "AT+CIMI")
    modem_helper.automate_test_read(ser, file, "AT+CLCK", t_sleep=5)
    modem_helper.automate_test_read(ser, file, "AT+CPIN", t_sleep=5)
    modem_helper.automate_test_read(ser, file, "AT+CPWD", t_sleep=5)
    modem_helper.automate_test_read(ser, file, "AT+CSIM")
    modem_helper.automate_test_read(ser, file, "AT+CRSM")
    modem_helper.automate_test_read(ser, file, "AT+CCHO")
    modem_helper.automate_test_read(ser, file, "AT+CCHC")
    modem_helper.automate_test_read(ser, file, "AT+CGLA")
    modem_helper.automate_test_read(ser, file, "AT+QPINC")
    modem_helper.automate_test_read(ser, file, "AT+QINSTAT")
    modem_helper.automate_test_read(ser, file, "AT+QSIMDET")
    modem_helper.automate_test_read(ser, file, "AT+QSIMSTAT")
    modem_helper.automate_test_read(ser, file, "AT+QUIMSLOT")





    # Section 5 Network Service Commands
    modem_helper.automate_test_read(ser, file, "AT+COPS", True, t_sleep = 180)
    modem_helper.automate_test_read(ser, file, "AT+CREG")
    modem_helper.automate_test_read(ser, file, "AT+CGREG")
    modem_helper.automate_test_read(ser, file, "AT+CEREG")
    modem_helper.automate_test_read(ser, file, "AT+C5GREG")
    modem_helper.automate_test_read(ser, file, "AT+CGDCONT")
    modem_helper.automate_test_read(ser, file, "AT+C5GNSSAI")
    modem_helper.automate_test_read(ser, file, "AT+C5GNSSAIRDP")
    modem_helper.automate_test_read(ser, file, "AT+CSQ")
    modem_helper.automate_test_read(ser, file, "AT+QRSRP")
    modem_helper.automate_test_read(ser, file, "AT+QRSRQ")
    modem_helper.automate_test_read(ser, file, "AT+QSINR")
    modem_helper.automate_test_read(ser, file, "AT+CPOL")
    modem_helper.automate_test_read(ser, file, "AT+COPN")
    modem_helper.automate_test_read(ser, file, "AT+CTZU")
    modem_helper.automate_test_read(ser, file, "AT+CTZR")
    modem_helper.automate_test_read(ser, file, "AT+QLTS")
    modem_helper.automate_test_read(ser, file, "AT+QNWINFO")
    modem_helper.automate_test_read(ser, file, "AT+QSPN")
    modem_helper.automate_test_read(ser, file, "AT+QENG")
    modem_helper.automate_test_read(ser, file, "AT+QCAINFO")
    modem_helper.automate_test_read(ser, file, "AT+QENDC")
    modem_helper.automate_test_read(ser, file, "AT+QSCAN", False, 180)
    modem_helper.automate_test_read(ser, file, "AT+QNWCFG")
    modem_helper.automate_test_read(ser, file, "AT+QNWPREFCFG")


print("Runtime: ", (time.time()-start_time))