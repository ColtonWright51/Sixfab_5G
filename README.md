# Sixfab-5G
Testing for the Sixfab Raspberry Pi 5G Development Kit.

Can communicate to the Quectel RM502Q-AE modem through python script prog1.py

To detect the (U)SIM card for this Sixfab board, you must disable all Hot-Plug commands and restart the modem with the (U)SIM inserted. Make sure these commands are sent before restart:

`
AT+QSIMDET=0,0
AT+QSIMSTAT=0
AT+QUIMSLOT=1
`

Then insert the (U)SIM and restart the modem by flipping the Full Card Power (FCP) switch of OFF for 10 seconds. Run the command:

`
AT+QINISTAT
`

This command should now return a 7, meaning:
CPIN READY. Operation like locking/unlocking PIN is allowed.
SMS DONE. SMS initialization completed.
PB DONE. Phonebook initialization completed.
