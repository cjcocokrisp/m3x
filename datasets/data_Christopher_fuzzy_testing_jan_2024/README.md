## Fuzzy Controller UR 2024 WIP Paper Dataset
### Overview
This dataset was used in the UR WIP Paper for the parameter tuning.

Files are broken up into sen (sensitive), nor (normal), and res (resistant) files. 
For the horizontal and push tasks a pressure sensor broke and only one was working so it is broken up into bicep and tricep files.
This is denoted by the letter at the end of the file b = bicep, t = tricep.

Each task directory also has a tune and no_tune directory. In the tune directory the fuzzy controller is active and in the no_tune directory the gain is preset to 10 throughout the entire way through.

### Tasks
- Vertical Movement
- Horizontal Pick and Place
- Pushing Motion 

### Data Collected From:
- Base Device
- Pressure Sensor