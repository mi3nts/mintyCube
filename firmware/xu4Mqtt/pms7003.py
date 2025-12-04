import serial
import time

baudRate = 9600
portIn = "/dev/ttyS0" #probably needs to be dynamically found? maybe?

ser = serial.Serial(
    port= portIn,\
    baudrate=baudRate,\
	parity  =serial.PARITY_NONE,\
	stopbits=serial.STOPBITS_ONE,\
	bytesize=serial.EIGHTBITS,\
    timeout=0)

print(f"PMS7003 connected to {ser.port} at {ser.baudrate} baud.")

def main()
    data = read_pms7003()


def read_pms7003():
    while True:
        if ser.read(1) == b'\x42':
            if ser.read(1) == b'\x4d':
                print("got here")
                frame = ser.read(30)  
                if len(frame) == 30:
                    data = b'\x42\x4d' + frame
                    return data


if __name__ == "__main__":
    print("MINTS")
    main()

