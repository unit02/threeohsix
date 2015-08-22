#!/usr/bin/env python
class WorldConfig():

    MIN_ROWS = 3
    MIN_PICKER = 2

    def __init__(self):
    
        self.numberOfRows = 3
        self.numberOfPickers =  2
        self.maxPickers = self.numberOfRows - 1
        self.rowWidth = 3.5
        self.treeSpacing = 5 
        self.lastTrunk = 13.5 
        self.lastPargola = 0
        self.getNumberOfRows()
        self.getNumberOfPickers()
        self.getRowWidth()
        self.kiwifruitSpacing()
        self.makeWorld()

    def getNumberOfRows(self):    

        self.numberOfRows = raw_input("Please enter number of rows: ")
        print "#ofRows " + self.numberOfRows
        self.maxPickers = int(self.numberOfRows) - 1
        return int(self.numberOfRows)

    def getNumberOfPickers(self):    

        self.numberOfPickers = raw_input("Please enter number of pickers: ")
        #while (self.numberOfPickers > self.maxPickers):
             #self.numberOfPickers = raw_input("Number of pickers must be less than the number of rows. Please enter number of pickers: ")
   
        print "#ofPickers" + self.numberOfPickers
        return int(self.numberOfPickers)

    def getRowWidth(self):    

        self.rowWidth = raw_input("Please enter the row width (in metres): ")
        print "row width" + self.rowWidth
        return int(self.rowWidth)

    def kiwifruitSpacing(self):    

        self.treeSpacing = raw_input("Please enter the kiwifruitTrunk/post spacing (in metres): ")
        print "kiwifruitTrunk/Post spacing" + self.treeSpacing
        return int(self.treeSpacing)



    def makeWorld(self):
        f = open('/afs/ec.auckland.ac.nz/users/c/c/ccha504/unixhome/threeohsix/src/robotsim/world/instances.inc', 'a')
        for i in range(int(self.numberOfRows)- 1):
            self.lastParagola = (float(self.lastTrunk) - 0.25 - (float(self.rowWidth)/2))
            self.lastTrunk = (float(self.lastTrunk) - 0.25 - float(self.rowWidth) - 0.25)
             
            #f.write(' ' + str(self.lastTrunk) )
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

world = WorldConfig()

