#!/bin/bash
#to run , use the command "bash run.sh"
#will remove build and devel folders for a fresh clean yay
rm -r build
rm -r devel
gnome-terminal -x sh -c 'roscore'
catkin_make
source devel/setup.bash
gnome-terminal -x sh -c 'roslaunch robotsim launch.launch'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim talker.py'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim test.py'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun stage_ros stageros src/robotsim/world/orchard.world'
