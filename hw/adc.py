# Simple example of reading the MCP3008 analog input channels and printing
# them all out.
# Author: Tony DiCola
# License: Public Domain

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import time,sys

# Software SPI configuration:
#CLK  = 18
#MISO = 23
#MOSI = 24
#CS   = 25
#mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
# variables
current_value = 0
previous_value = 0
up_down_delta = 100
state = ""

FREQ=float(sys.argv[1])
#print('Reading MCP3008 values, press Ctrl-C to quit...')
# Print nice channel column headers.
#print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*range(8)))
#print('-' * 57)
# Main program loop.
counter=0
sys.stdout.write('[')
while True:
    # Read all the ADC channel values in a list.
    values = [0]*8
    for i in range(8):
        # The read_adc function will get the value of the specified channel (0-7).
        values[i] = mcp.read_adc(i)
    # Print the ADC values.
    #print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
    #print values[1]
    previous_value = current_value
    current_value = values[1]
    delta = current_value - previous_value
    if delta >= up_down_delta:
    	state = "DOWN"
    elif delta <= -1*up_down_delta:
	state = "UP"
    #print state
    #print "delta: ",delta
	 # Pause for half a second.
    sys.stdout.write(str(current_value)+',')
    counter+=1
    if counter == 600 :
	counter=0
	sys.stdout.flush()
    time.sleep(1/FREQ)

