"""
Created by Colton Wright on 1/5/2023

Communicates to the Quectel RM502Q-AE modem through a serial port. The modem
uses the standard "Hayes command set" popular with modems. Set settings
so that the modem can detect the (U)SIM after the Full Card Power (FCP)
switch is reset.

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

    # Turn off (U)SIM Hot-Plug detection
    modem_helper.automate_com(ser, file, "AT+QSIMDET=0,0")

    # Turn off (U)SIM insertion status reports
    modem_helper.automate_com(ser, file, "AT+QSIMSTAT=0")

    # Set the (U)SIM card slot to slot 1. Slot 2 is unused.
    modem_helper.automate_com(ser, file, "AT+QUIMSLOT=1")

# Now reset the modem & the (U)SIM will be detected.
print("Runtime: " + str(time.time()-start_time))