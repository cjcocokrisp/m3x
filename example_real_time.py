import myopro

ser = myopro.Device('...') # enter the port that the device is on here
ser.set_mode(3) # set to dual mode
ser.set_dual_mode_parameters(dual_mode_type=3) # set to proportional

# Sometimes you might need real time streaming data and to make sure that the string returned is the most recent
# To get that string simply just call this function
data_string = ser.get_data_string()

ser.disconnect()