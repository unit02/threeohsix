#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point
from havesting_robot import havesting_robot


class carrier(havesting_robot):

	def updateBin (self):
		#every 1 second picker "pick"s kiwifruit
		#sends signal to nearest carrier to updateBin()
		pass

	def leaveBin(self):
	# occurs at end of the row
		pass

	def retrieveNewBin(self):
	# after bin is left, the carrier gets a new bin
		pass

	def followPicker(self):
	# after reciving the signal from the picker, begins to follow it. use tutlebot follower as a beginning on how to do this
		pass

if __name__ == '__main__':
    rospy.init_node("robot_4")  # Create a node of name laser_roomba
    l = carrier(rospy.get_name(),"carrier", False)  # Create an instance of above class
    rospy.spin()  # Function to keep the node running until terminated via Ctrl+C


	
