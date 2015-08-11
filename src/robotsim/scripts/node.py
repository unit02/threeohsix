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
import math
from std_msgs.msg import String
from geometry_msgs.msg import Vector3, Twist
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point


class node():


    def __init__(self, name):
        self.position = Point()
        self.twist = Twist()
        self.twist.linear.x = 1.0

        rospy.loginfo("Starting node %s" % name)

        self.cmd_vel_pub = rospy.Publisher(
            "cmd_vel",
            Twist,
            queue_size=10
        )


        # Subscribe to stage topic to obtain its position
        # Must change to approprite name instead "ns" + cmd_vel
        self.stage_info = rospy.Subscriber(
            "robot_4/base_pose_ground_truth",
            Odometry,
            callback=self.stage_callback,
            queue_size=10
        )

        self.wait(5)

        
        # Later release will ensure it gets a position from another robot by a message
        new_position = Point(-34.5, -5.5, 0.0)
        self.move_to(new_position)
        #self.turnLeft()


    def stage_callback(self, data):
        self.position = data.pose.pose.position

    def laser_calback(self,msg):
            ranges = msg.ranges
            rospy.loginfo(ranges)

    def move_to(self, new_position):
        self.move_x_steps(10)
        rospy.loginfo("Current position %s", self.position)
        rospy.loginfo("Moving to new position %s", new_position)


        deltaX = new_position.x - self.position.x
        deltaY = new_position.y - self.position.y

        rospy.loginfo("DeltaX %s, DeltaY %s", deltaX, deltaY)
        if deltaX < 0:
            # rotate 180 degrees
            pass
        self.move_x_steps(deltaX)

        # requires turning if it needs to go in y direction
        # has rotated 180 degrees - convention of turning is opposite
        if deltaX < 0:
            if deltaY < 0:
                # rotate -90 degrees (turn right)
                pass
            elif deltaY > 0:
                # rotate -90 degrees (turn left)
                pass
        elif deltaX > 0:
            # rotate -90 degrees (turn left)
            if deltaY < 0:
                # rotate 90 degrees (turn left)
                pass
            elif deltaY > 0:
                # rotate -90 degrees (turn right)
                pass
        self.move_x_steps(deltaY)


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

    def turnLeft(self):
        self.twist = Twist()
        self.twist.linear.x = 1.0
        self.twist.angular.z = -(math.pi/2)
        rospy.loginfo("Turning")
        for i in range(20):
            self.cmd_vel_pub.publish(self.twist)
            rospy.sleep(0.05)
        
        self.twist = Twist()
        self.twist.linear.x = 1.0
        self.twist.angular.z = 0.0
        self.cmd_vel_pub.publish(self.twist)
        rospy.loginfo("Straight")
        #twist.angular.x = radian/1


    def turnRight(self):
        self.twist = Twist()
        self.twist.linear.x = 1.0
        self.twist.angular.z = (math.pi/2)
        rospy.loginfo("Turning")
        for i in range(20):
            self.cmd_vel_pub.publish(self.twist)
            rospy.sleep(0.05)
        
        self.twist = Twist()
        self.twist.linear.x = 1.0
        self.twist.angular.z = 0.0
        self.cmd_vel_pub.publish(self.twist)
        rospy.loginfo("Straight")
        #twist.angular.x = radian/1



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
    rospy.init_node("node1")  # Create a node of name laser_roomba
    l = node(rospy.get_name())  # Create an instance of above class
    rospy.spin()  # Function to keep the node running until terminated via Ctrl+C
