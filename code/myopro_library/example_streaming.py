import myopro
from time import time

ser = myopro.Device('...') # enter the port that the device is on here
ser.set_mode(3) # set to dual mode
ser.set_dual_mode_parameters(dual_mode_type=3) # set to proportional

# There are multiple ways of streaming data
# The first is start streaming and then read the data.
ser.start_streaming()
start_time = time()
while time() - start_time < 30:
    data = ser.get_string_while_streaming()
    print(data)
ser.stop_streaming()

ser.disconnect()