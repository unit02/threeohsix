#!/usr/bin/env python

# Shape
# top speed
# working speed
# color

# methods
# moveForward
# turn (int degrees)
# wait (int timeToWaitInSeconds)

import roslib
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Vector3, Twist
from nav_msgs.msg import Odometry



class node(object):


	def __init__(self,shape,topSpeed,workingSpeed,color):
		self.shape = shape
		self.topSpeed = topSpeed
		self.workingSpeed = workingSpeed
		self.color = color



	def move(self):
		twist = Twist()
		twist.linear.x = 1

	def turn(self, radian):
		twist = Twist()
		#angular is radians/sec
		twist.angular.x = radian/1

	def wait(self, seconds):
		pass