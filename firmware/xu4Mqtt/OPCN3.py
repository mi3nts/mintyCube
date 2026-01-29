import spidev
import time

# This library has NOT been tested in tandem with other SPI devices
# In the case of having multiple SPI devices, chip select will need to be handled

spi = spidev.SpiDev()

def test():
    opcInit()
    startSampling() # includes wait
    while(True):
        readStatus()
        #readSample()
        time.sleep(1)

def main():
    opcInit()
    fanOn()
    readStatus()
    readFirmware()

def opcInit():
    spi.open(0, 0)
    spi.max_speed_hz = 1000000 # 100 kHz
    spi.mode = 0
    time.sleep(1)

def readStatus():
    time.sleep(0.02)
    response = spi.xfer2([0x13] + 5*[0x00])                
    print(response)

def fanOn():
    time.sleep(0.02)
    response = spi.xfer2([0x03, 0x04, 0x00, 0x00])
    print(response)
    time.sleep(1)

def fanOff():
    time.sleep(0.02)
    response = spi.xfer2([0x03, 0x05, 0x00, 0x00])
    print(response)

def readFirmware():
    time.sleep(0.02)
    response = spi.xfer2([0x12] + 3*[0x00])
    print(response)

def startSampling():
    time.sleep(0.02)
    spi.xfer2([0x03, 0x00, 0x00, 0x00])
    time.sleep(2)

def readSample():
    time.sleep(0.02)
    response = spi.xfer2([0x32] + 13*[0x00])
    print(response)

if __name__ == "__main__":
    print("==========================")
    print("MINTS Python OPC N3 Reader")
    print("==========================")
    test()

