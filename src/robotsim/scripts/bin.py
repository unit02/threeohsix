#!/usr/bin/env python

from geometry_msgs.msg import Vector3, Twist
import rospy
from nav_msgs.msg import Odometry
from node import node


class bin(node):


    def __init__(self, name, to_follow):
        super(bin, self).__init__(name, False)

        # Subscribes to robot_4's stage information to follow
        # Must change to approprite name instead
        self.follow_robot = rospy.Subscriber(
            to_follow + "/base_pose_ground_truth",
            Odometry,
            callback=self.follow_robot,
            queue_size=10
        )

    # Uses another robot's linear velocity, and publish it to its own cmd_vel
    def follow_robot(self, data):
        rospy.loginfo(rospy.get_caller_id() + "Robot to follow position %s ", data.pose.pose.position)
        rospy.loginfo(rospy.get_caller_id() + "Robot to follow %s ", data.twist.twist.linear.x)
        twist_msg = Twist()
        twist_msg =   data.twist.twist
        self.cmd_vel_pub.publish(twist_msg)

# The block below will be executed when the python file is executed
# __name__ and __main__ are built-in python variables and need to start and end with *two* underscores
if __name__ == '__main__':
    rospy.init_node("robot_2")  # Create a node of name
    l = bin(rospy.get_name(), "robot_1")  # Create an instance of above class
    rospy.spin()  # Function to keep the node running until terminated via Ctrl+C

