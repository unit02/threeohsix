#!/usr/bin/env python
import unittest
import rospy
from geometry_msgs.msg import Point
import time
from node import node


class mock_rob(node):
    pass
	
"""
How to run the tests:
1) roscore
2) new terminal: caqtkin_make, source, rosrun robotsim mock_rob.py
"""	
class test_movement(unittest.TestCase):
 
    #tests if robot moves correctly on x-axis
    def test_moveX_to(self):
        rospy.loginfo(l.position)
        l.move_to(Point(5.0,0.0,0.0))
        l.position = Point(5.0,0.0,0.0)
        self.assertEqual(l.position, Point(5.0,0.0,0.0))

    #tests if robot moves correctly on y-axis
    def test_moveY_to(self):
        rospy.loginfo(l.position)
        l.move_to(Point(0.0,1.0,0.0))
        l.position = Point(0.0,1.0,0.0)
        self.assertEqual(l.position, Point(0.0,1.0,0.0))

    #tests if robot moves correctly x steps        
    def test_moveXMeters(self):
		l.move_x_steps(5)
		l.position = Point(5.0, 0.0, 0.0)
		self.assertEqual(l.position, Point(5.0,0.0,0.0))
	
    #tests if robot waits for a specific amount of time	
    def test_wait(self):
		currentTime = int(round(time.time()))		
		l.wait(2)
		newTime = int(round(time.time()))
		self.assertEqual(newTime, currentTime+2)

    #tests if robot follows another, still working on tests
    def test_follow(self):
		l.twist.linear.x =2
                l2.follow_robot	
                l2.twist.linear.x =2	
		self.assertEqual(l2.twist.linear.x, 2)



# The block below will be executed when the python file is executed
# __name__ and __main__ are built-in python variables and need to start and end with *two* underscores
if __name__ == '__main__':
    rospy.init_node("mockRob1")  
    l = mock_rob(rospy.get_name(), False)  # Create an instance of above class
    l2 = mock_rob(rospy.get_name(), False)  # Create an instance of above class
    unittest.main()
    rospy.spin()  # Function to keep the node running until terminated via Ctrl+C
    
    
