#!/usr/bin/env python
import rospy

from geometry_msgs.msg import Point
from havesting_robot import havesting_robot
import sys

class picker(havesting_robot):

    def move_down_rows(self):


        row_width=6
        row_length=78


        #For loop here with variable
        if self.position.x < 0:
            self.move_x_steps(row_length)
            rospy.loginfo("Bin detaching")
            self.detach_bin()
            self.turnRight()
            self.move_x_steps(row_width)
            self.turnRight()
            self.reorientation()
            self.move_x_steps(8)

        else:
            self.move_x_steps(row_length)
            rospy.loginfo("Bin detaching")
            self.detach_bin()
            self.turnLeft()
            self.move_x_steps(row_width)
            self.turnLeft()
            self.reorientation()
            self.move_x_steps(8)



# The block below will be executed when the python file is executed
# __name__ and __main__ are built-in python variables and need to start and end with *two* underscores
if __name__ == '__main__':
    rospy.init_node("robot_"+sys.argv[1])  # Create a node of name robot_1
    row_width = 5.0
    object_width = 1.5

    p = picker(rospy.get_name(), True, row_width, object_width)  # Create an instance of above class

    p.move_down_rows()
    #p.wait(30)
    
    # Later release will ensure it gets a position from another robot by a message
    #Create arrays of points


    rospy.spin()  # Function to keep the node running until terminated via Ctrl+C
