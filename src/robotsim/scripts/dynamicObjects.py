# Shape
# top speed
# working speed
# color

# methods
# moveForward
# turn (int degrees)
# wait (int timeToWaitInSeconds)


#!/usr/bin/env python


from std_msgs.msg import String
import roslib
import rospy
from geometry_msgs.msg import Vector3, Twist


class dynamicObjects(object):
	def __init__(self,shape,topSpeed,workingSpeed,color):
        self.shape = shape
	self.topSpeed = topSpeed
	self.workingSpeed = workingSpeed
	self.color = color

	def move():
	twist = Twist()
	twist.linear.x = 1
	

	def turn(radian):
	twist = Twist()
#angular is radians/sec
	twist.angular.x = radian/1


	def wait(seconds):


