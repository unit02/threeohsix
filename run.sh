#!/bin/bash
<<<<<<< HEAD
#to run , use the command "bash run.sh"
#will remove build and devel folders for a fresh clean yay
=======
>>>>>>> 3c79488711cc88a0572c589005317caa6c8e0043
rm -r build
rm -r devel
gnome-terminal -x sh -c 'roscore'
catkin_make
source devel/setup.bash
gnome-terminal -x sh -c 'roslaunch robotsim launch.launch'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim talker.py'
source devel/setup.bash
<<<<<<< HEAD
gnome-terminal -x sh -c 'rosrun robotsim test.py'
=======
gnome-terminal -x sh -c 'rosrun robotsim listener.py'
>>>>>>> 3c79488711cc88a0572c589005317caa6c8e0043
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun stage_ros stageros src/robotsim/world/orchard.world'
