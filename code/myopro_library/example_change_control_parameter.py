import myopro

ser = myopro.Device('...') # enter the port that the device is on here
ser.set_mode(3) # set to dual mode
ser.set_dual_mode_parameters(dual_mode_type=3) # set to proportional

# To set parameters just call these functions.
# For the bounds of these parameters check the device documentation.
ser.set_bicep_gain(10) # Set bicep gain
ser.set_tricep_gain(10) # Set tricep gain
new_et_b = new_et_t = 25
ser.set_effort_threshold(new_et_b, new_et_t) # Set bicep and tricep effort thresholds

ser.disconnect()