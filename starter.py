import myopro

PORT = ""
# CHANNELS = []

ser = myopro.Device(PORT)
ser.set_mode(3)
ser.set_dual_mode_parameters(dual_mode_type=3)
# ser.connect_daq(CHANNELS)

# Insert your code here

#ser.daq_device.disconnect()
ser.disconnect()