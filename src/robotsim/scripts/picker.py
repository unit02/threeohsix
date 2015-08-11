#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
import node.py
from geometry_msgs.msg import Twist
import numpy as np
from random import choice, randint
import node
from sensor_msgs.msg import Range




class picker(node):

	def __init__(self, name):
		node.__init__(self, "square", 1,1, "red")

		rospy.loginfo("Starting node %s" % name)
		self.laser_sub = rospy.Subscriber(
			"/robot_3/base_scan",
			LaserScan,
			callback=self.laser_callback,
			queue_size=10
		)

		self.cmd_vel_pub = rospy.Publisher(
			"cmd_vel",
			Twist,
			queue_size=10
		)
		pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
		rate = rospy.Rate(10) # 10hz


	def laser_callback(self,msg):
		ranges = msg.ranges
		min_distance = np.nanmin(ranges)
		twtist_msg = Twist()
		rate = rospy.Rate(10)
		if (min_distance <= 3):
			if (ranges.index(min_distance) <=30):
				twist_msg.linear.x = 1
				twist_msg.angular.z = 1
				self.cmd_vel_pub.publish(twist_msg)
			else:
				twist_msg.linear.x = 1
				twist_msg.angular.z = -1
				self.cmd_vel_pub.publish(twist_msg)
		else
			twist_msg.linear.x = 1
			twist_msg.angular.z = 0
			self.cmd_vel_pub.publish(twist_msg)
		rate.sleep()

        def rotateLeft:



		twist = Twist()
		twist.linear.x = 1.0
		twist.linear.y = 0
		twist.angular.x = 0.5


    for i in range(100):
        pub.publish(twist)
        rospy.sleep(0.1) # 30*0.1 = 3.0 seconds


	def rotateRight:

		
		


	def pick (self):
		pass
			#every 1 second "pick" kiwifruit
			  #sends signal to nearest carrier to updateBin()

	def goThroughRow(self):
		pass

	def goToNextRow(self):
		pass
	#assumes the picker is 


if __name__ == '__main__':
	rospy.init_node("picker1")
	p = picker(rospy.get_name())
	rospy.spin()
	picker()


