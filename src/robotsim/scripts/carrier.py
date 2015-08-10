#!/usr/bin/env python
import node.py

class carrier(node):

	def __init__(self):
		node.__init__(self, "square", 1,1, "red")


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



	
