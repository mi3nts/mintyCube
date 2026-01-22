import spidev
import time

# This library has NOT been tested in tandem with other SPI devices
# In the case of having multiple SPI devices, chip select will need to be handled

spi = spidev.SpiDev()

def main():
    opcInit()
    readStatus()
    readFirmware()

def opcInit():
    spi.open(0, 0)

    spi.max_speed_hz = 1000000 # 1 MHz
    spi.mode = 1

def readStatus():
    time.sleep(0.01)
    spi.xfer2([0x13])               
    response = spi.xfer2([0x00]*5) 
    print(response)


def readFirmware():
    time.sleep(0.01)
    response = spi.xfer([0x12])
    response = spi.xfer2([0x00]*3)
    print(response)

if __name__ == "__main__":
    print("==========================")
    print("MINTS Python OPC N3 Reader")
    print("==========================")
    main()

