import serial
import time

baudrate = 9600
portIn = "/dev/ttyACM0" #probably needs to be dynamically found? maybe?

ser = serial.Serial(
    port= portIn,\
    baudrate=baudRate,\
	parity  =serial.PARITY_NONE,\
	stopbits=serial.STOPBITS_ONE,\
	bytesize=serial.EIGHTBITS,\
    timeout=0)

print(f"PMS7003 connected to {ser.port} at {ser.baudrate} baud.")

line = []

def main():
    while True:
        try:
            for c in ser.read():
                line.append(chr(c))
                if chr(c) == '\n':
                    if line.len() < 32:
                        continue
                    print(line)
                    line = []

if __name__ == "__main__":
    print("MINTS")
    main()

