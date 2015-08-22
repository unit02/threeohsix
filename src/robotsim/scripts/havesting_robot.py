#!/usr/bin/env python
from node import node
import rospy
import roslib
roslib.load_manifest('robotsim')
from robotsim.msg import bin_call
from geometry_msgs.msg import Point


class havesting_robot(node):
	#Subscribes to the bin info topic to receive data on whether bins
    #need to be picked up
    def __init__(self,name, laser_on):
        super(havesting_robot,self).__init__(name,laser_on)
        node = self.pick_bin_sub = rospy.Subscriber(
			"/bin_info",
			bin_call,
			callback=self._pickBin_callback,
			queue_size=1
		)

    def _pickBin_callback(self,bin_call):
        self.wait(5)
        new_position = Point(bin_call.x_coordinate + 2, bin_call.y_coordinate + 2, 0.0)
        rospy.loginfo("moving to newwwww position")
        self.move_to(new_position)
        #rospy.loginfo("Recieving messages from %s xpos : %f, y pos : %f, isFull", bin_call.robot_name,bin_call.x_coordinate, bin_call.y_coordinate)






