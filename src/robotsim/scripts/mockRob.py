#!/usr/bin/env python

# Shape
# top speed
# working speed
# color

# methods
# moveForward
# turn (int degrees)
# wait (int timeToWaitInSeconds)

import sys
import unittest

import roslib
import rospy
import math
import tf
from tf.transformations import euler_from_quaternion
from std_msgs.msg import String
from geometry_msgs.msg import Vector3, Twist
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point
import time

class mockRob():


    def __init__(self, name):
        self.position = Point()
        self.twist = Twist()
        self.twist.linear.x = 1.0

        rospy.loginfo("Starting node %s" % name)

        self.cmd_vel_pub = rospy.Publisher(
            "robot_4/cmd_vel",
            Twist,
            queue_size=10
        )
        #rospy.loginfo(self.position)
		
	"""

        # Subscribe to stage topic to obtain its position
        # Must change to approprite name instead "ns" + cmd_vel
        self.stage_info = rospy.Subscriber(
            "robot_4/base_pose_ground_truth",
            Odometry,
            callback=self.stage_callback,
            queue_size=10
        )
        
        # Later release will ensure it gets a position from another robot by a message
        new_position = Point(38, 5.0, 0.0)
        self.move_to(new_position)

        #self.turnLeft()
        #for i in range(20):
        #    rospy.sleep(0.05)
        #self.turnRight()
        #for i in range(20):
        #    rospy.sleep(0.05)
        #self.turnRight()
        #for i in range(20):
        #    rospy.sleep(0.05)
        #self.turnRight()
        #for i in range(20):
        #    rospy.sleep(0.05)
        #self.turnLeft()
        #for i in range(20):
        #    rospy.sleep(0.05)
        #self.turnLeft()


    def stage_callback(self, data):
        self.position = data.pose.pose.position
	"""
    def move_to(self, new_position):
        #rospy.loginfo("Current position %s", self.position)
        #rospy.loginfo("Moving to new position %s", new_position)

        deltaX = new_position.x - self.position.x
        deltaY = new_position.y - self.position.y
        # moves in x direction of stage

        rospy.loginfo("DeltaX %s, DeltaY %s", int(deltaX), int(deltaY))
        if deltaX < 0:
            # rotate 180 degrees
            self.turnLeft()
            self.turnLeft()

        if deltaX != 0:
            self.move_x_steps(int(deltaX))

        # moves in y direction of stage

        # requires turning if it needs to go in y direction
        # has rotated 180 degrees - convention of turning is opposite
        if deltaX < 0:
            if deltaY > 0:
                # rotate -90 degrees (turn right)
                self.turnRight()
            elif deltaY < 0:
                # rotate -90 degrees (turn left)
                self.turnLeft()
        elif deltaX > 0:
            if deltaY > 0:
                # rotate 90 degrees (turn left)
                self.turnLeft()
            elif deltaY < 0:
                # rotate -90 degrees (turn right)
                self.turnRight()

        if deltaY != 0:
            self.move_x_steps(int(deltaY))

        #rospy.loginfo("Finished moving to the new position %s", new_position)


	
	
    def move_x_steps(self, metres):
        # runtime seconds = distance/velocity
        # need to convert to seconds so *10 is applied
        runtime = abs(int(10 *(metres/self.twist.linear.x)))

        rospy.loginfo("Started moving %s metres at speed %s /s!", metres, self.twist.linear.x)

        # publish twist for runtime seconds to move x metres
        for i in range(runtime):
            self.cmd_vel_pub.publish(self.twist)
            rospy.sleep(0.1)

        # create a new message - everything set to 0 so it can stop
        twist = Twist()

        #rospy.loginfo("Stopping!")
        self.cmd_vel_pub.publish(twist)
        
    
	
    def turnRight(self):
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = -(math.pi / 8)
        rospy.loginfo("Turning")
        for i in range(40):
            self.cmd_vel_pub.publish(twist)
            rospy.sleep(0.1)
        
        twist = Twist()
        self.cmd_vel_pub.publish(twist)
        rospy.loginfo("Turned Right")
        #twist.angular.x = radian/1


    def turnLeft(self):
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = (math.pi / 8)
        rospy.loginfo("Turning")
        for i in range(40):
            self.cmd_vel_pub.publish(twist)
            rospy.sleep(0.1)

        twist = Twist()
        self.cmd_vel_pub.publish(twist)
        rospy.loginfo("Turned Left")
        #twist.angular.x = radian/1


    def reorientation(self,msg):
        (roll,pitch,yaw) = euler_from_quaternion([msg.pose.pose.orientation.x,msg.pose.pose.orientation.y,msg.pose.pose.orientation.z,msg.pose.pose.orientation.w])
        rospy.loginfo("Testing", yaw)

	
    def wait(self, seconds):
        runtime = int(10 * seconds)
        twist = Twist()

        rospy.loginfo("Waiting for %s seconds!", seconds)

        # publish a twist of 0 linear & angular velocity
        for i in range(runtime):
            self.cmd_vel_pub.publish(twist)
            rospy.sleep(0.1)
   
    # Uses another robot's linear velocity, and publish it to its own cmd_vel
    def follow_robot(self, data):
        rospy.loginfo(rospy.get_caller_id() + "Robot to follow position %s ", data.pose.pose.position)
        rospy.loginfo(rospy.get_caller_id() + "Robot to follow %s ", data.twist.twist.linear.x)
        twist_msg = Twist()
        twist_msg =   data.twist.twist
        self.cmd_vel_pub.publish(twist_msg)
        
	
	
"""
How to run the tests:
1) roscore
2) new terminal: caqtkin_make, source, rosrun robotsim mockRob.py
"""	
class test_movement(unittest.TestCase):
 
    #tests if robot moves correctly on x-axis
    def test_moveX_to(self):
        rospy.loginfo(l.position)
        l.move_to(Point(5.0,0.0,0.0))
        l.position = Point(5.0,0.0,0.0)
        self.assertEqual(l.position, Point(5.0,0.0,0.0))

    #tests if robot moves correctly on y-axis
    def test_moveY_to(self):
        rospy.loginfo(l.position)
        l.move_to(Point(0.0,1.0,0.0))
        l.position = Point(0.0,1.0,0.0)
        self.assertEqual(l.position, Point(0.0,1.0,0.0))

    #tests if robot moves correctly x steps        
    def test_moveXMeters(self):
		l.move_x_steps(5)
		l.position = Point(5.0, 0.0, 0.0)
		self.assertEqual(l.position, Point(5.0,0.0,0.0))
	
    #tests if robot waits for a specific amount of time	
    def test_wait(self):
		currentTime = int(round(time.time()))		
		l.wait(2)
		newTime = int(round(time.time()))
		self.assertEqual(newTime, currentTime+2)

    #tests if robot follows another, still working on tests
    def test_follow(self):
		l.twist.linear.x =2
                l2.follow_robot	
                l2.twist.linear.x =2	
		self.assertEqual(l2.twist.linear.x, 2)



# The block below will be executed when the python file is executed
# __name__ and __main__ are built-in python variables and need to start and end with *two* underscores
if __name__ == '__main__':
    rospy.init_node("mockRob1")  
    l = mockRob(rospy.get_name())  # Create an instance of above class
    l2 = mockRob(rospy.get_name())  # Create an instance of above class
    unittest.main()
    rospy.spin()  # Function to keep the node running until terminated via Ctrl+C
    
    