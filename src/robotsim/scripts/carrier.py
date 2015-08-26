#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point
from havesting_robot import havesting_robot
import roslib
roslib.load_manifest('robotsim')
from robotsim.msg import bin_call,carrier_to_picker
import sys
from worldInfo import *
from geometry_msgs.msg import Point,Vector3, Twist
from havesting_robot import havesting_robot
import roslib
roslib.load_manifest('robotsim')
import sys
from robotsim.msg import bin_call,queue_position,bin_detach,attach_bin
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from node import node
import std_msgs
from worldInfo import *

class State:
    Waiting, Working = range(2)

    @classmethod
    def tostring(cls, val):
        for name,v in vars(cls).iteritems():
            if v==val:
                return name



class carrier(havesting_robot):
    def __init__(self,name, laser_on, path_width, width, bin_name):
        self.picking_bin = False
        self.to_pick_bin_pos = Point()
        self.binCall = bin_call()
        self.state = State.Waiting
        self.positionInQueue = Point()
        super(carrier,self).__init__(name,laser_on, path_width, width, bin_name)

        self.pick_bin_sub = rospy.Subscriber(
            "/bin_info",
            bin_call,
            callback=self._pickBin_callback,
            queue_size=1
        )
        self.whichOne = rospy.Subscriber(
            "/whichRobotToPick",
            String,
            callback=self.isItMe,
            queue_size=10
        )

        self.firstInQ = rospy.Publisher(
            "/firstInQ",
            queue_position,
            queue_size=1
        )

    """ method to see if bin is calling self, if it does, then I will go pick it up ASAP """ 
    def isItMe(self, msg):
       
        if self.name == msg.data and self.state == State.Waiting:

            self.state = State.Working  #change my state to working so I stop receiving bin calls
            self.positionInQueue = self.position  #save my position for late
            self.goPickBin()  #go pick bin up 


    """ publish position of self to firstInQ topic so bin can listen to it and calls the closest robot """
    def publish_position(self):
        msg = queue_position()
        msg.robot_name = self.name
        msg.x_coordinate = self.position.x
        msg.y_coordinate = self.position.y
        if self.state == State.Waiting:   #only publish if you are in waiting queue to avpid bin calling a working robot
            self.firstInQ.publish(msg)


    """ method to go pick bin  """
    def goPickBin(self):
         
         #Get the pickers name from the bin_call message
         picker_name = self.binCall.picker_to_attach_name

         #Create the publisher to tell the picker to move and which bin to attach
         self.inform_picker = rospy.Publisher(
            picker_name + "/end_of_row",
            carrier_to_picker,
            queue_size=1
         )
         row_width = worldInfo.rowWidth + 0.5
         sign_changer = 1
         #Move to the empty bin
         if (self.binCall.x_coordinate < 0):
            sign_changer = -1

         #Move to the empty bin
         new_position = Point(self.binCall.x_coordinate + 8*sign_changer, self.binCall.y_coordinate-row_width, 0.0)
         rospy.loginfo("Moving to pick up the bin")
         self.picking_bin = True
         self.to_pick_bin_pos = new_position
         self.move_to(new_position)

         # face the same way the picker
         self.turnRight()

         #Detach the empty bin and tell the picker to go
         self.detach_bin(False)

         # tell picker to attach to the bin following carrier
         msg = carrier_to_picker()
         msg.bin_name = self.bin_following
         self.inform_picker.publish(msg)


         #TODO: momve the picker to an appropriate location to attach the bin
         #Attach the full bin
         new_position = Point(self.binCall.x_coordinate + 8*sign_changer, self.binCall.y_coordinate, 0.0)
         self.move_to(new_position)

         # face same was the bin and attach the bin
         self.turnRight()
         self.bin_attach(self.binCall.bin_name)
         self.picking_bin = False
         self.laser_on = True

         rospy.loginfo("Full bin attached to carry, time to drop off at tractor")
         self.move_x_steps(5)
         self.turnRight()
         rospy.loginfo("Lets go to tractor!")
         #self.goToTractor()

    """ method to move carrier robot with full kiwi to tractor to drop off, then back to its position in queue """
    def goToTractor(self):
         #move to bottom right corner
         rospy.loginfo("BOTTOM RIGHHHHHHHHHHHHHHHHHHHHHHHHHHTTTTTTTTT")
         new_position = Point(float(worldInfo.xRight)-5, float(worldInfo.yBottom) +5, 0.0)
         self.move_to(new_position)
         self.turnRight()

         #move to bottom left corner
         rospy.loginfo("BOTTOM LEFTTTTTTTTTT")
         new_position = Point(float(worldInfo.xLeft)+5, float(worldInfo.yBottom) +5, 0.0)
         self.move_to(new_position)
         self.turnRight()

         #move to top left corner, tractor place and wait for 5 seconds (unloading kiwis)
         rospy.loginfo("TRACTORRRRRRRRRRRRRRRRRRRRRRRRRR")
         new_position = Point(float(worldInfo.xLeft)+5, float(worldInfo.yTop) -15, 0.0)
         self.move_to(new_position)
         self.wait(5)
         self.turnRight()

         #move back to queue, top right
         #maybe go back to original position in Q
         rospy.loginfo("BACK TO QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ")
         new_position = Point(float(worldInfo.xRight)-5, float(worldInfo.yTop) -5, 0.0)
         self.move_to(new_position)
         self.state = State.Waiting

    """ callback method called after listening to bin_info topic """
    def _pickBin_callback(self,bin_call):
         rospy.loginfo(self.name)
         self.publish_position()
         self.binCall = bin_call   #get the bin call position to be used in later methods


    def stage_callback(self, data):
        super(carrier,self).stage_callback(data)
        if self.picking_bin:
            deltaX = self.position.x - self.to_pick_bin_pos.x
            deltaY = self.position.y - self.to_pick_bin_pos.y
            if (abs(deltaX) < 3.0 and abs(deltaY) < 3.0) and self.laser_on:
                rospy.logwarn("Temporary turning off laser to get to bin")
                self.laser_on = False


if __name__ == '__main__':
    bin_name = int(sys.argv[1]) + worldInfo.numberOfPickers * 2
    rospy.init_node("robot_"+sys.argv[1])  # Create a node of name laser_roomba

    # leave as static
    row_width = worldInfo.rowWidth
    object_width = 1.5
    rospy.loginfo("bin name %s", bin_name)
    l = carrier(rospy.get_name(), False, row_width, object_width, "/robot_" + str(bin_name))  # Create an instance of above class

    rospy.spin()  # Function to keep the node running until terminated via Ctrl+C

