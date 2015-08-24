#!/usr/bin/env python
import rospy
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


class carrier(havesting_robot):
    def __init__(self,name, laser_on, path_width, width):
        super(carrier,self).__init__(name,laser_on, path_width, width)
        self.picking_bin = False

        self.pick_bin_sub = rospy.Subscriber(
            "/bin_info",
            bin_call,
            callback=self._pickBin_callback,
            queue_size=1
        )

        """self.whichOne = rospy.Subscriber(
            "/whichRobotToPick",
            str,
            callback=self.isItMe,
            queue_size=1
        )"""

        self.firstInQ = rospy.Publisher(
            "/firstInQ",
            queue_position,
            queue_size=1
        )

    def isItMe(self, msg):
        rospy.loginfo("IS IT MEE?????????????????????????? MNSG")
        if self.name == msg:
            rospy.loginfo(msg)
            return True 

    def publish_position(self):
        rospy.loginfo("HIIIIIIIIIIIIIIIIIIIIIIIIIII!")
        lowestY = self.name
        msg = queue_position()
        msg.robot_name = self.name
        msg.x_coordinate = self.position.x
        msg.y_coordinate = self.position.y
        self.firstInQ.publish(msg)
        rospy.loginfo("HEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEYYYY"+str( msg.y_coordinate))


    def _pickBin_callback(self,bin_call):
         self.wait(5)
         rospy.loginfo("_pickBin_callback_pickBin_callbackHIIIIIIIIIIIIIIIIIIIIIIIIIII!")
         
         
         new_position = Point(bin_call.x_coordinate + 2, bin_call.y_coordinate + 2, 0.0)
         rospy.loginfo("Moving to pick up the bin")
         self.move_to(new_position)
         #if isItMe:
             #self.move_to(new_position)
         rospy.loginfo(self.name)
         self.publish_position()
         
         # changed so selected queue like
         if self.name == "/robot_13":
             self.bin_attach(bin_call.bin_name)

    def _pickBin_callback(self,bin_call):
         self.wait(5)
         new_position = Point(bin_call.x_coordinate + 2, bin_call.y_coordinate + 2, 0.0)
         rospy.loginfo("Moving to pick up the bin")
         self.move_to(new_position)
         rospy.loginfo(self.name)

         # changed so selected queue like
         if self.name == "/robot_14":
             self.bin_attach(bin_call.bin_name)

    def stage_callback(self, data):
        super(carrier,self).stage_callback(data)



if __name__ == '__main__':
    rospy.init_node("robot_"+sys.argv[1])  # Create a node of name laser_roomba

    # leave as static
    row_width = 5.0
    object_width = 1.5

    l = carrier(rospy.get_name(), False, row_width, object_width)  # Create an instance of above class
    rospy.spin()  # Function to keep the node running until terminated via Ctrl+C

