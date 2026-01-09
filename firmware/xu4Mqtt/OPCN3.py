import spidev
import time

# This library has NOT been tested in tandem with other SPI devices
# In the case of having multiple SPI devices, chip select will need to be handled

spi = spidev.SpiDev()

def main():
    opcn3_init()
    read_status()

def opcn3_init():
    spi.open(0, 0)

    spi.max_speed_hz = 1000000 # 1 MHz
    spi.mode = 0

    # Send data and receive response
    # data_to_send = [0x01, 0x02, 0x03]
    # response = spi.xfer(data_to_send)
    # print("Received:", response)

    # Close the bus when finished

def read_status():
    time.sleep(0.01)
    response = spi.xfer2([0x13, 0x13, 0x13, 0x13, 0x13])
    print(response)

def read_firmware():
    time.sleep(0.01)
    response = spi.xfer([0x12, 0x12, 0x12])
    print(response)

if __name__ == "__main__":
    print("==========================")
    print("MINTS Python OPC N3 Reader")
    print("==========================")
    main()

