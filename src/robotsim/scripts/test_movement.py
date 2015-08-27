#!/usr/bin/env python
PKG = 'robotsim' # put in your own package name
#import moveRobot

import node
import test_node
import weed
import rospy
import unittest
from geometry_msgs.msg import Point

# to perform the test we'll read odometry from stage
from nav_msgs.msg import Odometry

data_from_callback = Odometry()

def callback(data):
	global data_from_callback
	data_from_callback = data

""" This class tests the movement methods that are implemented in all the nodes"""
class TestRobotMoves(unittest.TestCase):
	rospy.init_node('testing_robot_moves', anonymous=False)
	rospy.Subscriber("robot_11/odom",Odometry,callback)
	
	"""Test move_to_method"""
	def test_move_to(self):
		# ensure that node starts from position 0
		self.assertEquals(int(data_from_callback.pose.pose.position.x), 0.0)
		
		commandX = weed.weed("robot_11", False)
		commandX.move_to(Point(4.0, 0.0, 0.0))
		
		# testing robot is in the correct position (allowing margin of error of <1)
		result = False
		if (data_from_callback.pose.pose.position.x > 3.5 ) & (data_from_callback.pose.pose.position.x < 4.5):
			result = True
		self.assertTrue(result)
		
	def test_move_to_backwards(self):
		# ensure that node starts from the earliest position (3,0,0)
		
		# move robot backward to position (-4,0,0)
		commandX = weed.weed("robot_11", False)
		#self.assertEquals(int(data_from_callback.pose.pose.position.x), 4.0)
		commandX.move_to(Point(0.0, 0.0, 0.0))
		result = False
		if (data_from_callback.pose.pose.position.x > -0.5 ) & (data_from_callback.pose.pose.position.x < 0.5):
			result = True
		self.assertTrue(result)
		# testing robot is in the correct position
		#self.assertEquals(int(data_from_callback.pose.pose.position.x), -3.0)
	
	"""Test move_x_steps_method"""
	def test_move_x_steps(self):
		#Starting position is (4,0,0)
		
		# move robot 3 meters using the method
		commandX = weed.weed("robot_11", False)
		commandX.move_x_steps(3)
		
		# testing robot is in the correct position
		result = False
		if (data_from_callback.pose.pose.position.x > -3.5 ) & (data_from_callback.pose.pose.position.x < -2.5):
			result = True
		self.assertTrue(result)
		
	def test_move_x_steps_backward(self):
		#Starting position is (-6,0,0)
		
		# move robot 3 meters using the method
		commandX = weed.weed("robot_11", False)
		commandX.move_x_steps(-3)
		
		# testing robot is in the correct position
		result = False
		if (data_from_callback.pose.pose.position.x > -6.5 ) & (data_from_callback.pose.pose.position.x < -5.5):
			result = True
		self.assertTrue(result)

	def test_laser_switching(self):
        	commandX = weed.weed("robot_11", False)
        	self.assertEqual(commandX.laser_on, False)

        	commandX.laser_on = True
        	self.assertEqual(commandX.laser_on , True)

    	def test_change_velocity(self):
        	commandX = weed.weed("robot_0", False)
        	twist = Twist()
        	twist.linear.x = 1.0
        	commandX.cmd_vel_pub.publish(twist)
		commandX.wait(5)
        	self.assertEqual(commandX.twist.linear.x , 1.0)
		
if __name__ == '__main__':
	import rostest
	rostest.rosrun(PKG, 'test_robot_moves', TestRobotMoves)
