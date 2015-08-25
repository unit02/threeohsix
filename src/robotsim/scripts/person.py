#!/usr/bin/env python
import rospy
from node import node
import sys

class person(node):
    pass


# The block below will be executed when the python file is executed
# __name__ and __main__ are built-in python variables and need to start and end with *two* underscores
if __name__ == '__main__':
    rospy.init_node("robot_"+sys.argv[1])  # Create a node of name laser_roomba
    l = person(rospy.get_name(), True)  # Create an instance of above class
    rospy.spin()  # Function to keep the node running until terminated via Ctrl+C
