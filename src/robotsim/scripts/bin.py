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
from geometry_msgs.msg import Vector3, Twist
import rospy
from nav_msgs.msg import Odometry
import roslib
roslib.load_manifest('robotsim')
from std_msgs.msg import String
from node import node
from robotsim.msg import bin_call,bin_detach,attach_bin, queue_position
import std_msgs
import sys
from geometry_msgs.msg import Point, Twist
from worldInfo import *

#Models the bin/buckets in which kiwifruit are stored
class bin(node):

    def __init__(self, name):
        super(bin, self).__init__(name, False)
        self.isFull = False
        self.following = None
        self.time_to_detach = None
        self.lowerYname = None
        self.lowerY = 0.0

        #Creates topic to publish to when it needs to be picked up by a carrier
        self.need_to_be_picker = rospy.Publisher(
            "/bin_info",
            bin_call,
            queue_size=10
        )
        #Creates topic to publish to when it needs to be picked up by a carrier
        self.whoToPickMe = rospy.Publisher(
            "/whichRobotToPick",
            String,
            queue_size=10
        )
        self.whosFirstInQ = rospy.Subscriber(
            "/firstInQ",
            queue_position,
            callback=self.handle_message,
            queue_size=19
        )

        self.attach_time = rospy.Subscriber(
                "/attach_bin",
                attach_bin,
                callback=self.attach_to_robot,
                queue_size=10
        )
    """ callbakc method form firstInQ topic, it searches for closest robot in q to come pick me up"""
    def handle_message(self, msg):
     
        #if this is the first message, assign me the first robot name
        if self.lowerYname is None:  
            self.lowerYname = msg.robot_name
            self.lowerY = msg.x_coordinate
            rospy.loginfo("first lowerY!" + self.lowerYname +str(msg.x_coordinate)+ str(self.lowerY))
      
        #if it is not my first message, compare and get the closest robot
        else:                        

            if self.lowerY < msg.x_coordinate:
                rospy.loginfo("before y coord!" + str(self.lowerY))
                self.lowerY = msg.x_coordinate
                self.lowerYname = msg.robot_name
                rospy.loginfo("first lowerY!" + self.lowerYname)
                rospy.loginfo("after y coord!" + str(self.lowerY))


    #Method called when it recieves a message from the robot to detach
    #Starts to publish the message asking to be picked up
    def stop_following(self,var):
        if var.unfollow:
            self.following.unregister()
            self.isFull = var.is_full
            rospy.loginfo("Sending message to be picked up!")
            # only call carrier when it is full
            if self.isFull:
                self.pick_me_up(self.position)


    # Method to make the bin follow a robot be matching the speed
    def move_with_robot(self,data):
        twist_msg = Twist()
        twist_msg = data.twist.twist
        if twist_msg.linear.x < 0:
            twist_msg.linear.x = -1 * twist_msg.linear.x
        if twist_msg.linear.y < 0:
            twist_msg.linear.y = -1 * twist_msg.linear.y
        # when facing north and south it considers the cmd_vel as y instead of x
        if twist_msg.linear.y > twist_msg.linear.x:
            twist_msg.linear.x = twist_msg.linear.y
            twist_msg.linear.y = 0.0
        self.cmd_vel_pub.publish(twist_msg)

    # Used to make the bin subscribe to the robot it's following's velocity and angle
    def attach_to_robot(self,msg):
        if msg.bin_name == self.name:
            rospy.loginfo("Attaching to %s", msg.to_attach_name)
            self.follow_robot(msg.to_attach_name)

    # Uses another robot's linear velocity, and publish it to its own cmd_vel
    def follow_robot(self, to_follow):
            self.robot_to_follow = to_follow
            self.following = rospy.Subscriber(
            to_follow + "/base_pose_ground_truth",
            Odometry,
            callback=self.move_with_robot,
            queue_size=1
        )
            self.time_to_detach = rospy.Subscriber(
            to_follow + "/detach",
            bin_detach,
            callback=self.stop_following,
            queue_size=1
        )

    #creates message to post to the bin_info topic
    def pick_me_up(self, bin_position):
        msg = bin_call()
        msg.bin_name = self.name
        msg.x_coordinate = bin_position.x
        msg.y_coordinate = bin_position.y
        msg.picker_to_attach_name = self.robot_to_follow
        self.need_to_be_picker.publish(msg)
        rospy.loginfo("BIN HEREEEEEEEEEEEEEEEEEE" +self.name)
        #self.wait(5)  #after publishing, give sometime to figure out which robot is closer to us
        #rospy.loginfo("!!!!!!!!!!!!!!robot name "+ self.lowerYname + str(self.lowerY))
        while self.lowerYname is None:
            pass
        self.wait(5)
        rospy.loginfo("!!!!!!!!!!!!!ROBOT NAMEEEEEEE "+ self.lowerYname +"  "+ str(self.lowerY))
        self.whoToPickMe.publish(self.lowerYname)


# The block below will be executed when the python file is executed
# __name__ and __main__ are built-in python variables and need to start and end with *two* underscores
if __name__ == '__main__':
    following_robot_name = int(sys.argv[1]) - worldInfo.numberOfPickers * 2

    rospy.init_node("robot_"+sys.argv[1])  # Create a node of name robot_2
    l = bin(rospy.get_name())  # Create an instance of above class
    l.follow_robot("robot_"+str(following_robot_name))
    l.robot_to_follow = "robot_"+str(following_robot_name)
    rospy.spin()  # Function to keep the node running until terminated via Ctrl+C

