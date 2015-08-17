#!/usr/bin/env python
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



	
