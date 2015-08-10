#!/usr/bin/env python
# references used: http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point
from math import atan2, degrees, pi
from geometry_msgs.msg import Twist


a = Point()
b = Point()


def mypostion(data):
    rospy.loginfo(rospy.get_caller_id() + "robot_2 position stationary %s", data.pose.pose.position)
    global a
    a = data.pose.pose.position

def otherpostion(data):
    rospy.loginfo(rospy.get_caller_id() + "robot_3 position %s", data.pose.pose.position)
    global b
    b = data.pose.pose.position

def rotate():
    deltaX = a.x - b.x
    deltaY = a.y - b.y
    rads = atan2(-deltaX, deltaY)



def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'talker' node so that multiple talkers can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)


    rospy.Subscriber("robot_2/base_pose_ground_truth", Odometry, mypostion)

    rospy.Subscriber("robot_3/base_pose_ground_truth", Odometry, otherpostion)

    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    rate = rospy.Rate(10) # 10hz

    twist = Twist()
    twist.linear.x = 1.0
    distanceX = abs(abs(a.x)-abs(b.x))

 

    for i in range(100):
        pub.publish(twist)
        rospy.sleep(0.1) # 30*0.1 = 3.0 seconds

    # create a new message
    twist = Twist()

    # note: everything defaults to 0 in twist, if we don't fill it in, we stop!
    rospy.loginfo("Stopping!")
    pub.publish(twist)
#on from exiting until this node is stopped
    rospy.spin()

 # this quick check means that the following code runs ONLY if this is the
 # main file -- if we "import move" in another file, this code will not execute.
if __name__ == '__main__':
    listener()
