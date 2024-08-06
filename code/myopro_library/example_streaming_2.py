import myopro
from time import time

ser = myopro.Device('...') # enter the port that the device is on here
ser.set_mode(3) # set to dual mode
ser.set_dual_mode_parameters(dual_mode_type=3) # set to proportional

# There are multiple ways of streaming data
# The second is using the stream data command which streams to a file.
# There are optional parameters to add things to the streaming process
# The parameters are described below
ser.stream_data()
# stream_time - the amount of time in seconds that you want to stream (required)
# log - whether you want to log the data to a file (default is True)
# command - a function you can pass that requires an argument of the device (default is None)
# command_interval - the interval in seconds you want to run the command (default is 0)
# print_data - whether you want to print data as its collecting (default is False)
# directory - a string that will place the produced log in another folder (default is None)
# print_time - the interval to print data while streaming (default is 0)
# use_daq -  specifies if daq data should be included in data collection (default is False)
# create_model - specifies if you want to have labels with your csv (default is False)
# model_parameters - specifies the model columns, see documentation on model columns for more info (default is None)
# return data - mark True if you want the data collected to be put into a list and then returned (default is False)

ser.disconnect()