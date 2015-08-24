#!/usr/bin/env python
from node import node
import rospy
import roslib
roslib.load_manifest('robotsim')
from robotsim.msg import bin_call, bin_detach, attach_bin
from geometry_msgs.msg import Point, Twist
from sensor_msgs.msg import LaserScan

class havesting_robot(node):
	#Subscribes to the bin info topic to receive data on whether bins
    #need to be picked up
    def __init__(self,name, laser_on):
        self.is_stopped = False
        super(havesting_robot,self).__init__(name,laser_on)

        self.detachment = rospy.Publisher(
            self.name + "/detach",
            bin_detach,
            queue_size=1
        )
        self.attachment = rospy.Publisher(
            "/attach_bin",
            attach_bin,
            queue_size=1
        )

    def bin_attach(self, bin_name):
        rospy.loginfo("Bin attaching")
        msg = attach_bin()
        msg.to_attach_name = self.name
        msg.bin_name = bin_name
        self.attachment.publish(msg)

    def detach_bin(self):
        rospy.loginfo("Bin detaching")
        msg = bin_detach()
        msg.unfollow = True
        self.detachment.publish(msg)

    def laser_callback(self,msg):
        if self.laser_on:
            # Get the ranges of the laser scan
            ranges = msg.ranges
            rate = rospy.Rate(10)
            stop = False

            for i in range(60):
                if (ranges[i] < 2.5):
                    stop = True

            if not self.is_stopped and stop:
                self.is_stopped = True
                self.event.clear()
                rospy.logwarn("Stopping robot, something in the way,  %s")

            # publish a 0 velocity speed
            if stop:
                twist = Twist()
                self.cmd_vel_pub.publish(twist)

            # nothing in the way anymore - so signals it can move
            if self.is_stopped and not stop:
                self.is_stopped = False
                self.event.set()
                rospy.loginfo("Event set, so should continue moving")

            rate.sleep()




