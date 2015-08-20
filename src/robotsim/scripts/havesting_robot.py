#!/usr/bin/env python
from node import node
import rospy
import roslib
roslib.load_manifest('robotsim')
from robotsim.msg import bin_call


class havesting_robot(node):
	#Subscribes to the bin info topic to receive data on whether bins
    #need to be picked up
    def __init__(self,name, laser_on):
        super(havesting_robot,self).__init__(name,laser_on)
        self.pick_bin_sub = rospy.Subscriber(
			"/bin_info",
			bin_call,
			callback=self._pickBin_callback,
			queue_size=10
		)

    def _pickBin_callback(self,bin_call):
			rospy.loginfo("Recieving messages from %s xpos : %f, y pos : %f, isFull", bin_call.robot_name,bin_call.x_coordinate, bin_call.y_coordinate )





