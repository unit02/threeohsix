#!/usr/bin/env python
# references used: http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry



def mypostion(data):
    rospy.loginfo(rospy.get_caller_id() + "robot_0 position %s", data.pose.pose.position)

def otherpostion(data):
    rospy.loginfo(rospy.get_caller_id() + "robot_1 position %s", data.pose.pose.position)



def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'talker' node so that multiple talkers can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)


    rospy.Subscriber("robot_0/base_pose_ground_truth", Odometry, mypostion)

    rospy.Subscriber("robot_1/base_pose_ground_truth", Odometry, otherpostion)


# spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
