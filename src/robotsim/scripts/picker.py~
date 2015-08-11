#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
import node.py
from geometry_msgs.msg import Twist

class picker(node):

	def __init__(self, name):
		node.__init__(self, "square", 1,1, "red")

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
		pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
		rate = rospy.Rate(10) # 10hz


	def laser_callback(self,msg):
		pass

        def rotateLeft:

		twist = Twist()
		twist.linear.x = 1.0
		twist.linear.y = 0
		twist.angular.x = 0.5

		#testing for github
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
	picker()


