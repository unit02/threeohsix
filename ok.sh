killall xterm

sleep 2

rm -r build
rm -r devel


# roscore
xterm -e "catkin_make; source devel/setup.bash
" &

sleep 2

# stage
xterm-e "source devel/setup.bash; roscore" > /dev/null 2>&1 &

# scheduler

# actual robots
xterm -e "source devel/setup.bash; roslaunch robotsim launch.launch; read" > /dev/null 2>&1 &
xterm  -e "source devel/setup.bash; rosrun robotsim node.py; read" > /dev/null 2>&1 &
xterm -e "source devel/setup.bash;rosrun robotsim bin.py; read" > /dev/null 2>&1 &
xterm -e "source devel/setup.bash;rosrun robotsim picker.py; read" > /dev/null 2>&1 &
xterm -e "source devel/setup.bash;rosrun robotsim carrier.py; read" > /dev/null 2>&1 &
xterm -e "source devel/setup.bash;rosrun robotsim person.py; read" > /dev/null 2>&1 &
xterm -e "source devel/setup.bash;rosrun robotsim animal.py; read" > /dev/null 2>&1 &
xterm -e "source devel/setup.bash;rosrun stage_ros stageros src/robotsim/world/orchard.world; read" > /dev/null 2>&1 &



clear

