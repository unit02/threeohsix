#!/usr/bin/env python
from node import node
import rospy
import roslib
roslib.load_manifest('robotsim')
from robotsim.msg import bin_call, bin_detach
from geometry_msgs.msg import Point


class havesting_robot(node):
	#Subscribes to the bin info topic to receive data on whether bins
    #need to be picked up
    def __init__(self,name, laser_on):
        super(havesting_robot,self).__init__(name,laser_on)

        self.detachment = rospy.Publisher(
            self.name + "/detach",
            bin_detach,
            queue_size=1
        )

    def detach_bin(self):
        rospy.loginfo("Bin detaching")
        msg = bin_detach()
        msg.unfollow = True
        self.detachment.publish(msg)






