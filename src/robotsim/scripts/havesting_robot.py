#!/usr/bin/env python
from node import node
import rospy
import roslib
roslib.load_manifest('robotsim')
from robotsim.msg import bin_call, bin_detach, attach_bin
from geometry_msgs.msg import Point, Twist
from sensor_msgs.msg import LaserScan
from node import Face

class Action:
    move_to, move_x_steps, no_action = range(3)

    @classmethod
    def tostring(cls, val):
        for name,v in vars(cls).iteritems():
            if v==val:
                return name

class havesting_robot(node):
	#Subscribes to the bin info topic to receive data on whether bins
    #need to be picked up
    def __init__(self,name, laser_on):
        self.current_action = Action.no_action
        self.action_arguments = None
        super(havesting_robot,self).__init__(name,laser_on)

        self.detachment = rospy.Publisher(
            self.name + "/detach",
            bin_detach,
            queue_size=1
        )
        self.attachment = rospy.Publisher(
            "/attach_bin",
            attach_bin,
            queue_size=1
        )

    def bin_attach(self, bin_name):
        rospy.loginfo("Bin attaching")
        msg = attach_bin()
        msg.to_attach_name = self.name
        msg.bin_name = bin_name
        self.attachment.publish(msg)

    def detach_bin(self):
        rospy.loginfo("Bin detaching")
        msg = bin_detach()
        msg.unfollow = True
        self.detachment.publish(msg)

    def move_to(self, new_position):
        rospy.loginfo("Move_to in harvesting robot")

        self.current_action = Action.move_to
        self.action_arguments = [new_position]
        super(havesting_robot,self).move_to(new_position)
        if not self.is_stopped:
            rospy.loginfo("Move_to, stopping normally")
            self.current_action = Action.no_action

    def move_x_steps(self, metres):
        # move x steps not part of move_to
        if self.current_action != Action.move_to:
            rospy.loginfo("Move_x_steps in harvesting robot")

            self.current_action = Action.move_x_steps
            self.action_arguments = [metres, self.position, self.face_value(self.rad_orient), self.position]
            super(havesting_robot,self).move_x_steps(metres)
            if not self.is_stopped:
                rospy.loginfo("Move_x_steps, stopping normally")

                self.current_action = Action.no_action

    def continue_action(self, action, args):
        if action == Action.move_to:
            self.move_to(args[0])
        elif action == Action.move_x_steps:
            # difference interms of x and y distances - assume first move in x then y
            metres = args[0]
            deltaX = metres - abs(args[3].x - args[1].x)
            deltaY = metres - abs(args[3].y - args[1].y)
            face = args[2]

            if (face == Face.South or face == Face.North):
                self.move_x_steps(deltaY)
            # facing west of east
            else:
                self.move_x_steps(deltaX)

    def laser_callback(self,msg):
        if self.laser_on:
            #Get the ranges of the laser scan and find the minimum
            ranges = msg.ranges
            rate = rospy.Rate(10)

            stop = False
            for i in range(60):
                if (ranges[i] < 2.5):
                    stop = True

            if not self.is_stopped and stop:
                self.is_stopped = True
                if self.current_action == Action.move_x_steps:
                    self.action_arguments[3] = self.position
                    rospy.logwarn("Initial stopping, something in the way,  %s",self.action_arguments[3])


            if stop:
                #rospy.logwarn("Stopping, something in the way")
                twist = Twist()
                self.cmd_vel_pub.publish(twist)


            if self.is_stopped and not stop:
                #start old
                rospy.loginfo("Starting old action %s", Action.tostring(self.current_action))
                self.is_stopped = False
                self.continue_action(self.current_action, self.action_arguments)
                self.current_action = Action.no_action
            rate.sleep()




