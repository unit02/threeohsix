#!/bin/bash
rm -r build
rm -r devel
gnome-terminal -x sh -c 'roscore'
catkin_make
source devel/setup.bash
gnome-terminal -x sh -c 'roslaunch robotsim launch.launch'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim node.py'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim bin.py'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim picker.py'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim carrier.py'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim person.py'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim animal.py'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim tractor.py'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun stage_ros stageros src/robotsim/world/orchard.world'

