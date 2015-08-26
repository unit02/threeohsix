#!/usr/bin/env python
class WorldInfo():
    MIN_ROWS = 3
    MIN_PICKER = 2
    def __init__(self):
	self.numberOfRows = 5
	self.numberOfPickers = 2
	self.maxPickers = 4
	self.rowWidth = 5
	self.numberOfCarriers = 2
	self.numberOfBins = 4
	self.lastTrunk = -8.5
	self.lastPargola = 0
	self.vertFence = 63.5
	self.pickerNormal = 2
	self.pickerRemainder = 0
	self.lastPickerName = "/robot_12"
	self.yTop = "34"
	self.yBottom = "-29.5"
	self.xRight = "50"
	self.xLeft = "-50"
worldInfo = WorldInfo()