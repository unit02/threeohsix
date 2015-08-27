#!/usr/bin/env python
PKG = 'robotsim' # put in your own package name
#import moveRobot

import node
import test_node
import weed
import rospy
import unittest
from geometry_msgs.msg import Point, Twist
from std_msgs.msg import String

# to perform the test we'll read odometry from stage
from nav_msgs.msg import Odometry

data_from_callback = Odometry()

def callback(data):
	global data_from_callback
	data_from_callback = data

class Face:
    North, South, East, West = range(4)

    @classmethod
    def tostring(cls, val):
        for name,v in vars(cls).iteritems():
            if v==val:
                return name

""" This class tests the movement methods that are implemented in all the nodes"""
class TestRobotMoves(unittest.TestCase):
	rospy.init_node('testing_robot_moves', anonymous=False)
	rospy.Subscriber("robot_11/odom",Odometry,callback)
	
	"""Test move_to_method"""
	def test_move_to(self):
		# ensure that node starts from position 0
		self.assertEquals(int(data_from_callback.pose.pose.position.x), 0.0)
		
		# Test method
		commandX = weed.weed("robot_11", False)
		commandX.move_to(Point(4.0, 0.0, 0.0))
		
		# testing robot is in the correct position (allowing margin of error of <1)
		result = False
		if (data_from_callback.pose.pose.position.x > 3.5 ) & (data_from_callback.pose.pose.position.x < 4.5):
			result = True
		self.assertTrue(result)
		
	def test_move_to_backwards(self):
		# earliest position (4,0,0)
		# move robot backward to position (0,0,0)
		commandX = weed.weed("robot_11", False)
		commandX.move_to(Point(0.0, 0.0, 0.0))
		
		# testing robot is in the correct position (allowing margin of error of <1)
		result = False
		if (data_from_callback.pose.pose.position.x > -0.5 ) & (data_from_callback.pose.pose.position.x < 0.5):
			result = True
		self.assertTrue(result)
	
	"""Test move_x_steps_method with positive input"""
	def test_move_x_steps(self):
		#Starting position is (0,0,0)
		
		# move robot 3 meters to on the direction he is facing (negative)
		commandX = weed.weed("robot_11", False)
		commandX.move_x_steps(3)
		
		# testing robot is in the correct position (allowing margin of error of <1)
		result = False
		if (data_from_callback.pose.pose.position.x > -3.5 ) & (data_from_callback.pose.pose.position.x < -2.5):
			result = True
		self.assertTrue(result)
	
	"""Test move_x_steps_method with negative input"""	
	def test_move_x_steps_backward(self):
		#Starting position is (-3,0,0)
		# move robot 3 meters using the method
		commandX = weed.weed("robot_11", False)
		commandX.move_x_steps(-3)
		
		# testing robot is in the correct position (allowing margin of error of <1)
		result = False
		if (data_from_callback.pose.pose.position.x > -6.5 ) & (data_from_callback.pose.pose.position.x < -5.5):
			result = True
		self.assertTrue(result)

	"""	Test laser switches on and off successfully """
	def test_laser_switching(self):
            commandX = weed.weed("robot_11", False)
            self.assertEqual(commandX.laser_on, False)
            commandX.laser_on = True
            self.assertEqual(commandX.laser_on , True)

	"""	Test laser switches on and off successfully """
   	def test_change_velocity(self):
		commandX = weed.weed("robot_0", False)
        	twist = Twist()
        	twist.linear.x = 1.0
        	commandX.cmd_vel_pub.publish(twist)
        	commandX.wait(5)
        	self.assertEqual(commandX.twist.linear.x , 1.0)

	"""	Test turning left method """
	def test_turn_left(self):
		commandX = weed.weed("robot_0", False)
		self.assertEqual(commandX.face_value(commandX.rad_orient),Face.East)
		commandX.turnLeft()
		self.assertEqual(commandX.face_value(commandX.rad_orient),Face.North)
		
if __name__ == '__main__':
	import rostest
	rostest.rosrun(PKG, 'test_robot_moves', TestRobotMoves)
