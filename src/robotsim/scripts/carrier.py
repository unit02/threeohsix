#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point
from havesting_robot import havesting_robot
import roslib
roslib.load_manifest('robotsim')
from robotsim.msg import bin_call
import sys


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
         new_position = Point(bin_call.x_coordinate + 2, bin_call.y_coordinate + 2, 0.0)
         rospy.loginfo("Moving to pick up the bin")
         self.picking_bin = True

         self.to_pick_bin_pos = new_position
         self.move_to(new_position)
         rospy.loginfo(self.name)

         # changed so selected queue like
         if self.name == "/robot_14":
             self.picking_bin = False
             self.bin_attach(bin_call.bin_name)
         self.picking_bin = False
         self.laser_on = True

    def stage_callback(self, data):
        super(carrier,self).stage_callback(data)
        if self.picking_bin:
            deltaX = self.position.x - self.to_pick_bin_pos.x
            deltaY = self.position.y - self.to_pick_bin_pos.y
            if (abs(deltaX) < 3.0 and abs(deltaY) < 3.0) and self.laser_on:
                rospy.logwarn("Temporary turning off laser to get to bin")
                self.laser_on = False


if __name__ == '__main__':
    rospy.init_node("robot_"+sys.argv[1])  # Create a node of name laser_roomba

    # leave as static
    row_width = 5.0
    object_width = 1.5

    l = carrier(rospy.get_name(), True, row_width, object_width)  # Create an instance of above class
    rospy.spin()  # Function to keep the node running until terminated via Ctrl+C



