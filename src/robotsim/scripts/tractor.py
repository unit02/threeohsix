#!/usr/bin/env python
import rospy
from node import node
import sys
from havesting_robot import havesting_robot

class tractor(havesting_robot):
    pass
	

# The block below will be executed when the python file is executed
# __name__ and __main__ are built-in python variables and need to start and end with *two* underscores
if __name__ == '__main__':
    rospy.init_node("robot_"+sys.argv[1])  # Create a node of name laser_roomba
    driveway_width = 6.0
    object_width = 3.0
    l = tractor(rospy.get_name(), True, driveway_width, object_width)  # Create an instance of above class
    a = 1
    while a==1:
	l.wait(5)
	l.move_x_steps(20)
	l.turnRight()
	l.turnRight()
   
    
    rospy.spin()  # Function to keep the node running until terminated via Ctrl+C
