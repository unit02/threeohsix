#!/usr/bin/env python
import worldConfig
import os
import wx
import sys


class ConfigFrame(wx.Frame) :


	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(400,200))
		panel = wx.Panel(self)
		

		#Getting Number of Rows
		self.quote = wx.StaticText(panel, label="Number of Rows: ", pos=(20, 30))
		self.quote = wx.StaticText(panel, label="(Min: 3 Rows, Max: 20 Rows)", pos=(20, 45))
		self.rowInput = wx.TextCtrl(panel, -1, "5", size=(50, -1), pos=(220, 25) )
        	self.rowInput.SetInsertionPoint(0)

		#Getting number of Pickers
		self.quote = wx.StaticText(panel, label="Number of Picker Robots: ", pos=(20, 70))
		self.quote = wx.StaticText(panel, label="(Min: 2 Pickers)", pos=(20, 85))
		self.quote = wx.StaticText(panel, label="(Cannot have more rows than Pickers)", pos=(20, 100))
		self.pickerInput = wx.TextCtrl(panel, -1, "2", size=(50, -1), pos=(220, 65) )
        	self.pickerInput.SetInsertionPoint(0)

		#Getting width of rows
		self.quote = wx.StaticText(panel, label="Width of Rows: ", pos=(20, 130))
		self.quote = wx.StaticText(panel, label="(Min: 5 metres) ", pos=(20, 145))
		self.rowWidthInput = wx.TextCtrl(panel, -1, "5", size=(50, -1), pos=(220, 125) )
        	self.rowWidthInput.SetInsertionPoint(0)


		#Button to set the config
		self.saveButton = wx.Button(panel, id=-1, label='Save Orchard!', pos=(220, 165), size=(175, 28))
                self.saveButton.Bind(wx.EVT_BUTTON, self.buttonClick)
		self.Show(True)

	def buttonClick(self,event):

		errorRow=0
		errorPicker=0
		errorWidth=0
		
		world=worldConfig.WorldConfig()
		if (int(self.rowInput.GetValue()) > 2 ) & (int(self.rowInput.GetValue()) < 21 ) :
			world.numberOfRows=int(self.rowInput.GetValue())
			errorRow=0
		else :
			print "Invalid Row value. Please try again"
			errorRow=1
		if (int(self.pickerInput.GetValue()) > 1 ) & (int(self.pickerInput.GetValue()) < int(self.rowInput.GetValue()) ) :
			world.numberOfPickers=int(self.pickerInput.GetValue())
			errorPicker=0
		else :
			print "Invalid number of Pickers. Please try again."
			errorPicker=1
		if (int(self.rowWidthInput.GetValue())) > 4 :
			world.rowWidth=float(self.rowWidthInput.GetValue())
			errorWidth=0
		else :
			print "Invalid row width. Please try again"
			errorWidth=1

		if ((errorRow == 0) & (errorPicker == 0) & (errorWidth == 0)) :
 
			world.setup()
			sys.exit()
			



app = wx.App(False)  
frame = ConfigFrame(None, "Orchard Configuration")
app.MainLoop()

