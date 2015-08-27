#!/bin/bash
rm -r build
rm -r devel
gnome-terminal -x sh -c 'roscore'
catkin_make
source devel/setup.bash; roslaunch robotsim launch.launch &
source devel/setup.bash; rosrun robotsim node.py &
source devel/setup.bash; rosrun robotsim animal.py 0 &
source devel/setup.bash; rosrun robotsim animal.py 1 &
source devel/setup.bash; rosrun robotsim animal.py 2 &
source devel/setup.bash; rosrun robotsim person.py 3 &
source devel/setup.bash; rosrun robotsim person.py 4 &
source devel/setup.bash; rosrun robotsim person.py 5 &
source devel/setup.bash; rosrun robotsim person.py 6 &
source devel/setup.bash; rosrun robotsim person.py 7 &
source devel/setup.bash; rosrun robotsim person.py 8 &
source devel/setup.bash; rosrun robotsim person.py 9 &
source devel/setup.bash; rosrun robotsim tractor.py 10 &
source devel/setup.bash; rosrun robotsim weed.py 11 &
source devel/setup.bash; rosrun robotsim weed.py 12 &
source devel/setup.bash; rosrun robotsim weed.py 13 &
source devel/setup.bash; rosrun robotsim weed.py 14 &
source devel/setup.bash; rosrun robotsim weed.py 15 &
source devel/setup.bash; rosrun robotsim weed.py 16 &
source devel/setup.bash; rosrun robotsim weed.py 17 &
source devel/setup.bash; rosrun robotsim weed.py 18 &
source devel/setup.bash; rosrun robotsim weed.py 19 &
source devel/setup.bash; rosrun robotsim weed.py 20 &
source devel/setup.bash; rosrun robotsim picker.py 21 &
source devel/setup.bash; rosrun robotsim picker.py 22 &
source devel/setup.bash; rosrun robotsim carrier.py 23 &
source devel/setup.bash; rosrun robotsim carrier.py 24 &
source devel/setup.bash; rosrun robotsim bin.py 25 &
source devel/setup.bash; rosrun robotsim bin.py 26 &
source devel/setup.bash; rosrun robotsim bin.py 27 &
source devel/setup.bash; rosrun robotsim bin.py 28 &
source devel/setup.bash; rosrun stage_ros stageros src/robotsim/world/orchard.world &
