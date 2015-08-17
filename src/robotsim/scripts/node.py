#!/usr/bin/env python

# Shape
# top speed
# working speed
# color

# methods
# moveForward
# turn (int degrees)
# wait (int timeToWaitInSeconds)

import rospy
import math
from tf.transformations import euler_from_quaternion
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Twist
import numpy as np
from sensor_msgs.msg import LaserScan

class node(object):


    def __init__(self, name, laser_on):
        self.position = Point()
        self.twist = Twist()
        self.twist.linear.x = 1.0
        self.name = name
        self.laser_on = laser_on

        rospy.loginfo("Starting node %s" % name)

        self.cmd_vel_pub = rospy.Publisher(
            self.name + "/cmd_vel",
            Twist,
            queue_size=10
        )
        if laser_on:
        # Create new topic called laser to which it listens
            self.laser_sub = rospy.Subscriber(
                self.name + "/base_scan",
                LaserScan,
                callback=self.laser_callback,
                queue_size=10
            )

        # Subscribe to stage topic to obtain its position
        # Must change to approprite name instead "ns" + cmd_vel
        self.stage_info = rospy.Subscriber(
            self.name + "/base_pose_ground_truth",
            Odometry,
            callback=self.stage_callback,
            queue_size=10
        )

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

    def stage_callback(self, data):
        self.position = data.pose.pose.position

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

    def reorientation(self,msg):
        (roll,pitch,yaw) = euler_from_quaternion([msg.pose.pose.orientation.x,
                                                  msg.pose.pose.orientation.y,
                                                  msg.pose.pose.orientation.z,msg.
                                                 pose.pose.orientation.w])
        rospy.loginfo("Testing", yaw)

    def wait(self, seconds):
        runtime = int(10 * seconds)
        twist = Twist()

        rospy.loginfo("Waiting for %s seconds!", seconds)

        # publish a twist of 0 linear & angular velocity
        for i in range(runtime):
            self.cmd_vel_pub.publish(twist)
            rospy.sleep(0.1)

        rospy.loginfo("Awake!")



# The block below will be executed when the python file is executed
# __name__ and __main__ are built-in python variables and need to start and end with *two* underscores
if __name__ == '__main__':
    rospy.init_node("robot_4")  # Create a node of name laser_roomba
    l = node(rospy.get_name(), False)  # Create an instance of above class
    l.wait(5)
    new_position = Point(38, 5.0, 0.0)
    l.move_to(new_position)
    rospy.spin()  # Function to keep the node running until terminated via Ctrl+C
