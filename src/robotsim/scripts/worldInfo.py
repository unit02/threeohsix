#!/usr/bin/env python
class WorldInfo():
    MIN_ROWS = 3
    MIN_PICKER = 2
    def __init__(self):
	self.numberOfRows = 11
	self.numberOfPickers = 3
	self.maxPickers = 10
	self.rowWidth = 5
	self.numberOfCarriers = 3
	self.numberOfBins = 6
	self.numberOfWeeds = 10
	self.lastTrunk = -41.5
	self.lastPargola = 0
	self.vertFence = 96.5
	self.pickerNormal = 3
	self.pickerRemainder = 1
	self.lastPickerName = "/robot_13"
	self.yTop = "34"
	self.yBottom = "-62.5"
	self.xRight = "50"
	self.xLeft = "-50"
worldInfo = WorldInfo()