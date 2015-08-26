#!/bin/bash
source devel/setup.bash
roscore &
cd src/robotsim/scripts &
rosrun robotsim test_node.py &
python test_node.py & 
cd ../../.. &
source devel/setup.bash; rosrun robotsim weed.py 11 &
source devel/setup.bash; rosrun stage_ros stageros src/robotsim/world/orchard.world &
cd src/robotsim/scripts &
python test_movement.py
