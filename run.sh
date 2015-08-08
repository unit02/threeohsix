#!/bin/bash

source devel/setup.bash
gnome-terminal -x sh -c 'roscore'
source devel/setup.bash
gnome-terminal -x sh -c 'roslaunch robotsim launch.launch'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim talker.py'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun stage_ros stageros src/robotsim/world/orchard.world'
