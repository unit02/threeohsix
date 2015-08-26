#!/usr/bin/env python
PKG = 'robotsim' # put in your own package name
#import moveRobot

import node
import test_node
import weed
import rospy
import unittest
from geometry_msgs.msg import Point

# to perform the test we'll read odometry from stage
from nav_msgs.msg import Odometry

data_from_callback = Odometry()

def callback(data):
    global data_from_callback
    data_from_callback = data

""" This class tests the movement methods that are implemented in all the nodes"""
class TestRobotMoves(unittest.TestCase):
    rospy.init_node('testing_robot_moves', anonymous=True)
    rospy.Subscriber("robot_11/odom",Odometry,callback)
	
    """Test move_to_method"""
    def test_move_to(self):
        # ensure that node starts from position 0
        self.assertEquals(int(data_from_callback.pose.pose.position.x), 0.0)
        # move robot to position (4,0,0)
        commandX = weed.weed("robot_11", False)
        commandX.move_to(Point(4.0, 0.0, 0.0))
        # testing robot is in the correct position
        self.assertEquals(int(data_from_callback.pose.pose.position.x), 4.0)

    def test_move_to_backwards(self):
        # ensure that node starts from the earliest position (4,0,0)
        self.assertEquals(int(data_from_callback.pose.pose.position.x), 4.0)
        # move robot backward to position (-4,0,0)
        commandX = weed.weed("robot_11", False)
        commandX.move_to(Point(-4.0, 0.0, 0.0))
        # testing robot is in the correct position
        self.assertEquals(int(data_from_callback.pose.pose.position.x), -4.0)


    # def move_x_steps(self):
    #     # ensure that node starts from position 0
    #     self.assertEquals(int(data_from_callback.pose.pose.position.x), 0.0)
    #     # move robot 5 meters using the method
    #     commandX = weed.weed("robot_19", False)
    #     commandX.move_x_steps(5)
    #     # testing robot is in the correct position
    #     self.assertEquals(int(data_from_callback.pose.pose.position.x), 5.0)
    #     #self.assertEquals(int(data_from_callback.pose.pose.position.y), 0.0)
		# #self.assertEquals(int(data_from_callback.pose.pose.position.z), 0.0)

if __name__ == '__main__':
    import rostest
    rostest.rosrun(PKG, 'test_robot_moves', TestRobotMoves)
