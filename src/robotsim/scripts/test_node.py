#!/usr/bin/env python
import unittest
import rospy
from geometry_msgs.msg import Point
import time
from node import node
from node import Face


class mock_rob(node):
    pass
	
"""
How to run the tests:
1) roscore
2) new terminal: catkin_make, source it, then: rosrun robotsim mock_rob.py
"""	
class test_node(unittest.TestCase):

    """The following tests sets are testing that robot can identify
    which direction he is facing.
    They test the method face_value(rad_orient)
    input: the robot's orientation in radians
    output: integer between 0-3,
    where 0 = North, 1 = south, 2 = East, 3 = West"""
    def test_north(self):
        self.assertEqual(l.face_value(0.9), 0)

    def test_south(self):
        self.assertEqual(l.face_value(-1.5), 1)

    def test_east(self):
        self.assertEqual(l.face_value(0.3), 2)

    def test_west(self):
        self.assertEqual(l.face_value(-3.0), 3)
	
    #tests if robot waits for a specific amount of time	
    def test_wait(self):
		currentTime = int(round(time.time()))		
		l.wait(2)
		newTime = int(round(time.time()))
		self.assertEqual(newTime, currentTime+2)


# The block below will be executed when the python file is executed
# __name__ and __main__ are built-in python variables and need to start and end with *two* underscores
if __name__ == '__main__':
    rospy.init_node("mockRob1")  
    l = mock_rob(rospy.get_name(), False)  # Create an instance of above class
    unittest.main()
    rospy.spin()  # Function to keep the node running until terminated via Ctrl+C
