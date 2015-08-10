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

 def __init__(self,name,type,color):
  self.name = name
  self.type = type
  self.color = color

  if type == carrier:
   workingSpeed = 1.5
   topSpeed = 3.0
  elif type == picker:
   workingSpeed = 0.01
   topSpeed =  0.5
  elif type == bin:
   carrierSpeed = 1.5
   pickerSpeed = 0.01
  else :
   speed = 0.5


 def getType(self):
  return self.type

 def getName(self):
  return self.name

  def getColor(self):
  return self.color

def move(self):
 twist = Twist()
 twist.linear.x = 1


def turn(radian):
 twist = Twist()
#angular is radians/sec
twist.angular.x = radian/1


#def wait(seconds):



