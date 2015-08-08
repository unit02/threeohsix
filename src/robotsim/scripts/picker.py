#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
import dynamicObjects.py
import havestingRobot.py
import Twist
class picker(havestingRobot):

	def __init__(self, name):
		dynamicObjects.__init__(self, "square", 1,1, "red")

		rospy.loginfo("Starting node %s" % name)
		self.laser_sub = rospy.Subscriber(
			"laser",
			LaserScan,
			callback=self.laser_callback,
			queue_size=1
		)

		self.cmd_vel_pub = rospy.Publisher(
			"laser",
			Twist,
			queue_size=1
		)

	def laser_callback(self,msg):
	


	def pick (self):
			#every 1 second "pick" kiwifruit
			  #sends signal to nearest carrier to updateBin()

	def goThroughRow(self):


	def goToNextRow(self):
	#assumes the picker is 

