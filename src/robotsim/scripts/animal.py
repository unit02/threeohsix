#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from node import node
from random import randint 
import threading


class animal(node):
    #Chooses a random number between 1 and 6 and either turns or changes speed
    def random_move(self):
        twist_randmsg = Twist()
        random_action=randint(0,6)
        threading.Timer(3.0, self.random_move).start()

        if random_action==0:
            twist_randmsg.angular.z = 180
            self.cmd_vel_pub.publish(twist_randmsg)

        elif random_action==1:
            twist_randmsg.angular.z = 90
            self.cmd_vel_pub.publish(twist_randmsg)

        elif random_action==2:
            twist_randmsg.angular.z = 270
            self.cmd_vel_pub.publish(twist_randmsg)

# The block below will be executed when the python file is executed
# __name__ and __main__ are built-in python variables and need to start and end with *two* underscores
if __name__ == '__main__':
    rospy.init_node("robot_0")  # Create a node of name laser_roomba
    l = animal(rospy.get_name(), True)  # Create an instance of above class
    l.random_move()

    rospy.spin()  # Function to keep the node running until terminated via Ctrl+C
