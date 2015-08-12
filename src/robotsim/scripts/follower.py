#!/usr/bin/env python

from geometry_msgs.msg import Vector3, Twist
import rospy
from nav_msgs.msg import Odometry

class follower():

    # Uses another robot's linear velocity, and publish it to its own cmd_vel
    def follow_robot(self, data):
        rospy.loginfo(rospy.get_caller_id() + "Robot to follow position %s ", data.pose.pose.position)
        rospy.loginfo(rospy.get_caller_id() + "Robot to follow %s ", data.twist.twist.linear.x)
        twist_msg = Twist()
        twist_msg.linear.x =  data.twist.twist.linear.x
        self.cmd_vel_pub.publish(twist_msg)

    def __init__(self, name):
        rospy.loginfo("Starting node %s" % name)

        # publish its velocity to its namespace + cmd_vel
        # must change at a later state - doesnt work with just cmd_vel
        self.cmd_vel_pub = rospy.Publisher(
            "robot_5/cmd_vel",
            Twist,
            queue_size=10
        )

        # Subscribes to robot_4's stage information to follow
        # Must change to approprite name instead
        self.follow_robot = rospy.Subscriber(
            "robot_4/base_pose_ground_truth",
            Odometry,
            callback=self.follow_robot,
            queue_size=10
        )

# The block below will be executed when the python file is executed
# __name__ and __main__ are built-in python variables and need to start and end with *two* underscores
if __name__ == '__main__':
    rospy.init_node("follower1")  # Create a node of name
    l = follower(rospy.get_name())  # Create an instance of above class
    rospy.spin()  # Function to keep the node running until terminated via Ctrl+C

