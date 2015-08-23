#!/bin/bash

roscore &
roslaunch robotsim launch.launch &
source setup.bash; rosrun robotsim node.py &
source setup.bash; rosrun robotsim animal.py 0 &
source setup.bash; rosrun robotsim animal.py 1 &
source setup.bash; rosrun robotsim animal.py 2 &
source setup.bash; rosrun robotsim person.py 3 &
source setup.bash; rosrun robotsim person.py 4 &
source setup.bash; rosrun robotsim person.py 5 &
source setup.bash; rosrun robotsim person.py 6 &
source setup.bash; rosrun robotsim person.py 7 &
source setup.bash; rosrun robotsim person.py 8 &
source setup.bash; rosrun robotsim person.py 9 &
source setup.bash; rosrun robotsim tractor.py 10 &
source setup.bash; rosrun robotsim picker.py 11 &
source setup.bash; rosrun robotsim picker.py 12 &
source setup.bash; rosrun robotsim carrier.py 13 &
source setup.bash; rosrun robotsim carrier.py 14 &
source setup.bash; rosrun robotsim bin.py 15 &
source setup.bash; rosrun robotsim bin.py 16 &
rosrun stage_ros stageros src/robotsim/world/orchard.world &




