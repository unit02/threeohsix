#!/usr/bin/env python
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
        self.lastTrunk = 13.5 
        self.lastPargola = 0
        self.vertFence = 0

        
        self.getNumberOfRows()
        self.getNumberOfPickers()
        self.getRowWidth()
        self.getNumberOfCarriers()
        self.getNumberOfBins()
        self.setGround()
        self.makeOrchard()
        self.makeWorld()
        self.makeLaunch()
        self.makeBash()

    def getNumberOfRows(self):    

        accepted = 0
        while (accepted == 0):
            self.numberOfRows = int(raw_input("Please enter number of rows (min = 3 rows, max = 20 rows): "))
            if (self.numberOfRows > 2 ) & (self.numberOfRows < 21):
                accepted = 1
            else: 
                print "invalid input, please try again"
        
        print "#ofRows " + str(self.numberOfRows)
        self.maxPickers = int(self.numberOfRows) - 1
        return self.numberOfRows

    def getNumberOfPickers(self):    


        accepted = 0
        while (accepted == 0):
            self.numberOfPickers = int(raw_input("Please enter number of pickers (min = 2 pickers, max = less than number of rows): "))
            if (self.numberOfPickers > 1 ) & (self.numberOfPickers <= self.maxPickers):
                accepted = 1
            else: 
                print "invalid input, please try again"
   
        print "#ofPickers " + str(self.numberOfPickers)
        return self.numberOfPickers

    def getRowWidth(self):    


        accepted = 0
        while (accepted == 0):
            self.rowWidth = int(raw_input("Please enter the row width (min = 5 metres): "))
            if (self.rowWidth > 4 ):
                accepted = 1
            else: 
                print "invalid input, please try again"

        
        print "row width " + str(self.rowWidth)
        return self.rowWidth

    def getNumberOfCarriers(self):    

        self.numberOfCarriers = int(self.numberOfPickers) 
        print "#ofCarriers " + str(int(self.numberOfCarriers))
        return int(self.numberOfCarriers)

    def getNumberOfBins(self): 
        self.numberOfBins = int(self.numberOfPickers) * 2
        print "#ofBins" + str(int(self.numberOfBins))
        return int(self.numberOfBins)
    
    def setGround(self):
        f = open('/afs/ec.auckland.ac.nz/users/c/c/ccha504/unixhome/threeohsix/src/robotsim/world/ground.inc', 'w')

        f.write('define fenceHorizontal model( \n')
 	f.write('\tcolor "yellow"\n ')
 	f.write('\tsize [101 1 2.5] \n')	
	f.write('\tblock( \n')
	f.write('\tpoints 4 \n')
	f.write('\tpoint[0] [0 0]\n ')
	f.write('\tpoint[1] [1 0]\n ')
	f.write('\tpoint[2] [1 1] \n')
	f.write('\tpoint[3] [0 1]\n')
	f.write('\tz [0 1] )\n)\n')


        self.vertFence = float(self.rowWidth * (self.numberOfRows -1)) + float((0.5 * self.numberOfRows)) + 41 

        f.write('define fenceVertical model( \n')
 	f.write('\tcolor "yellow"  \n')
 	f.write('\tsize [1 '+ str(self.vertFence + 1) +' 2.5]  \n')	
	f.write('\tblock(  \n')
	f.write('\tpoints 4  \n') 
	f.write('\tpoint[0] [0 0]  \n')
	f.write('\tpoint[1] [1 0]  \n')
	f.write('\tpoint[2] [1 1]  \n')
	f.write('\tpoint[3] [0 1] \n')
	f.write('z [0 1] ) \n)\n')
       
        f.write('define ground model \n')
        f.write('( \n')
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


        f.write('define pergola model\n')
        f.write('(\n')
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

        f.close()

    def makeOrchard(self):
        f = open('/afs/ec.auckland.ac.nz/users/c/c/ccha504/unixhome/threeohsix/src/robotsim/world/instances.inc', 'w')
        f.write('include "myblock.inc" \n') 
        f.write('include "ground.inc" \n') 
        
        f.write('ground( pose [ 0 '+ str(self.vertFence * 0.5 * -1 + 34) +' 0 0] ) \n')
 
        #f.write('driveway( pose [ -30 26.5 0 0] ) \n') 
        

        f.write('fenceHorizontal( pose [ 0 34 0 0] )  \n') 
        f.write('fenceHorizontal( pose [ 0 '+ str(self.vertFence * -1 + 34) +' 0 0 ] ) \n') 
        f.write('fenceVertical( pose [ 50 '+ str(34 - self.vertFence * 0.5 ) +' 0 0 ] ) \n') 
        f.write('fenceVertical( pose [ -50 '+ str(34 - self.vertFence * 0.5) + ' 0 0 ] )  \n') 
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
        f.write('post( pose [ 29.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 

        for i in range(int(self.numberOfRows)- 1):
            self.lastParagola = (float(self.lastTrunk) - 0.25 - (float(self.rowWidth)/2))
            self.lastTrunk = (float(self.lastTrunk) - 0.25 - float(self.rowWidth) - 0.25)
             
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
            f.write('post( pose [ 29.5 ' + str(self.lastTrunk) + ' 0 0 ] )\n') 
        f.close()

    def makeWorld(self):
        f = open('/afs/ec.auckland.ac.nz/users/c/c/ccha504/unixhome/threeohsix/src/robotsim/world/orchard.world', 'w')
        f.write('include "instances.inc"\n') 
        f.write('include "objects.inc"\n') 
        f.write('# simulation property milliseconds per update step \n') 
        f.write('interval_sim 100 \n') 
        
        #adding animals
        f.write('dog( pose [-14.5 -15 0 0  ] name "dog")\n')           
        f.write('dog( pose [-10.5 -10 0 0  ] name "dog2")\n')
        f.write('cat( pose [-12.5 -17 0 0  ] name "cat")\n')

        #adding workers
        f.write('person_worker ( pose [-40 22 0 0 ] name "worker")\n')           
        f.write('person_worker ( pose [-40 12 0 0 ] name "worker2")\n')
        f.write('person_worker ( pose [-40 0 0 0 ] name "worker3")\n')
        f.write('person_worker ( pose [-40 -20 0 0 ] name "worker4")\n')
           
        #adding visitors
        f.write('person_visitor ( pose [-38 4 0 0 ] name "visitor")\n')           
        f.write('person_visitor ( pose [-38 16 0 0 ] name "visitor2")\n')
        f.write('person_visitor ( pose [-38 -22 0 0 ] name "visitor3")\n')

        #adding tractor
        f.write('tractor( pose [-40 26.5 0 0  ] name "tractor")\n')  
      
        #adding pickers
        location = 11
        for i in range(int(self.numberOfPickers)):
            f.write('picker( pose [-39 '+ str(location) +' 0 0  ] name "picker" color "violet")\n')
            location = location - int(self.rowWidth)   
        #adding carriers
        location = 16.5
        for i in range(int(self.numberOfCarriers)):
            f.write('carrier( pose [34.5 '+ str(location) +' 0 0  ] name "carrier" color "cyan")\n')
            location = location + 4  
        
        #adding bins
        location = 11
        for i in range(int(self.numberOfBins)/2):
            f.write('bucket( pose [-41 '+ str(location) +' 0 0  ] name "bin")\n')
            location = location - int(self.rowWidth)   
        

        location = 16.5
        for i in range(int(self.numberOfBins)/2):
            f.write('bucket( pose [32.5 '+ str(location) +' 0 0  ] name "bin")\n')
            location = location + 4
        f.close()     

    def makeLaunch(self):
        f = open('/afs/ec.auckland.ac.nz/users/c/c/ccha504/unixhome/threeohsix/src/robotsim/launch.launch', 'w')
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

    def makeBash(self):
        f = open('/afs/ec.auckland.ac.nz/users/c/c/ccha504/unixhome/threeohsix/run.sh', 'w')
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
       
        # Launch 4 workers and 3 visitors
        for i in range(7):
            f.write('source devel/setup.bash\n')
            f.write('gnome-terminal -x sh -c \'rosrun robotsim person.py '+str(robot) + '\'\n')
            robot += 1

        # Launch 4 workers and 3 visitors
        f.write('source devel/setup.bash\n')
        f.write('gnome-terminal -x sh -c \'rosrun robotsim tractor.py '+ str(robot)+ '\'\n')
        robot += 1

        # Launch pickers
        for i in range(int(self.numberOfPickers)):
            f.write('source devel/setup.bash\n')
            f.write('gnome-terminal -x sh -c \'rosrun robotsim picker.py '+ str(robot) + '\'\n')
            robot += 1

        # Launch carriers
        for i in range(int(self.numberOfCarriers)):
            f.write('source devel/setup.bash\n')
            f.write('gnome-terminal -x sh -c \'rosrun robotsim carrier.py '+ str(robot) + '\'\n')
            robot += 1

        # Launch bins
        for i in range(int(self.numberOfBins)):
            f.write('source devel/setup.bash\n')
            f.write('gnome-terminal -x sh -c \'rosrun robotsim bin.py '+ str(robot)+ '\'\n')
            robot += 1

        f.write('source devel/setup.bash\n')
        f.write('gnome-terminal -x sh -c \'rosrun stage_ros stageros src/robotsim/world/orchard.world\'\n')
        f.close()

world = WorldConfig()

