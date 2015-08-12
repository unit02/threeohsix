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


class animal():
    def __init__(self, name):
	
        # node.__init__(self, "square", 1, 1, "red")

        rospy.loginfo("Starting node %s" % name)
        # Create new topic called laser to which it listens
        self.laser_sub = rospy.Subscriber(
            "/robot_2/base_scan",
            LaserScan,
            callback=self.laser_callback,
            queue_size=10
        )


        #self.laser_pub = rospy.Publisher(
         #   "sensor_output",
          #  LaserScan, queue_size=10
        #)
        self.cmd_vel_pub = rospy.Publisher(
            "/robot_2/cmd_vel",
            Twist,
            queue_size=10
        )

	self.randomMove()

	#Chooses a random number between 1 and 6 and either turns or changes speed
    def randomMove(self):

	twist_randmsg = Twist()
        threading.Timer(3.0, self.randomMove).start()
	random_action=randint(0,6)
		
	if (random_action==0):
		twist_randmsg.angular.z = 180
		self.cmd_vel_pub.publish(twist_randmsg)
			
			
	elif (random_action==1):
		twist_randmsg.angular.z = 90
		self.cmd_vel_pub.publish(twist_randmsg)
			
			
	elif (random_action==2):
		twist_randmsg.angular.z = 270
		self.cmd_vel_pub.publish(twist_randmsg)
			
			

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


# The block below will be executed when the python file is executed
# __name__ and __main__ are built-in python variables and need to start and end with *two* underscores
if __name__ == '__main__':
    rospy.init_node("animal1")  # Create a node of name laser_roomba
    l = animal(rospy.get_name())  # Create an instance of above class
    rospy.spin()  # Function to keep the node running until terminated via Ctrl+C
