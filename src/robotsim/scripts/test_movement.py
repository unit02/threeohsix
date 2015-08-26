#!/usr/bin/env python
PKG = 'robotsim' # put in your own package name
from node import node
from person import person
import rospy
import unittest

# to perform the test we'll read odometry from stage
from nav_msgs.msg import Odometry

data_from_callback = Odometry()

def callback(data):
	global data_from_callback
	data_from_callback = data

# a test case that moves the robot_0 using our method and checks the odom data from stage
class TestRobotMoves(unittest.TestCase):
	rospy.init_node('testing_robot_moves', anonymous=True)
	rospy.Subscriber("robot_3/odom",Odometry,callback)
	def test_movement(self):
		# odom from stage is initially 0
		self.assertEquals(data_from_callback.pose.pose.position.x, 0)
		# move robot using the method we are testing
		commandX = moveRobot.moveX()
		commandX.robot_velocity()
		# odom should no longer be zero
		self.assertNotEquals(data_from_callback.pose.pose.position.x, 0)

if __name__ == '__main__':
	import rostest
	rostest.rosrun(PKG, 'test_robot_moves', TestRobotMoves)
