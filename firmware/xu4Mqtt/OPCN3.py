import spidev
import time

# Open SPI bus 0, device 0 (CE0)
spi = spidev.SpiDev()
spi.open(0, 0)

# Configure speed and mode
spi.max_speed_hz = 1000000 # 1 MHz
spi.mode = 0

# Send data and receive response
data_to_send = [0x01, 0x02, 0x03]
response = spi.xfer(data_to_send)
print("Received:", response)

# Close the bus when finished
spi.close()
