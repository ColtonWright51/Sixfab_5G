"""
Created by Colton Wright on 1/27/2023
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

    file.write(b"prog9.py\n========================================\n")

    # All commands must start with AT or at and end with carriage return!
    modem_helper.automate_com(ser, file, "ATE1") # Enable echo
    modem_helper.automate_com(ser,file, "AT+CIMI") # Query IMSI number of (U)SIM which is attached to MT.
    modem_helper.automate_com(ser, file, "AT+CSMS=?") # List of supported <service>s
    # modem_helper.automate_com(ser, file, "AT+C5GNSSAIRDP=?")
    modem_helper.automate_com(ser, file, "AT+QENG=?") # List of supported <cell_type>s
    modem_helper.automate_com(ser, file, "AT+QSCAN=?") # range of supported <modes>s
    # modem_helper.automate_com(ser, file, "AT+QSCAN=3,1", 180)
    # modem_helper.automate_com(ser,file, "AT+COPS=?", 180)
    modem_helper.automate_com(ser, file, "AT+CGDCONT=?")
    modem_helper.automate_com(ser, file, "AT+CGDCONT?")
    modem_helper.automate_com(ser, file, "AT+CGDCONT=1,\"IPV4V6\",\"srsapn\"")
    modem_helper.automate_com(ser,file, "AT+COPS=?", 180)


print("Runtime: " + str(time.time()-start_time))