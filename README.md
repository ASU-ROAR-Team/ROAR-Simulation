# ASU ROAR Simulation
## Dependencies
[ROAR-Msgs](https://github.com/ASU-ROAR-Team/ROAR-Msgs)

## Setup
``` bash
sudo apt install ros-noetic-urdf
sudo apt install ros-noetic-hector-gazebo-plugins
sudo apt install ros-noetic-robot-state-publisher
sudo apt install ros-noetic-controller-manager
sudo apt-get install ros-noetic-gazebo-ros-pkgs 
sudo apt-get install ros-noetic-gazebo-ros-control
```

## Running
``` bash 
roslaunch roar spawn.launch
```

## Published Topics
### IMU
`/imu` ([sensor_msgs/imu](http://docs.ros.org/en/api/sensor_msgs/html/msg/Imu.html))

### Encoders
`/joint_states` ([sensor_msgs/JointState](http://docs.ros.org/en/api/sensor_msgs/html/msg/JointStates.html))

### GPS
`/gps` ([sensor_msgs/NavSatFix](http://docs.ros.org/en/api/sensor_msgs/html/msg/NavSatFix.html))