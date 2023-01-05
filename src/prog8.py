"""
Created by Colton Wright on 1/5/2023
Communicates to the Quectel RM502Q-AE modem through a serial port. The modem
uses the standard "Hayes command set" popular with modems. (U)SIM is
initialized, play with the settings.

https://en.wikipedia.org/wiki/Hayes_command_set

"""

import serial
import time
import modules.modem_helper as modem_helper

# Setup data directory & file name to save responses from modem
log_file_path = modem_helper.make_data_file()

start_time = time.time()


with serial.Serial('/dev/ttyUSB3', baudrate=115200, timeout=1) as ser, \
    open(log_file_path, 'ab') as file:

    file.write(b"prog8.py\n========================================\n")

    # All commands must start with AT or at and end with carriage return!
    modem_helper.automate_com(ser, file, "ATE1") # Enable echo

    modem_helper.automate_com(ser, file, "ATI")


    # Request International Mobile Equipment Identity (IMEI) number of the
    # Mobile Equipemnt (ME)
    modem_helper.automate_com(ser, file, "AT+GSN")

    # Check for full functionality level. Should give a 1.
    modem_helper.automate_com(ser, file, "AT+CFUN?", t_sleep=15)



    # This command queries the initialization status of (U)SIM card.
    modem_helper.automate_com(ser, file, "AT+QINISTAT") # Should give 7

    # This command requests the International Mobile Subscriber Identity
    # (IMSI) which is intended to permit the Terminal Equipment (TE) to 
    # identify the individual (U)SIM card or active application in the 
    # UICC (GSM or (U)SIM) that is attached to MT.
    modem_helper.automate_com(ser, file, "AT+CIMI")

    # Returns a string indicating whether or not a password is required.
    # No password is required...
    modem_helper.automate_com(ser, file, "AT+CPIN?")

    # PIN remainder counter, should be worthless
    modem_helper.automate_com(ser, file, "AT+QPINC?")










print("Runtime: " + str(time.time()-start_time))