#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import numpy as np
from random import choice, randint
import node
from sensor_msgs.msg import Range
from random import randint 
from time import sleep
import threading
import roslib
import rospy
import math
import tf
from tf.transformations import euler_from_quaternion
from std_msgs.msg import String
from geometry_msgs.msg import Vector3, Twist
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point

class person():
    def __init__(self, name):
	self.position = Point()
        self.twist = Twist()
        self.twist.linear.x = 1.0
        # node.__init__(self, "square", 1, 1, "red")

        rospy.loginfo("Starting node %s" % name)
        # Create new topic called laser to which it listens
        self.laser_sub = rospy.Subscriber(
            "/robot_3/base_scan",
            LaserScan,
            callback=self.laser_callback,
            queue_size=10
        )


        #self.laser_pub = rospy.Publisher(
         #   "sensor_output",
          #  LaserScan, queue_size=10
        #)
        self.cmd_vel_pub = rospy.Publisher(
            "/robot_3/cmd_vel",
            Twist,
            queue_size=10
        )


	self.move_x_steps(10)
        self.turnRight()
	#for i in range(25):
            #rospy.sleep(0.05)		
			

	# called when new message arrives from laser topic
    def laser_callback(self,msg):
            #Get the ranges of the laser scan and find the minimum
            ranges = msg.ranges
            #rospy.loginfo(ranges)
            min_distance = np.nanmin(ranges)
            #rospy.loginfo("Minimum distance: %f" % min_distance)
            twist_msg = Twist()
            rate = rospy.Rate(10)
            #Avoid obstacles that were detected within 3m ahead
            if (min_distance <= 3):
                #Recognise the turning direction, given that laser beam is 60 degrees wide
                if (ranges.index(min_distance) <=30):
					#rospy.loginfo(ranges.index(min_distance))	
					#now = rospy.Time.now().to_sec()
					#end_time = now + 5
					#angle_velocity = 100
					#while end_time != now:
					#rospy.loginfo(end_time)
					#rospy.loginfo(now)
					twist_msg.linear.x = 1
					twist_msg.angular.z = 1
					self.cmd_vel_pub.publish(twist_msg)
                else:
					#rospy.loginfo(ranges.index(min_distance))
					#now = rospy.Time.now().to_sec()
					#end_time = now + 5
					#angle_velocity = 100
					#while end_time != now:
					twist_msg.linear.x = 1
					twist_msg.angular.z = -1
					self.cmd_vel_pub.publish(twist_msg)
            else:
                #Moving straight
            	twist_msg.linear.x = 1
            	twist_msg.angular.z = 0
            	self.cmd_vel_pub.publish(twist_msg)
            rate.sleep()

    def move_to(self, new_position):
        rospy.loginfo("Current position %s", self.position)
        rospy.loginfo("Moving to new position %s", new_position)

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

        rospy.loginfo("Finished moving to the new position %s", new_position)



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

        rospy.loginfo("Stopping!")
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




# The block below will be executed when the python file is executed
# __name__ and __main__ are built-in python variables and need to start and end with *two* underscores
if __name__ == '__main__':
    rospy.init_node("person1")  # Create a node of name laser_roomba
    l = person(rospy.get_name())  # Create an instance of above class
    rospy.spin()  # Function to keep the node running until terminated via Ctrl+C