"""
Created by Colton Wright on 1/4/2023
Communicates to the Quectel RM502Q-AE modem through a serial port. The modem
uses the standard "Hayes command set" popular with modems. Attempt to read
some broadband data through the modem without actually connecting to a tower.
This is done with the "Network Service Commands" given in the modem's
documentation.

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

    # Returns the network registration status and returns the status of 
    # result code presentation and an integer <stat> which shows whether the
    # network has currently indicated the registration of MT
    # (Mobile Terminal). Location information parameters <lac> and <ci> are 
    # returned only when <n>=2 and MT is registered on the network.
    ser.write(b"AT+CREG?\r")
    time.sleep(.3)
    file.write(ser.read(100))

    # This command indicates the received signal strength <RSSI> and the 
    # channel bit error rate <ber>. This Test Command returns values supported
    # by MT. This Execution Command returns received signal strength
    # indication <RSSI> and channel bit error rate <ber> from MT. Gives
    # signal strength in -dBm format, power ratio in decibels of measured
    # power referenced to one milliwatt. Weak signal in the lab.
    ser.write(b"AT+CSQ\r")
    time.sleep(.3)
    file.write(ser.read(100))

    # The command queries and reports the RSRP of the current service network.
    # No service network available because there is no registered (U)SIM card.
    ser.write(b"AT+QRSRP\r")
    time.sleep(.3)
    file.write(ser.read(100))

    # This command queries network information such as access technology
    # selected, the operator and the band selected.
    ser.write(b"AT+QNWINFO\r")
    time.sleep(.3)
    file.write(ser.read(100))
