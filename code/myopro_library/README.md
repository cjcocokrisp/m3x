## Myopro Library
### Overview

The purpose of this library is to provide a wrapper class to interact with Myopro 2 device. The class provides methods to stream and read data, change the device's control parameters, and run other commands that have not been implemented through functions. 

The library also allows for communication with Measurement Computing devices to be used with the Myopro 2 to collect extra information through the `mcculw` library.

### Installation

Installing this library is simple. Just download the code from this directory as a zip and then place the `myopro` folder in your project. 

There also are a few dependencies for the library being [`pyserial`](https://pypi.org/project/pyserial/) and [`mcculw`](https://github.com/mccdaq/mcculw). You can install them manually or use the `requirements.txt` file in the following manner.
```
pip install -r requirements.txt
```

### Usage 

To use the wrapper import the class by doing the following.
```
import myopro 
# or
from myopro import Device
```

### Documentation

The current functions provide doc strings that explain the functions arguments and usage. More detailed docs are currently being developed.

### Examples

There are some example files in the base directory when the project is installed. These examples can help you get started with usage of the code.

Current Examples:

- `example_change_control_parameter.py` - demonstrates how to change the control parameters of the device with the library.
- `example_daq.py` - shows how to use a Measurement Computing device with the code and read values from it.
- `example_real_time.py` - shows how to read the real time values of the device.
- `example_straming.py` - shows how to stream data from the devices.
- `example_streaming_2.py` - shows how to stream data from the devices using the `stream_data` method and explains the various arguments the function has.
