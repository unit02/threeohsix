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
      
    #p.wait(30)
    
    # Later release will ensure it gets a position from another robot by a message
    #Create arrays of points
    
    x_point=-39
    y_point=11
    length_row=75
    numberofrows=2

    for i in range(0, numberofrows):
        new_position = Point(x_point+length_row, y_point, 0.0)
    	p.move_to(new_position)
	#Wait here for the new message
	new_position = Point(x_point+length_row, y_point-4.5, 0.0)
	p.move_to(new_position)
        y_point=y_point-4.5
        new_position = Point(x_point, y_point, 0.0) 
        p.move_to(new_position)
        new_position = Point(x_point+length_row, y_point-4.5, 0.0)
	p.move_to(new_position)
        y_point=y_point-4.5
	

    #new_position = Point(-34.5, -8.5, 0.0)
    #p.move_to(new_position)
    #new_position = Point(5, -8.5, 0.0)
    #p.move_to(new_position)

    rospy.spin()  # Function to keep the node running until terminated via Ctrl+C
