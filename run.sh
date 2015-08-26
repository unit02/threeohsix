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
gnome-terminal -x sh -c 'rosrun robotsim animal.py 0'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim animal.py 1'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim animal.py 2'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim person.py 3'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim person.py 4'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim person.py 5'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim person.py 6'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim person.py 7'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim person.py 8'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim person.py 9'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim tractor.py 10'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim picker.py 11'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim picker.py 12'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim picker.py 13'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim carrier.py 14'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim carrier.py 15'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim carrier.py 16'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim bin.py 17'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim bin.py 18'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim bin.py 19'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim bin.py 20'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim bin.py 21'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim bin.py 22'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim weed.py 23'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim weed.py 24'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim weed.py 25'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim weed.py 26'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim weed.py 27'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim weed.py 28'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim weed.py 29'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim weed.py 30'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim weed.py 31'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun robotsim weed.py 32'
source devel/setup.bash
gnome-terminal -x sh -c 'rosrun stage_ros stageros src/robotsim/world/orchard.world'
