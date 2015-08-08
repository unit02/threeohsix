#!/usr/bin/env python
   2 
   3 """ Example code of how to move a robot forward for 3 seconds. """
   4 
   5 # We always import roslib, and load the manifest to handle dependencies
   6 import roslib; roslib.load_manifest('mini_max_tutorials')
   7 import rospy
   8 
   9 # recall: robots generally take base movement commands on a topic 
  10 #  called "cmd_vel" using a message type "geometry_msgs/Twist"
  11 from geometry_msgs.msg import Twist
  12 
  13 x_speed = 0.1  # 0.1 m/s
  14 
  15 # this quick check means that the following code runs ONLY if this is the 
  16 # main file -- if we "import move" in another file, this code will not execute.
  17 if __name__=="__main__":
  18 
  19     # first thing, init a node!
  20     rospy.init_node('move')
  21 
  22     # publish to cmd_vel
  23     p = rospy.Publisher('cmd_vel', Twist)
  24 
  25     # create a twist message, fill in the details
  26     twist = Twist()
  27     twist.linear.x = x_speed;                   # our forward speed
  28     twist.linear.y = 0; twist.linear.z = 0;     # we can't use these!        
  29     twist.angular.x = 0; twist.angular.y = 0;   #          or these!
  30     twist.angular.z = 0;                        # no rotation
  31 
  32     # announce move, and publish the message
  33     rospy.loginfo("About to be moving forward!")
  34     for i in range(30):
  35         p.publish(twist)
  36         rospy.sleep(0.1) # 30*0.1 = 3.0
  37 
  38     # create a new message
  39     twist = Twist()
  40 
  41     # note: everything defaults to 0 in twist, if we don't fill it in, we stop!
  42     rospy.loginfo("Stopping!")
  43     p.publish(twist)
