## Hamid's Model Training Data
### Overview:
Data collected for modeling for the UR 2024 Paper, *Investigating the Generalizability of Assistive Robots Models over Various Tasks*.

The thresholds in this data go from 65 to 10 and cover all combinations. There are also three different folders that cover three different participants. IMU sensors are also included on this dataset to help track positions better.

### Column Information:
The following columns are included in each of the data file types:

#### Model:
- device_type
- time
- pose
- Bi_cl_effort
- Tr_op_effort
- Bi_cl_E_T
- Tr_op_E_T
- IMU_id_E
- accl_x_E
- accl_y_E
- accl_z_E
- gyro_x_E
- gyro_y_E
- gyro_z_E
- mag_x_E
- mag_y_E
- mag_z_E

#### Processed:
- psi_gyro_E
- filtered_gyro_z_E
- Bi_cl_effort
- Tr_op_effort
- Bi_cl_E_T
- Tr_op_E_T
- del_psi_gyro_E
- del_gyro_z_deg_E
- psi_gyro_H
- filtered_gyro_z_H
- Cl_cl_effort
- Op_op_effort
- Cl_cl_E_T
- Op_op_E_T
- del_psi_gyro_H
- del_gyro_z_deg_H

### Tasks:
- Left Foot to Right Eye
- Right Foot to Left Eye 
- Eating Motion
- Push Motion
- Horizontal Movement
- Vertical Movement

### Data Collected From:
- Base Device
- IMU Sensors