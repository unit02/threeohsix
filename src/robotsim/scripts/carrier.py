#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point
from havesting_robot import havesting_robot
import roslib
roslib.load_manifest('robotsim')
from robotsim.msg import bin_call
import sys


class carrier(havesting_robot):
    def __init__(self, name, laser_on ):
        super(carrier,self).__init__(name, laser_on)

        self.pick_bin_sub = rospy.Subscriber(
            "/bin_info",
            bin_call,
            callback=self._pickBin_callback,
            queue_size=1
        )

    def _pickBin_callback(self,bin_call):
         self.wait(5)
         new_position = Point(bin_call.x_coordinate + 2, bin_call.y_coordinate + 2, 0.0)
         rospy.loginfo("moving to pick up the bin")
         self.move_to(new_position)
         rospy.loginfo(self.name)

         # changed so selected queue like
         if self.name == "/robot_14":
             self.bin_attach(bin_call.bin_name)



if __name__ == '__main__':
    rospy.init_node("robot_"+sys.argv[1])  # Create a node of name laser_roomba
    l = carrier(rospy.get_name(), False)  # Create an instance of above class
    rospy.spin()  # Function to keep the node running until terminated via Ctrl+C



