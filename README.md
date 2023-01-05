# Sixfab-5G
Testing for the Sixfab Raspberry Pi 5G Development Kit.

Can communicate to the Quectel RM502Q-AE modem through python script prog1.py

### AT Commands

Every command you ever send to the modem must start with AT and end with a carriage return, '\r' in python. Each command also has a maximum response time of at least 300 ms, so this amount of time must elapse before another command is sent.

### (U)SIM Detection
To detect the (U)SIM card for this Sixfab board, you must disable all Hot-Plug commands and restart the modem with the (U)SIM inserted. Make sure these commands are sent before restart:

```
AT+QSIMDET=0,0

AT+QSIMSTAT=0

AT+QUIMSLOT=1
```

Then insert the (U)SIM and restart the modem by flipping the Full Card Power (FCP) switch of OFF for 10 seconds. Run the command:

```
AT+QINISTAT
```

This command should now return a 7, meaning:
- CPIN READY. Operation like locking/unlocking PIN is allowed.
- SMS DONE. SMS initialization completed.
- PB DONE. Phonebook initialization completed.

`AT+QINISTAT` can tell you that the (U)SIM is ready, but if you query if the (U)SIM is detected with `AT+QSIMDET?` it will always tell you that (U)SIM card detection is disabled and the insert level is low.