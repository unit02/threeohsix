#!/usr/bin/env python
import rospy

from geometry_msgs.msg import Point
from havesting_robot import havesting_robot
import sys

from node import Face
class picker(havesting_robot):

    def move_down_rows(self):

        #new_position = Point(x_point+length_row +3, y_point, 0.0)
        self.move_x_steps(70)
        rospy.loginfo("Bin detaching")
        self.detach_bin()
        self.turnRight()
        self.move_x_steps(6)
        self.turnRight()
        self.move_x_steps(70)
     #    new_position = Point(x_point+length_row + 3, y_point-5.5, 0.0)
     #    self.move_to(new_position)
     #    self.move_to(new_position)
    #
	#     #p.reorientation()
     #    new_position = Point(x_point , y_point-5.5, 0.0)
     #    self.move_to(new_position)
     #    self.move_to(new_position)
	# #p.reorientation()
     #    new_position = Point(x_point+length_row, y_point-5, 0.0)
     #    self.move_to(new_position)
     #    self.move_to(new_position)
	# #p.reorientation()
     #    y_point=y_point-4.7


# The block below will be executed when the python file is executed
# __name__ and __main__ are built-in python variables and need to start and end with *two* underscores
if __name__ == '__main__':
    rospy.init_node("robot_"+sys.argv[1])  # Create a node of name robot_1
    p = picker(rospy.get_name(), True)  # Create an instance of above class

    p.move_down_rows()
    #p.wait(30)
    
    # Later release will ensure it gets a position from another robot by a message
    #Create arrays of points


    rospy.spin()  # Function to keep the node running until terminated via Ctrl+C
