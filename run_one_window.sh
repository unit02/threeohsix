#!/bin/bash
source devel/setup.bash
roscore &
roslaunch robotsim launch.launch &
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
source devel/setup.bash; rosrun robotsim picker.py 11 &
source devel/setup.bash; rosrun robotsim picker.py 12 &
source devel/setup.bash; rosrun robotsim carrier.py 13 &
source devel/setup.bash; rosrun robotsim carrier.py 14 &
source devel/setup.bash; rosrun robotsim bin.py 15 &
source devel/setup.bash; rosrun robotsim bin.py 16 &
rosrun stage_ros stageros src/robotsim/world/orchard.world &




