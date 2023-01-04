import os
import datetime
import time


def make_data_file():
    now = datetime.datetime.today()
    now = now.strftime("%Y-%m-%d")
    data_path = os.path.join("data", now+"_data")
    os.makedirs(data_path, exist_ok=True)
    now = datetime.datetime.today()
    now = now.strftime("%Y-%m-%dT%H%M%S")
    log_file_path = os.path.join(data_path, now+"_log")
    return(log_file_path)

def automate_test_read(ser, file, command, read=True, t_sleep=0.3):
    # Send faster command
    bin_command = command.encode("ascii")
    ser.write(b"AT+"+bin_command+b"=?\r")
    time.sleep(t_sleep)
    file.write(ser.read(100))
    file.write(ser.read(100))
    file.write(ser.read(100))

    # This will give errors if command does not exist. Just will have
    # another error in the text file, it's fine.

    if(read):
        ser.write(b"AT+"+bin_command+b"?\r")
        time.sleep(t_sleep)
        file.write(ser.read(100))
        file.write(ser.read(100))
        file.write(ser.read(100))
