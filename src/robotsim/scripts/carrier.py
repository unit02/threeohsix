#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point
from havesting_robot import havesting_robot
import roslib
roslib.load_manifest('robotsim')
from robotsim.msg import bin_call,carrier_to_picker
import sys
from worldInfo import *


class carrier(havesting_robot):
    def __init__(self,name, laser_on, path_width, width):
        self.picking_bin = False
        self.to_pick_bin_pos = Point()
        super(carrier,self).__init__(name,laser_on, path_width, width)

        self.pick_bin_sub = rospy.Subscriber(
            "/bin_info",
            bin_call,
            callback=self._pickBin_callback,
            queue_size=1
        )

    def _pickBin_callback(self,bin_call):
         self.wait(5)
         if self.name == "/robot_14":
             #Get the pickers name from the bin_call message
             picker_name = bin_call.picker_to_attach_name

             #Create the publisher to tell the picker to move and which bin to attach
             self.inform_picker = rospy.Publisher(
                picker_name + "/end_of_row",
                carrier_to_picker,
                queue_size=1
             )
             #Move to the empty picker
             new_position = Point(bin_call.x_coordinate + 2, bin_call.y_coordinate-5, 0.0)
             rospy.loginfo("Moving to pick up the bin")
             self.picking_bin = True
             self.to_pick_bin_pos = new_position
             self.move_to(new_position)
             #ABOVEISGOODS
             #Detach the empty bin and tell the picker to go
             self.detach_bin(False)
             msg = carrier_to_picker()
             msg.bin_name = self.bin_following

             self.inform_picker.publish(msg)

             self.picking_bin = False

             #TODO: momve the picker to an appropriate location to attach the bin
             #Attach the full bin
             new_position = Point(bin_call.x_coordinate + 2, bin_call.y_coordinate, 0.0)
             #self.bin_attach(bin_call.bin_name)
             #TODO move back to tractor position
             #TODO find what place it is left, right, top, bot - move method
             #rospy.loginfo("Full bin attached to carry, time to drop off at tractor")
             self.move_x_steps(5)
             #TODO turn laser back on
             self.laser_on = False

    def stage_callback(self, data):
        super(carrier,self).stage_callback(data)
        if self.picking_bin:
            deltaX = self.position.x - self.to_pick_bin_pos.x
            deltaY = self.position.y - self.to_pick_bin_pos.y
            if (abs(deltaX) < 3.0 and abs(deltaY) < 3.0) and self.laser_on:
                rospy.logwarn("Temporary turning off laser to get to bin")
                self.laser_on = False


if __name__ == '__main__':
    bin_name = sys.argv[1] + worldInfo.numberOfPickers * 2
    rospy.init_node("robot_"+sys.argv[1])  # Create a node of name laser_roomba

    # leave as static
    row_width = 5.0
    object_width = 1.5

    l = carrier(rospy.get_name(), False, row_width, object_width, "/robot_" + bin_name)  # Create an instance of above class

    rospy.spin()  # Function to keep the node running until terminated via Ctrl+C

