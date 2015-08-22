#!/usr/bin/env python
import rospy
from node import node

class tractor(node):
    pass
	

# The block below will be executed when the python file is executed
# __name__ and __main__ are built-in python variables and need to start and end with *two* underscores
if __name__ == '__main__':
    rospy.init_node("robot_5")  # Create a node of name laser_roomba
    l = tractor(rospy.get_name(), False)  # Create an instance of above class
    a = 1
    while a==1:
	l.wait(5)
	l.move_x_steps(20)
	l.turnRight()
	l.turnRight()
   
    
    rospy.spin()  # Function to keep the node running until terminated via Ctrl+C
