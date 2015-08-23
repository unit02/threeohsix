#!/usr/bin/env python
import rospy

from geometry_msgs.msg import Point
from havesting_robot import havesting_robot
import sys

from node import Face
class picker(havesting_robot):

    # def move_down_rows(self):
     #    x_point=self.position.x
     #    y_point=self.position.y
     #    length_row=75
     #    numberofrows=2
    #
     #    for i in range(0, numberofrows):
     #        new_position = Point(x_point+length_row, y_point, 0.0)
    	#     self.move_to(new_position)
	#     #Wait here for the new message
     #    new_position = Point(x_point+length_row, y_point-4.7, 0.0)
     #    self.move_to(new_position)
    #
     #    self.detach_bin()
    #
	#     #p.reorientation()
     #    y_point=y_point-4.7
    #
     #    new_position = Point(x_point, y_point, 0.0)
     #    self.move_to(new_position)
	#     #p.reorientation()
     #    new_position = Point(x_point, y_point-4.7, 0.0)
     #    self.move_to(new_position)
	# #p.reorientation()
     #    y_point=y_point-4.7
    #



    #new_position = Point(-34.5, -8.5, 0.0)
    #p.move_to(new_position)
    #new_position = Point(5, -8.5, 0.0)
    #p.move_to(new_position)

    def move_down_rows(self):
            x_point=self.position.x
            y_point=self.position.y
            length_row=70
            numberofrows=2

            new_position = Point(x_point+length_row, y_point, 0.0)
            p.move_to(new_position)
            rospy.logwarn("detach bin")
            self.detach_bin()
            #Wait here for the new message
            rospy.logwarn("Turning right 1st time")
            p.turnRight()
            rospy.logwarn("four steps forward")
            p.move_x_steps(5)

            rospy.logwarn("Turning right 2nd time")
            p.turnRight()
            rospy.logwarn("move to end of next row")

            new_position = Point(x_point, y_point-5, 0.0)
            p.move_to(new_position)

            # y_point=y_point-4.5
            # p.move_to(new_position)
            # new_position = Point(x_point+length_row, y_point-5, 0.0)
            # p.move_to(new_position)
            # y_point=y_point-5



# The block below will be executed when the python file is executed
# __name__ and __main__ are built-in python variables and need to start and end with *two* underscores
if __name__ == '__main__':
    rospy.init_node("robot_"+sys.argv[1])  # Create a node of name robot_1
    p = picker(rospy.get_name(), False)  # Create an instance of above class

    p.move_down_rows()
    #p.wait(30)
    
    # Later release will ensure it gets a position from another robot by a message
    #Create arrays of points


    rospy.spin()  # Function to keep the node running until terminated via Ctrl+C
