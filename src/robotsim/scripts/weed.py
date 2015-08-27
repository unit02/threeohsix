#!/usr/bin/env python
import rospy
import sys
import numpy as np
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from node import node
from nav_msgs.msg import Odometry

class weed(node):
	def __init__(self,name,laser_on):
		super(weed,self).__init__(name,laser_on)
		rospy.loginfo("Starting node %s" % name)
		self.cmd_vel_pub = rospy.Publisher(
        	    self.name + "/cmd_vel",
        	    Twist,
        	    queue_size=10
        	)

		# Create new topic called laser to which it listens
        	self.laser_sub = rospy.Subscriber(
                    self.name + "/base_scan",
                    LaserScan,
                    callback=self.laser_callback,
                    queue_size=10
                )

		# Subscribe to stage topic to obtain its position
      		# Must change to approprite name instead "ns" + cmd_vel
        	self.stage_info = rospy.Subscriber(
            		self.name + "/base_pose_ground_truth",
            		Odometry,
            		callback=self.stage_callback,
            		queue_size=10
        	)
        	# wait to gather stage information
        	# self.wait(20)


	def laser_callback(self,msg):
		ranges = msg.ranges
		min_distance = np.nanmin(ranges)
		if (min_distance < 2):
			twist = Twist()
			twist.linear.x = 200
			for i in range(5):
                		self.cmd_vel_pub.publish(twist)
                		rospy.sleep(0.1)
			twist = Twist()
			twist.linear.x = 0
			self.cmd_vel_pub.publish(twist)
			rospy.loginfo("Done")

if __name__ == '__main__':
	rospy.init_node("robot_"+sys.argv[1])  # Create a node of name laser_roomba
	l = weed(rospy.get_name(),False)  # Create an instance of above class

	rospy.spin()  # Function to keep the node running until terminated via Ctrl+C


