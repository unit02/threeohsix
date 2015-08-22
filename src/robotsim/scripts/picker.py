#!/usr/bin/env python
import rospy

from geometry_msgs.msg import Point
from havesting_robot import havesting_robot


class picker(havesting_robot):
    pass


# The block below will be executed when the python file is executed
# __name__ and __main__ are built-in python variables and need to start and end with *two* underscores
if __name__ == '__main__':
    rospy.init_node("robot_1")  # Create a node of name robot_1
    p = picker(rospy.get_name(), False)  # Create an instance of above class
    rospy.spin()  # Function to keep the node running until terminated via Ctrl+C
