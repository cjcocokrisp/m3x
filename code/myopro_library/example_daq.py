import myopro

ser = myopro.Device('...') # enter the port that the device is on here
ser.set_mode(3) # set to dual mode
ser.set_dual_mode_parameters(dual_mode_type=3) # set to proportional

# Connecting to the DAQ is simple just include the channels in the list parameter.
ser.connect_daq([0, 1])

# To read from the daq just call this function
daq_0, daq_1 = ser.daq_device.read_values() # The returned list has the engineering for each channel in the order that you connected them
print(daq_0, daq_1)

ser.daq_device.disconnect()
ser.disconnect()