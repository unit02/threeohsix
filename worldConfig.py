#!/usr/bin/env python
from random import randint
import os
import wx


class WorldConfig():

    MIN_ROWS = 3
    MIN_PICKER = 2
    

    def __init__(self):
    
        self.numberOfRows = 3
        self.numberOfPickers =  2
        self.maxPickers = self.numberOfRows - 1
        self.rowWidth = 3.5
        self.numberOfCarriers = 1
        self.numberOfBins = 4
        self.numberOfWeeds = 10
        self.lastTrunk = 13.5 
        self.lastPargola = 0
        self.vertFence = 0
        self.pickerNormal = 0
        self.pickerRemainder = 0
        self.lastPickerName = ""
        self.yTop = 34
        self.yBottom = -34
        self.xRight = 50
        self.xLeft = -50
        self.home = os.getenv("HOME");
        
        

    def setup(self):
	self.getNumberOfRows(self.numberOfRows)
        self.getNumberOfPickers(self.numberOfPickers)
        self.getRowWidth(self.rowWidth)
        self.getNumberOfCarriers()
        self.getNumberOfBins()
        self.setGround()
        self.makeOrchard()
        self.makeOneExecutableWindow()
        self.makeWorld()
        self.createWorldInfo()
        self.makeLaunch()
        self.makeBash()


    '''This method sets the number of rows for the simulation'''
    def getNumberOfRows(self, input):    

	
        accepted = 0
        while (accepted == 0):
            self.numberOfRows = input #get input from user - number of rows 
            if (input > 2 ) & (input < 21): #checking minimum and maximum
                accepted = 1
            
       
        self.maxPickers = int(self.numberOfRows) - 1
        return self.numberOfRows

    '''This method sets the number of pickers for the simulation'''
    def getNumberOfPickers(self, input):    

	
        accepted = 0
        while (accepted == 0):
            self.numberOfPickers = input  #get input from user - number of pickers 
            if (self.numberOfPickers > 1 ) & (self.numberOfPickers <= self.maxPickers): #checking minimum and maximum
                accepted = 1
            
        return self.numberOfPickers
    
    '''This method sets the row width for the simulation'''
    def getRowWidth(self, input):    

	
        accepted = 0
        while (accepted == 0):
            self.rowWidth = input  #get input from user - row width
            if (self.rowWidth > 4 ): #checking minimum 
                accepted = 1
        
        return self.rowWidth
    
    '''This method sets the number of carriers for the simulation'''
    def getNumberOfCarriers(self):    

        #number of carriers is the same as number of pickers
        self.numberOfCarriers = int(self.numberOfPickers) 

        return int(self.numberOfCarriers)

    '''This method sets the number of bins for the simulation'''
    def getNumberOfBins(self): 

        #number of bins is the twice the number of pickers
        self.numberOfBins = int(self.numberOfPickers) * 2

        return int(self.numberOfBins)
    
    '''This method changes the dimensions of the ground/orchard according to number of rows the user wants'''
    def setGround(self):

        #open ground.inc
        f = open(str(self.home) +'/threeohsix/src/robotsim/world/ground.inc', 'w')


        #horizontal fence model
        f.write('define fenceHorizontal model( \n')
        f.write('\tgui_move 0 \n')
 	f.write('\tcolor "yellow"\n ')
 	f.write('\tsize [101 1 2.5] \n')	
	f.write('\tblock( \n')
	f.write('\tpoints 4 \n')
	f.write('\tpoint[0] [0 0]\n ')
	f.write('\tpoint[1] [1 0]\n ')
	f.write('\tpoint[2] [1 1] \n')
	f.write('\tpoint[3] [0 1]\n')
	f.write('\tz [0 1] )\n)\n')

        #calculate the length of the vertical fence
        self.vertFence = float(self.rowWidth * (self.numberOfRows -1)) + float((0.5 * self.numberOfRows)) + 41 

        #vertical fence model
        f.write('define fenceVertical model( \n')
        f.write('\tgui_move 0 \n')
 	f.write('\tcolor "yellow"  \n')
 	f.write('\tsize [1 '+ str(self.vertFence + 1) +' 2.5]  \n')	
	f.write('\tblock(  \n')
	f.write('\tpoints 4  \n') 
	f.write('\tpoint[0] [0 0]  \n')
	f.write('\tpoint[1] [1 0]  \n')
	f.write('\tpoint[2] [1 1]  \n')
	f.write('\tpoint[3] [0 1] \n')
	f.write('z [0 1] ) \n)\n')
       
        #ground model
        f.write('define ground model \n')
        f.write('( \n')
        f.write('\tgui_move 0 \n')
        f.write('\tsize [100 '+ str(self.vertFence) +' 0.01] \n')
        f.write('\tcolor "YellowGreen"  \n') 
        f.write('\tblock \n')
        f.write('( \n')
        f.write('\tpoints [4] \n')
        f.write('\tpoint[0] [0 0] \n')
        f.write('\tpoint[1] [0 1] \n')
        f.write('\tpoint[2] [1 1] \n')
        f.write('\tpoint[3] [1 0] \n')
        f.write('\tz [0 0.5])\n)\n')

        #pergola model
        f.write('define pergola model\n')
        f.write('(\n')
        f.write('\tgui_move 0 \n')
        f.write('\tsize [1.7 '+ str(self.rowWidth - 0.5) +' 0.5]\n')
        f.write('\tcolor "DarkGreen"  \n')
        f.write('\tblock\n')
        f.write('(\n')
        f.write(' \tpoints [4]\n')
        f.write('\tpoint[0] [0 0]\n')
        f.write(' \tpoint[1] [0.5 0]\n')
        f.write('\tpoint[2] [0.5 3.5]\n')
        f.write(' \tpoint[3] [0 3.5]\n')
        f.write(' \tz [0 0.5]\n')
        f.write(')\n')
        f.write('\tblock\n')
        f.write(' (\n')
        f.write(' \tpoints [4]\n')
        f.write(' \tpoint[0] [0.5 0.2]\n')
        f.write(' \tpoint[1] [0.9 0.2]\n')
        f.write('\t point[2] [0.9 3.3]\n')
        f.write(' \tpoint[3] [0.5 3.3]\n')
        f.write(' \tz [0 0.5]\n')
        f.write(' )\n')
        f.write('\t block\n')
        f.write(' (\n')
        f.write('\tpoints [4]\n')
        f.write(' \tpoint[0] [0.9 0.4]\n')
        f.write(' \tpoint[1] [1.1 0.4]\n')
        f.write(' \tpoint[2] [1.1 3.1]\n')
        f.write(' \tpoint[3] [0.9 3.1]\n')
        f.write(' \tz [0 0.5]\n')
        f.write(')\n')
        f.write('\t  block\n')
        f.write('(\n')
        f.write('\t points [4]\n')
        f.write(' \tpoint[0] [-0.4 0.2]\n')
        f.write('\t point[1] [0 0.2]\n')
        f.write(' \tpoint[2] [0 3.3]\n')
        f.write(' \tpoint[3] [-0.4 3.3]\n')
        f.write(' \tz [0 0.5]\n')
        f.write(' )\n')
        f.write('\tblock\n')
        f.write(' (\n')
        f.write('\t points [4]\n')
        f.write(' \tpoint[0] [-0.4 0.4]\n')
        f.write('\tpoint[1] [-0.6  0.4]\n')
        f.write('\t point[2] [-0.6  3.1]\n')
        f.write(' \tpoint[3] [-0.4 3.1]\n')
        f.write(' \tz [0 0.5]\n')
        f.write(')\n')
        f.write(')\n')

        #close ground.inc
        f.close()

    '''This method makes the static orchard'''
    def makeOrchard(self):


        #open instances.inc
        f = open(str(self.home) +'/threeohsix/src/robotsim/world/instances.inc', 'w')

        #calculate y bottom - the y co-ordinate of the horizontal fence
        self.yBottom = (self.vertFence * -1 + 34)

        f.write('include "myblock.inc" \n') 
        f.write('include "ground.inc" \n') 

        #add ground instance
        f.write('ground( pose [ 0 '+ str(self.vertFence * 0.5 * -1 + 34) +' 0 0] ) \n')
        #add driveway instance
        f.write('driveway( pose [ -34.67 28.51 0 0] ) \n') 
        
        #add horizontal fence instances
        f.write('fenceHorizontal( pose [ 0 34 0 0] )  \n') 
        f.write('fenceHorizontal( pose [ 0 '+ str(self.vertFence * -1 + 34) +' 0 0 ] ) \n') 
 
        #add vertical fence instances
        f.write('fenceVertical( pose [ 50 '+ str(34 - self.vertFence * 0.5 ) +' 0 0 ] ) \n') 
        f.write('fenceVertical( pose [ -50 '+ str(34 - self.vertFence * 0.5) + ' 0 0 ] )  \n') 

        #add tree trunk instances for first row
        f.write('treetrunk( pose [ -34.5 ' + str(self.lastTrunk) + ' 0 0 ]) \n') 
        f.write('treetrunk( pose [ -28.5 ' + str(self.lastTrunk) + ' 0 0] )\n') 
        f.write('treetrunk( pose [ -22.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
        f.write('treetrunk( pose [ -16.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
        f.write('treetrunk( pose [ -10.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
        f.write('treetrunk( pose [ -4.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
        f.write('treetrunk( pose [ 1.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
        f.write('treetrunk( pose [ 7.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
        f.write('treetrunk( pose [ 13.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
        f.write('treetrunk( pose [ 19.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
        f.write('treetrunk( pose [ 25.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
        f.write('treetrunk( pose [ 31.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n')         
        
        #add tree instances for first row
        f.write('tree( pose [ -34.5 ' + str(self.lastTrunk) + ' 1.8 0 ]) \n') 
        f.write('tree( pose [ -28.5 ' + str(self.lastTrunk) + ' 1.8 0] )\n') 
        f.write('tree( pose [ -22.5 ' + str(self.lastTrunk) + ' 1.8 0 ] )\n') 
        f.write('tree( pose [ -16.5 ' + str(self.lastTrunk) + ' 1.8 0 ] )\n') 
        f.write('tree( pose [ -10.5 ' + str(self.lastTrunk) + ' 1.8 0 ] )\n') 
        f.write('tree( pose [ -4.5 ' + str(self.lastTrunk) + ' 1.8 0 ] )\n') 
        f.write('tree( pose [ 1.5 ' + str(self.lastTrunk) + ' 1.8 0 ] )\n') 
        f.write('tree( pose [ 7.5 ' + str(self.lastTrunk) + ' 1.8 0 ] )\n') 
        f.write('tree( pose [ 13.5 ' + str(self.lastTrunk) + ' 1.8 0 ] )\n') 
        f.write('tree( pose [ 19.5 ' + str(self.lastTrunk) + ' 1.8 0 ] )\n') 
        f.write('tree( pose [ 25.5 ' + str(self.lastTrunk) + ' 1.8 0 ] )\n') 
        f.write('tree( pose [ 31.5 ' + str(self.lastTrunk) + ' 1.8 0 ] )\n') 
      
        #add post instances for first row
        f.write('post( pose [ -31.5 ' + str(self.lastTrunk) + ' 0 0 ]) \n') 
        f.write('post( pose [ -25.5 ' + str(self.lastTrunk) + ' 0 0] )\n') 
        f.write('post( pose [ -19.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
        f.write('post( pose [ -13.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
        f.write('post( pose [ -7.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
        f.write('post( pose [ -1.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
        f.write('post( pose [ 4.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
        f.write('post( pose [ 10.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
        f.write('post( pose [ 16.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
        f.write('post( pose [ 22.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
        f.write('post( pose [ 28.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 


        for i in range(int(self.numberOfRows)- 1):

            #calculate next paragola and tree trunk position
            self.lastParagola = (float(self.lastTrunk) - 0.25 - (float(self.rowWidth)/2))
            self.lastTrunk = (float(self.lastTrunk) - 0.25 - float(self.rowWidth) - 0.25)
             
            #add tree trunk instances 
            f.write('treetrunk( pose [ -34.5 ' + str(self.lastTrunk) + ' 0 0 ]) \n') 
            f.write('treetrunk( pose [ -28.5 ' + str(self.lastTrunk) + ' 0 0] )\n') 
            f.write('treetrunk( pose [ -22.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
            f.write('treetrunk( pose [ -16.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
            f.write('treetrunk( pose [ -10.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
            f.write('treetrunk( pose [ -4.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
            f.write('treetrunk( pose [ 1.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
            f.write('treetrunk( pose [ 7.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
            f.write('treetrunk( pose [ 13.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
            f.write('treetrunk( pose [ 19.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
            f.write('treetrunk( pose [ 25.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
            f.write('treetrunk( pose [ 31.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 

            #add tree instances 
            f.write('tree( pose [ -34.5 ' + str(self.lastTrunk) + ' 1.8 0 ]) \n') 
            f.write('tree( pose [ -28.5 ' + str(self.lastTrunk) + ' 1.8 0] )\n') 
            f.write('tree( pose [ -22.5 ' + str(self.lastTrunk) + ' 1.8 0 ] )\n') 
            f.write('tree( pose [ -16.5 ' + str(self.lastTrunk) + ' 1.8 0 ] )\n') 
            f.write('tree( pose [ -10.5 ' + str(self.lastTrunk) + ' 1.8 0 ] )\n') 
            f.write('tree( pose [ -4.5 ' + str(self.lastTrunk) + ' 1.8 0 ] )\n') 
            f.write('tree( pose [ 1.5 ' + str(self.lastTrunk) + ' 1.8 0 ] )\n') 
            f.write('tree( pose [ 7.5 ' + str(self.lastTrunk) + ' 1.8 0 ] )\n') 
            f.write('tree( pose [ 13.5 ' + str(self.lastTrunk) + ' 1.8 0 ] )\n') 
            f.write('tree( pose [ 19.5 ' + str(self.lastTrunk) + ' 1.8 0 ] )\n') 
            f.write('tree( pose [ 25.5 ' + str(self.lastTrunk) + ' 1.8 0 ] )\n') 
            f.write('tree( pose [ 31.5 ' + str(self.lastTrunk) + ' 1.8 0 ] )\n') 

            #add pergola instances 
            f.write('pergola( pose [ -34.5 ' + str(self.lastParagola) + ' 2.3 0 ]) \n') 
            f.write('pergola( pose [ -28.5 ' + str(self.lastParagola) + ' 2.3 0] )\n') 
            f.write('pergola( pose [ -22.5 ' + str(self.lastParagola) + ' 2.3 0 ] )\n') 
            f.write('pergola( pose [ -16.5 ' + str(self.lastParagola) + ' 2.3 0 ] )\n') 
            f.write('pergola( pose [ -10.5 ' + str(self.lastParagola) + ' 2.3 0 ] )\n') 
            f.write('pergola( pose [ -4.5 ' + str(self.lastParagola) + ' 2.3 0 ] )\n') 
            f.write('pergola( pose [ 1.5 ' + str(self.lastParagola) + ' 2.3 0 ] )\n') 
            f.write('pergola( pose [ 7.5 ' + str(self.lastParagola) + ' 2.3 0 ] )\n') 
            f.write('pergola( pose [ 13.5 ' + str(self.lastParagola) + ' 2.3 0 ] )\n') 
            f.write('pergola( pose [ 19.5 ' + str(self.lastParagola) + ' 2.3 0 ] )\n') 
            f.write('pergola( pose [ 25.5 ' + str(self.lastParagola) + ' 2.3 0 ] )\n') 
            f.write('pergola( pose [ 31.5 ' + str(self.lastParagola) + ' 2.3 0 ] )\n') 

            #add post instances 
            f.write('post( pose [ -31.5 ' + str(self.lastTrunk) + ' 0 0 ]) \n') 
            f.write('post( pose [ -25.5 ' + str(self.lastTrunk) + ' 0 0] )\n') 
            f.write('post( pose [ -19.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
            f.write('post( pose [ -13.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
            f.write('post( pose [ -7.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
            f.write('post( pose [ -1.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
            f.write('post( pose [ 4.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
            f.write('post( pose [ 10.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
            f.write('post( pose [ 16.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
            f.write('post( pose [ 22.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
            f.write('post( pose [ 28.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 

        #close instances.inc
        f.close()

    '''This method creates the dynamic objects in the world'''
    def makeWorld(self):

        #open orchard.world
        f = open(str(self.home) +'/threeohsix/src/robotsim/world/orchard.world', 'w')
        f.write('include "instances.inc"\n') 
        f.write('include "objects.inc"\n') 
        f.write('# simulation property milliseconds per update step \n') 
        f.write('interval_sim 100 \n') 
        
        #adding animals
        f.write('dog( pose [20 -11 0 0  ] name "dog")\n')           
        f.write('dog( pose [20 15 0 0  ] name "dog2")\n')
        f.write('cat( pose [-47 -11 0 0  ] name "cat")\n')

        #adding workers
        f.write('person_worker ( pose [-20 22 0 0 ] name "worker")\n')           
        f.write('person_worker ( pose [25 25 0 0 ] name "worker2")\n')
        f.write('person_worker ( pose [36 18 0 0 ] name "worker3")\n')
        f.write('person_worker ( pose [-44 -15 0 0 ] name "worker4")\n')
           
        #adding visitors
        f.write('person_visitor ( pose [-47 8 0 0 ] name "visitor")\n')           
        f.write('person_visitor ( pose [-6 22 0 0 ] name "visitor2")\n')
        f.write('person_visitor ( pose [44 6 0 0 ] name "visitor3")\n')

        #adding tractor
        f.write('tractor( pose [-45 29 0 0  ] name "tractor")\n')  


        #adding weeds 
        robot = 11
        locationx = 0 
        locationy = 0

        for i in range(int(self.numberOfWeeds/2)):
            f.write('weed( pose  [ '+str(locationx)+' '+str(locationy)+' 0 0  ]name "weed '+str(robot)+'")\n')

            #randomly allocate x and y co-ordinates 
            locationx = randint(int(self.xLeft), int(self.xRight))
            locationy = randint(int(self.yBottom ), int(self.yBottom + 20))

            robot = robot + 1


        for i in range(int(self.numberOfWeeds/2)):

            #randomly allocate x and y co-ordinates 
            locationx = randint(int(self.xLeft), int(self.xRight))
            locationy = randint(int(self.yTop - 20) , int(self.yTop - 10))

            f.write('weed( pose  [ '+str(locationx)+' '+str(locationy)+' 0 0  ]name "weed '+str(robot)+'")\n')

            robot = robot + 1


      
        #adding pickers
        location = (13.5 - 0.25 - (float(self.rowWidth)/2))

        self.pickerNormal = (self.numberOfRows -1) / self.numberOfPickers #how many rows each picker has to do
        self.pickerRemainder = (self.numberOfRows -1) % self.numberOfPickers #remainder row that the last picker does

        
        for i in range(int(self.numberOfPickers)):
            f.write('picker( pose [-35.5 '+ str(location) +' 0 0  ] name "picker '+str(robot)+'" color "violet")\n')
            location = location - self.pickerNormal * (self.rowWidth + 0.5) #calculate next location
            robot = robot + 1
        self.lastPickerName = "/robot_" + str(robot-1)


        #adding carriers
        location = 40
        for i in range(int(self.numberOfCarriers)):
            f.write('carrier( pose [ '+str(location)+' 30 0 0  ] name "carrier '+str(robot)+'" color "cyan")\n')
            location = location - 6 #calculate next location
            robot = robot + 1


        #adding bins
        
        #bins following pickers
        location = (13.5 - 0.25 - (float(self.rowWidth)/2))
        for i in range(int(self.numberOfBins)/2):
            f.write('bucket( pose [-38 '+ str(location) +' 0 0  ] name "bin '+str(robot)+'")\n')
            location = location - self.pickerNormal * (self.rowWidth + 0.5) 
            robot = robot + 1


        #bins following carriers
        location = 37
        for i in range(int(self.numberOfBins)/2):
            f.write('bucket( pose  [ '+str(location)+' 30 0 0  ]name "bin '+str(robot)+'")\n')
            location = location - 6
            robot = robot + 1



        #close orchard.world
        f.close()     
    '''This method makes the launch file'''
    def makeLaunch(self):
        
        f = open( str(self.home) +'/threeohsix/src/robotsim/launch.launch', 'w')
        f.write('<launch>\n')
        # Launch animals
        robot = 0
        for i in range(3):
            f.write('\t<group ns="robot_'+ str(robot) +'">\n') 
            f.write('\t\t<node pkg="robotsim" name="node" type="animal.py"/>\n')
            f.write('\t</group>\n')
            robot += 1
       
        # Launch 4 workers and 3 visitors
        for i in range(7):
            f.write('\t<group ns="robot_'+ str(robot) +'">\n') 
            f.write('\t\t<node pkg="robotsim" name="node" type="person.py"/>\n')
            f.write('\t</group>\n')
            robot += 1

        f.write('\t<group ns="robot_'+ str(robot) +'">\n') 
        f.write('\t\t<node pkg="robotsim" name="node" type="tractor.py"/>\n')
        f.write('\t</group>\n')
        robot += 1

        # Launch weeds
        for i in range(int(self.numberOfWeeds)):
            f.write('\t<group ns="robot_'+ str(robot) +'">\n') 
            f.write('\t\t<node pkg="robotsim" name="node" type="weed.py"/>\n')
            f.write('\t</group>\n')
            robot += 1
       

        # Launch pickers
        for i in range(int(self.numberOfPickers)):
            f.write('\t<group ns="robot_'+ str(robot) +'">\n') 
            f.write('\t\t<node pkg="robotsim" name="node" type="picker.py"/>\n')
            f.write('\t</group>\n')
            robot += 1

        # Launch carriers
        for i in range(int(self.numberOfCarriers)):
            f.write('\t<group ns="robot_'+ str(robot) +'">\n') 
            f.write('\t\t<node pkg="robotsim" name="node" type="carrier.py"/>\n')
            f.write('\t</group>\n')
            robot += 1

        # Launch bins
        for i in range(int(self.numberOfBins)):
            f.write('\t<group ns="robot_'+ str(robot) +'">\n') 
            f.write('\t\t<node pkg="robotsim" name="node" type="bin.py"/>\n')
            f.write('\t</group>\n')
            robot += 1
        f.write('</launch>\n')
     
        f.close()
    
    ''' This method makes the executable file that only uses one terminal'''
    def makeOneExecutableWindow(self):

        #open run_one_window.sh
        f = open(str(self.home) +'/threeohsix/run_one_window.sh', 'w')

 
        f.write('#!/bin/bash\n')
        f.write('rm -r build\n')
        f.write('rm -r devel\n')
        f.write('gnome-terminal -x sh -c \'roscore\'\n')
        f.write('catkin_make\n')
        f.write('source devel/setup.bash; roslaunch robotsim launch.launch &\n')
        f.write('source devel/setup.bash; rosrun robotsim node.py &\n')

        # animal node
        robot = 0
        for i in range(3):
            f.write('source devel/setup.bash; rosrun robotsim animal.py '+str(robot) +' &\n')
            robot += 1
       
        # person node
        for i in range(7):
            f.write('source devel/setup.bash; rosrun robotsim person.py '+str(robot) +' &\n')
            robot += 1

        # tractor node
        f.write('source devel/setup.bash; rosrun robotsim tractor.py '+str(robot) +' &\n')
        robot += 1


        # weeds node
        for i in range(int(self.numberOfWeeds)):
            f.write('source devel/setup.bash; rosrun robotsim weed.py '+str(robot) +' &\n')
            robot += 1

        # picker node
        for i in range(int(self.numberOfPickers)):
            f.write('source devel/setup.bash; rosrun robotsim picker.py '+str(robot) +' &\n')
            robot += 1

        # carrier node 
        for i in range(int(self.numberOfCarriers)):
            f.write('source devel/setup.bash; rosrun robotsim carrier.py '+str(robot) +' &\n')
            robot += 1

        # bin node
        for i in range(int(self.numberOfBins)):
            f.write('source devel/setup.bash; rosrun robotsim bin.py '+str(robot) +' &\n')
            robot += 1

        
        f.write('source devel/setup.bash; rosrun stage_ros stageros src/robotsim/world/orchard.world &\n')
        #close run_one_window.sh
        f.close()

    ''' This method makes the executable file that uses multiple terminal - for debugging'''
    def makeBash(self):

        #open run.sh
        f = open(str(self.home) +'/threeohsix/run.sh', 'w')
        f.write('#!/bin/bash\n')
        f.write('rm -r build\n')
        f.write('rm -r devel\n')
        f.write('gnome-terminal -x sh -c \'roscore\'\n')
        f.write('catkin_make\n')
        f.write('source devel/setup.bash\n')
        f.write('gnome-terminal -x sh -c \'roslaunch robotsim launch.launch\'\n')
        f.write('source devel/setup.bash\n')
        f.write('gnome-terminal -x sh -c \'rosrun robotsim node.py\'\n')

        # animal node
        robot = 0
        for i in range(3):
            f.write('source devel/setup.bash\n')
            f.write('gnome-terminal -x sh -c \'rosrun robotsim animal.py '+str(robot) + '\'\n')
            robot += 1
       
        # person node
        for i in range(7):
            f.write('source devel/setup.bash\n')
            f.write('gnome-terminal -x sh -c \'rosrun robotsim person.py '+str(robot) + '\'\n')
            robot += 1

        # tractor node
        f.write('source devel/setup.bash\n')
        f.write('gnome-terminal -x sh -c \'rosrun robotsim tractor.py '+ str(robot)+ '\'\n')
        robot += 1


        # weeds node
        for i in range(int(self.numberOfWeeds)):
            f.write('source devel/setup.bash\n')
            f.write('gnome-terminal -x sh -c \'rosrun robotsim weed.py '+ str(robot)+ '\'\n')
            robot += 1

        # picker node
        for i in range(int(self.numberOfPickers)):
            f.write('source devel/setup.bash\n')
            f.write('gnome-terminal -x sh -c \'rosrun robotsim picker.py '+ str(robot) + '\'\n')
            robot += 1

        # carrier node 
        for i in range(int(self.numberOfCarriers)):
            f.write('source devel/setup.bash\n')
            f.write('gnome-terminal -x sh -c \'rosrun robotsim carrier.py '+ str(robot) + '\'\n')
            robot += 1

        # bin node
        for i in range(int(self.numberOfBins)):
            f.write('source devel/setup.bash\n')
            f.write('gnome-terminal -x sh -c \'rosrun robotsim bin.py '+ str(robot)+ '\'\n')
            robot += 1

       
        f.write('source devel/setup.bash\n')
        f.write('gnome-terminal -x sh -c \'rosrun stage_ros stageros src/robotsim/world/orchard.world\'\n')
        #close run.sh
        f.close()

    '''This method makes a worldInfo file which other classes can use to extract world info'''
    def createWorldInfo(self):

        #open worldInfo.py
        f = open(str(self.home) +'/threeohsix/src/robotsim/scripts/worldInfo.py', 'w')
        

        f.write('#!/usr/bin/env python\n')
        f.write('class WorldInfo():\n')

        f.write('    MIN_ROWS = 3\n')
        f.write('    MIN_PICKER = 2\n')

        f.write('    def __init__(self):\n')
    
        #write all the variable values to worldinfofile
        f.write('\tself.numberOfRows = ' + str(self.numberOfRows) + '\n')
        f.write('\tself.numberOfPickers = ' + str(self.numberOfPickers)+ '\n')
        f.write('\tself.maxPickers = ' + str(self.maxPickers)+ '\n')
        f.write('\tself.rowWidth = ' + str(self.rowWidth)+ '\n')
        f.write('\tself.numberOfCarriers = ' + str(self.numberOfCarriers)+ '\n')
        f.write('\tself.numberOfBins = ' + str(self.numberOfBins)+ '\n')
        f.write('\tself.numberOfWeeds = ' + str(self.numberOfWeeds)+ '\n')
        f.write('\tself.lastTrunk = ' + str(self.lastTrunk)+ '\n') 
        f.write('\tself.lastPargola = ' + str(self.lastPargola)+ '\n')
        f.write('\tself.vertFence = ' + str(self.vertFence)+ '\n')
        f.write('\tself.pickerNormal = ' + str(self.pickerNormal)+ '\n')
        f.write('\tself.pickerRemainder = ' + str(self.pickerRemainder)+ '\n')
        f.write('\tself.lastPickerName = "' + str(self.lastPickerName)+ '"\n')
        f.write('\tself.yTop = "' + str(self.yTop)+ '"\n')
        f.write('\tself.yBottom = "' + str(self.yBottom)+ '"\n')
        f.write('\tself.xRight = "' + str(self.xRight)+ '"\n')
        f.write('\tself.xLeft = "' + str(self.xLeft)+ '"\n')
     

        f.write('worldInfo = WorldInfo()')
        #close worldInfo.py
        f.close()



         




