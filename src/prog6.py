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
    modem_helper.automate_com(ser, file, "ATE1") # Enable echo

    modem_helper.automate_com(ser, file, "ATI")


    # Request International Mobile Equipment Identity (IMEI) number of the
    # Mobile Equipemnt (ME)
    modem_helper.automate_com(ser, file, "AT+GSN")

    # Check for full functionality level. Should give a 1.
    modem_helper.automate_com(ser, file, "AT+CFUN?", t_sleep=15)



    # Queries the activity status of the Mobile Equipment, 0 = Ready
    modem_helper.automate_com(ser, file, "AT+CPAS")

    # This command queries the initialization status of (U)SIM card.
    modem_helper.automate_com(ser, file, "AT+QINISTAT") # Will give 0 for initial state

    # This command enables (U)SIM card hot-swap function. (U)SIM card is
    # detected by GPIO interrupt. The level of (U)SIM card detection pin
    # should also be set when the (U)SIM card is inserted.
    # The Sixfab board does not have hot-plug capability. They are only
    # using a 6-pin SIM card, hot-plug requires 8 pins.
    modem_helper.automate_com(ser, file, "AT+QSIMDET?")


    # This command queries (U)SIM card insertion status or determines whether
    # (U)SIM card insertion status report is enabled.
    modem_helper.automate_com(ser, file, "AT+QSIMSTAT=?")
    modem_helper.automate_com(ser, file, "AT+QSIMSTAT?")
    modem_helper.automate_com(ser, file, "AT+QSIMSTAT=1")





    # This command queries the slot currently used by the (U)SIM and
    # configure which to use. The RM502Q-AE is definitely wired to use
    # the (U)SIM 1 slot, (U)SIM 2 is not hooked up for this modem
    modem_helper.automate_com(ser, file, "AT+QUIMSLOT=?")
    modem_helper.automate_com(ser, file, "AT+QUIMSLOT?")
    modem_helper.automate_com(ser, file, "AT+QUIMSLOT=1")

    modem_helper.automate_com(ser, file, "AT+QSIMDET=1,0")
    modem_helper.automate_com(ser, file, "AT+QSIMDET?")
    modem_helper.automate_com(ser, file, "AT+QINISTAT")
print("Runtime: " + str(time.time()-start_time))