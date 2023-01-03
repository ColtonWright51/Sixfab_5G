from time import sleep
import serial

print("Connecting Port..")
try:
    serw = serial.Serial("/dev/ttyUSB3", baudrate = 115200, timeout = 1,rtscts=True, dsrdtr=True)
    serw.write('AT+CFUN=1,1\r'.encode())
    serw.close()
    sleep(1)
except Exception as e: 
    print("Serial port connection failed.")
    print(e)
