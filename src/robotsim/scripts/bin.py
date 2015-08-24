#!/usr/bin/env python

from geometry_msgs.msg import Vector3, Twist
import rospy
from nav_msgs.msg import Odometry
import roslib
roslib.load_manifest('robotsim')
from std_msgs.msg import String
from node import node
from robotsim.msg import bin_call,bin_detach,attach_bin
import std_msgs
import sys
from geometry_msgs.msg import Point, Twist


class bin(node):


    def __init__(self, name):
        super(bin, self).__init__(name, False)
        self.isFull = False
        self.following = None
        self.time_to_detach = None

        #Used to get the bin's location to send to other robots
        #calls the method that creates and publishes the message
        # self.stage_info = rospy.Subscriber(
        #     self.name + "/base_pose_ground_truth",
        #     Odometry,
        #     callback=self.position_callback,
        #     queue_size=10
        # )
        #Creates topic to publish to
        self.need_to_be_picker = rospy.Publisher(
            "/bin_info",
            bin_call,
            queue_size=10
        )

    def stop_following(self,var):
        if var.unfollow == True:
            self.following.unregister()
            self.isFull = True
            rospy.loginfo("bin moving out of the rows")

            #self.move_to(self.position.x + 3, self.position.y,0.0)
            self.pick_me_up(self.position)
            self.attach_time = rospy.Subscriber(
                "/attach_bin",
                attach_bin,
                callback=self.attach_to_robot,
                queue_size=10
            )

    def move_with_robot(self,data):
         #rospy.loginfo(rospy.get_caller_id() + "Robot to follow position %s ", data.pose.pose.position)
        #rospy.loginfo(rospy.get_caller_id() + " Robot to follow linear velocity %s ", data.twist.twist)
        twist_msg = Twist()
        twist_msg =   data.twist.twist
        if twist_msg.linear.x < 0:
            twist_msg.linear.x = -1 * twist_msg.linear.x
        if twist_msg.linear.y < 0:
            twist_msg.linear.y = -1 * twist_msg.linear.y

        self.cmd_vel_pub.publish(twist_msg)

    def attach_to_robot(self,msg):
        if msg.bin_name == self.name:
            rospy.loginfo("Attaching to %s", msg.to_attach_name)
            self.follow_robot(msg.to_attach_name)

    # Uses another robot's linear velocity, and publish it to its own cmd_vel
    def follow_robot(self, to_follow):

            self.following = rospy.Subscriber(
            to_follow + "/base_pose_ground_truth",
            Odometry,
            callback=self.move_with_robot,
            queue_size=10
        )
            self.time_to_detach = rospy.Subscriber(
            to_follow + "/detach",
            bin_detach,
            callback=self.stop_following,
            queue_size=10
        )



    #creates message to post to the bin_info topic
    def pick_me_up(self, bin_position):
        #if self.isFull == True:
        rospy.loginfo("Sending message to be picked up!")
        msg = bin_call()
        msg.bin_name = self.name
        msg.x_coordinate = bin_position.x
        msg.y_coordinate = bin_position.y
        self.need_to_be_picker.publish(msg)


# The block below will be executed when the python file is executed
# __name__ and __main__ are built-in python variables and need to start and end with *two* underscores
if __name__ == '__main__':
    rospy.init_node("robot_"+sys.argv[1])  # Create a node of name robot_2
    l = bin(rospy.get_name())  # Create an instance of above class
    l.follow_robot("robot_"+str(int(sys.argv[1])-4))
    rospy.spin()  # Function to keep the node running until terminated via Ctrl+C

