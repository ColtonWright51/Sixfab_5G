# Sixfab-5G
Testing for the Sixfab Raspberry Pi 5G Development Kit.

Can communicate to the Quectel RM502Q-AE modem through python script prog1.py

### AT Commands

Every command you ever send to the modem must start with AT and end with a carriage return, '\r' in python. Each command also has a maximum response time of at least 300 ms, so this amount of time must elapse before another command is sent.

### (U)SIM Detection
To detect the (U)SIM card for this Sixfab board, you must disable all Hot-Plug commands and restart the modem with the (U)SIM inserted. Make sure these commands are sent before restart (`init_SIM_settings.py`):

```
AT+QSIMDET=0,0

AT+QSIMSTAT=0

AT+QUIMSLOT=1
```

Then insert the (U)SIM and restart the modem by flipping the Full Card Power (FCP) switch to OFF for 10 seconds. A few seconds after powering on the Sixfab board, the STAT LED should turn on.  Check the (U)SIM by running the command:

```
AT+QINISTAT
```

This command should now return a 7, meaning:
- CPIN READY. Operation like locking/unlocking PIN is allowed.
- SMS DONE. SMS initialization completed.
- PB DONE. Phonebook initialization completed.

`AT+QINISTAT` can tell you that the (U)SIM is ready, but if you query if the (U)SIM is detected with `AT+QSIMDET?` it will always tell you that (U)SIM card detection is disabled and the insert level is low.

### ModemManager

As soon as your (U)SIM card is detected by your modem, and you have a serial port connection between the Sixfab card and your PC, ModemManager will take control of the 4 serial ports the modem creates. `/dev/ttyUSB0 /dev/ttyUSB1 /dev/ttyUSB2 /dev/ttyUSB3` will all be busy. If you try to interact with them you'll get `/dev/ttyUSB3: Device or resource busy`