"""
Created by Colton Wright on 1/4/2023
Communicates to the Quectel RM502Q-AE modem through a serial port. The modem
uses the standard "Hayes command set" popular with modems. Show nearly all commands

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
    modem_helper.automate_com(ser, file, "ATE1") # Enable echo

    # SECTION 2 GENERAL COMMANDS
    modem_helper.automate_com(ser, file, "ATI")

    modem_helper.automate_com(ser, file, "AT+GMI")

    modem_helper.automate_com(ser, file, "AT+GMM")

    modem_helper.automate_com(ser, file, "AT+GMR")

    modem_helper.automate_com(ser, file, "AT+CGMI")

    modem_helper.automate_com(ser, file, "AT+CGMM")
    modem_helper.automate_com(ser, file, "AT+CGMR")

    modem_helper.automate_com(ser, file, "AT+GSN")
    modem_helper.automate_com(ser, file, "AT+CGSN")
    modem_helper.automate_com(ser, file, "AT&V")

    modem_helper.automate_com(ser, file, "AT+CFUN=?", t_sleep=15)
    modem_helper.automate_com(ser, file, "AT+CFUN?", t_sleep=15)



    # SECTION 3 STATUS CONTROL COMMANDS
    modem_helper.automate_com(ser, file, "AT+CPAS=?")
    modem_helper.automate_com(ser, file, "AT+CPAS")

    modem_helper.automate_com(ser, file, "AT+CEER=?")
    modem_helper.automate_com(ser, file, "AT+CEER") # Error if there is any error related to MT functionality


    # This command queries and configures various settings of User Equipment (UE).
    modem_helper.automate_com(ser, file, "AT+QCFG=?")

    # This command specifies the High Speed Downlink Packet Access (HSDPA) category.
    # Category 6, 8, 10, 12, 14, 18, 20 and 24 available
    # modem_helper.automate_com(ser, file, "AT+QINDCFG")




    # SECTION 4 (U)SIM COMMANDS

    # This command requests the International Mobile Subscriber Identity 
    # (IMSI) which is intended to permit the TE to identify the individual
    # (U)SIM card or active application in the UICC (GSM or (U)SIM) that is
    # attached to MT.
    modem_helper.automate_com(ser, file, "AT+CIMI") # Error if there is any error related to MT functionality
    
    modem_helper.automate_com(ser, file, "AT+CLCK=?", t_sleep=5)
    modem_helper.automate_com(ser, file, "AT+CPIN?", t_sleep=5)
    modem_helper.automate_com(ser, file, "AT+CPWD=?", t_sleep=5)

    # These commands give generic and restricted (U)SIM access.
    # modem_helper.automate_com(ser, file, "AT+CSIM")
    # modem_helper.automate_com(ser, file, "AT+CRSM")

    # This command opens a logical channel
    # modem_helper.automate_com(ser, file, "AT+CCHO")
    # This command closes a logical channel
    # modem_helper.automate_com(ser, file, "AT+CCHC")
    # Generic logical channel access
    # modem_helper.automate_com(ser, file, "AT+CGLA")

    # This command queries the number of attempts left to enter the password
    # of (U)SIM PIN/PUK.
    modem_helper.automate_com(ser, file, "AT+QPINC=?")

    # This command queries the initialization status of (U)SIM card.
    modem_helper.automate_com(ser, file, "AT+QINISTAT=?")
    modem_helper.automate_com(ser, file, "AT+QINISTAT")

    # This command enables (U)SIM card hot-swap function. (U)SIM card is
    # detected by GPIO interrupt. The level of (U)SIM card detection pin
    # should also be set when the (U)SIM card is inserted.
    modem_helper.automate_com(ser, file, "AT+QSIMDET=?")
    modem_helper.automate_com(ser, file, "AT+QSIMDET?")
    modem_helper.automate_com(ser, file, "AT+QSIMDET=1,0")

    # This command queries (U)SIM card insertion status or determines whether
    # (U)SIM card insertion status report is enabled.
    modem_helper.automate_com(ser, file, "AT+QSIMSTAT=?")
    modem_helper.automate_com(ser, file, "AT+QSIMSTAT?")
    modem_helper.automate_com(ser, file, "AT+QSIMSTAT=1")

    # This command queries the slot currently used by the (U)SIM and
    # configure which to use.
    modem_helper.automate_com(ser, file, "AT+QUIMSLOT=?")
    modem_helper.automate_com(ser, file, "AT+QUIMSLOT?")



print("Runtime: " + str(time.time()-start_time))