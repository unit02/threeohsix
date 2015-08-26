#!/usr/bin/env python
# top speed
# working speed

import rospy
import math
from tf.transformations import euler_from_quaternion
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Twist
import numpy as np
from sensor_msgs.msg import LaserScan
import roslib
roslib.load_manifest('robotsim')
from robotsim.msg import bin_call
import threading
import math

class Face:
    North, South, East, West = range(4)

    @classmethod
    def tostring(cls, val):
        for name,v in vars(cls).iteritems():
            if v==val:
                return name


class node(object):


    def __init__(self, name, laser_on):
        self.position = Point()
        self.twist = Twist()
        self.twist.linear.x = 1.0
        self.name = name
        self.laser_on = laser_on
        self.rad_orient = 0.0
        self.goal = 0.0
        self.Face = Face.East
        self.event = threading.Event()
        self.event.set()
        self.is_turning = False

        rospy.loginfo("Starting node %s" % name)

        self.cmd_vel_pub = rospy.Publisher(
            self.name + "/cmd_vel",
            Twist,
            queue_size=1
        )

        # Create new topic called laser to which it listens
        self.laser_sub = rospy.Subscriber(
                self.name + "/base_scan",
                LaserScan,
                callback=self.laser_callback,
                queue_size=1
            )

        # Subscribe to stage topic to obtain its position
        # Must change to approprite name instead "ns" + cmd_vel
        self.stage_info = rospy.Subscriber(
            self.name + "/base_pose_ground_truth",
            Odometry,
            callback=self.stage_callback,
            queue_size=1
        )
        # wait to gather stage information
        self.wait(10)



    # called when new message arrives from laser topic
    def laser_callback(self,msg):
        if self.laser_on:
            #Get the ranges of the laser scan and find the minimum
            ranges = msg.ranges
            min_distance = np.nanmin(ranges)
            twist_msg = Twist()
            rate = rospy.Rate(10)
            
            #Avoid obstacles that were detected within 4m ahead
            if (min_distance <= 1.0):
                # If it is nearly colliding, stop and turn
                self.wait(2)
                self.turnLeft()
                
            elif (min_distance <= 4.0):
                # Recognise the turning direction,
                # given that laser beam is 60 degrees wide
                if (ranges[0] <= 4.0) & (ranges[179] <= 4.0):
                    twist_msg.linear.x = 0
                    twist_msg.angular.z = math.pi*2
                    self.cmd_vel_pub.publish(twist_msg)
                    
                elif (ranges.index(min_distance) <=90):
                    #rospy.loginfo(ranges.index(min_distance))
                    twist_msg.linear.x = 1.0
                    twist_msg.angular.z = math.pi
                    self.cmd_vel_pub.publish(twist_msg)
                else:
                    #rospy.loginfo(ranges.index(min_distance))
                    twist_msg.linear.x = 1.0
                    twist_msg.angular.z = -math.pi
                    self.cmd_vel_pub.publish(twist_msg)
            else:
                #Moving straight
                twist_msg.linear.x = 1.0
                twist_msg.angular.z = 0
                self.cmd_vel_pub.publish(twist_msg)
            rate.sleep()

    def stage_callback(self, data):
        self.position = data.pose.pose.position
        quanternion = data.pose.pose.orientation
        qList = [quanternion.x, quanternion.y, quanternion.z, quanternion.w]
        self.rad_orient = euler_from_quaternion(qList)[2]

    # assuming Face.East is initial facing direction
    def face_value(self, rad_orient):
        # rad_orient is apporixmately 0.0 (0 degrees away from initial)
        if rad_orient > -0.7 and rad_orient < 0.7:
            return Face.East
        # if rad_orient is  is apporixmately 3.14 or -3.14 then it is facing west
        elif ((rad_orient > (-math.pi - 0.7) and rad_orient < (-math.pi + 0.7)) or
                      (rad_orient > (math.pi - 0.7) and rad_orient < (math.pi + 0.7))):
            return Face.West
        # rad_orient is apporixmately -1.5 (-90 degrees away from initial)
        elif rad_orient > (-math.pi/2 - 0.7) and rad_orient < (-math.pi/2 + 0.7):
            return Face.South
        # rad_orient is apporixmately 1.5 (90 degrees away from initial)
        else:
            return Face.North


    def move_to(self, new_position):
        self.wait(2)
        face = self.face_value(self.rad_orient)
        rospy.loginfo("Initial face direction: %s", Face.tostring(face))
        rospy.loginfo("Current position %s", self.position)
        rospy.loginfo("Moving to new position %s", new_position)

        # difference interms of x and y distances - assume first move in x then y
        steps_one = new_position.x - self.position.x
        steps_two = new_position.y - self.position.y

        # reverts so it moves deltaY distance first, y then x
        if face == Face.South or face == Face.North:
            temp = steps_two
            steps_two = steps_one
            steps_one = temp

        rospy.loginfo("Moving %s metres in face %s, turning then moving %s metres", int(steps_one), Face.tostring(face), int(steps_two))

        if abs(steps_one) > 0:
            # opposite direction to what robot is facing - rotate 180 degrees
            if (steps_one < 0 and (face == Face.East or face == Face.North)) \
                    or (steps_one > 0 and (face == Face.West or face == Face.South)):
                rospy.logwarn("Turning 180")
                self.turnLeft()
                self.turnLeft()
                self.wait(2)
                face = self.face_value(self.rad_orient)
            self.move_x_steps(int(steps_one))

        if abs(steps_two) > 0:
            if (steps_two > 0 and (face == Face.East or face == Face.South)) \
                    or (steps_two < 0 and (face == Face.West or face == Face.North)):
                self.turnLeft()
            else:
                self.turnRight()
            self.move_x_steps(int(steps_two))

        rospy.loginfo("Finished moving to the new position %s, facing %s", self.position,  Face.tostring(face))

    def move_x_steps(self, metres):
        # runtime seconds = distance/velocity
        # need to convert to seconds so *10 is applied
        runtime = abs(10*int(metres/self.twist.linear.x))

        rospy.loginfo("Started moving %s metres at speed %s, eta time %s!", self.twist.linear.x*runtime/10, self.twist.linear.x, runtime/10)

        # only remainder speed - velocity too fast
        if runtime >= 10:
            # publish twist for runtime seconds to move x metres
            for i in range(runtime):
                self.cmd_vel_pub.publish(self.twist)
                rospy.sleep(0.1)
                # need to pause if something is in the way - waits if event is not set
                self.event.wait()

        rospy.loginfo("At new position %s", self.position)

        self.wait(1)
        remainder_speed = metres % self.twist.linear.x

        if remainder_speed > 0.2:
            twist = Twist()
            twist.linear.x = remainder_speed
            rospy.loginfo("Moving remainder %s metres at speed %s, eta time 1!", metres % self.twist.linear.x, remainder_speed)

            for i in range(10):
                self.cmd_vel_pub.publish(twist)
                rospy.sleep(0.1)
                # need to stop the moving as something is in the way
                self.event.wait()

        # create a new message - everything set to 0 so it can stop
        twist = Twist()

        rospy.loginfo("Stopping!")
        self.cmd_vel_pub.publish(twist)

        rospy.loginfo("At new position %s", self.position)

    def turnRight(self):
        self.is_turning = True
        rospy.loginfo("Original Orientation %s, face %s", self.rad_orient, Face.tostring(self.face_value(self.rad_orient)))
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = -(math.pi / 8)
        rospy.loginfo("Turning")
        for i in range(40):
            self.cmd_vel_pub.publish(twist)
            rospy.sleep(0.1)
        
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        self.cmd_vel_pub.publish(twist)

        rospy.loginfo("Turned Right")
        rospy.loginfo("New Orientation %s, face %s", self.rad_orient, Face.tostring(self.face_value(self.rad_orient)))
        self.reorientation()
        self.is_turning = False
        #rospy.loginfo("New Orientation after reorientation %s, face %s", self.rad_orient,  Face.tostring(self.face_value(self.rad_orient)))

    def turnLeft(self):
        self.is_turning = True
        rospy.loginfo("Original Orientation %s, face %s", self.rad_orient, Face.tostring(self.face_value(self.rad_orient)))
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = (math.pi / 8)
        #rospy.loginfo("Turning")
        for i in range(40):
            self.cmd_vel_pub.publish(twist)
            rospy.sleep(0.1)

        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        self.cmd_vel_pub.publish(twist)
        rospy.loginfo("Turned Left")
        rospy.loginfo("New Orientation %s, face %s", self.rad_orient, Face.tostring(self.face_value(self.rad_orient)))
        self.reorientation()
        self.is_turning = False
        #rospy.loginfo("New Orientation after reorientation %s, face %s", self.rad_orient,  Face.tostring(self.face_value(self.rad_orient)))

    def reorientation(self):
        self.wait(1)
        twist = Twist()
        if self.rad_orient == 0:
            remainder = 0
        else:
            remainder = (math.pi/2) % abs(self.rad_orient)
            rospy.loginfo("remainder 1 is %s", remainder)
        if remainder == (math.pi/2) and self.rad_orient < (3*math.pi/4):
            rad_dist = abs(self.rad_orient) - math.pi/2
            rospy.loginfo("1rad_dist is %s", rad_dist)
        elif remainder == (math.pi/2) and self.rad_orient > (3*math.pi/4):
            rad_dist = math.pi - abs(self.rad_orient)
            rospy.loginfo("2rad_dist is %s", rad_dist)
        elif self.rad_orient < math.pi/4 and self.rad_orient > -math.pi/4:
            rad_dist = abs(self.rad_orient)
            rospy.loginfo("3rad_dist is %s", rad_dist)
        else:
            rad_dist = remainder
            rospy.loginfo("4rad_dist is %s", rad_dist)

        if (remainder > 0):
            # when the robot is facing east, but is slightly too north
            if ((self.rad_orient < math.pi/4) and (self.rad_orient > 0)):
                twist.angular.z = -rad_dist
                for i in range(10):
                    self.cmd_vel_pub.publish(twist)
                    rospy.sleep(0.1)
                    rospy.loginfo(self.rad_orient)
                    rospy.loginfo("1")
                twist = Twist()
            # when the robot is racing east, but is slightly too south
            elif ((self.rad_orient > -math.pi/4) and (self.rad_orient < 0)):
                twist.angular.z = rad_dist
                for i in range(10):
                    self.cmd_vel_pub.publish(twist)
                    rospy.sleep(0.1)
                    rospy.loginfo(self.rad_orient)
                    rospy.loginfo("2")
                twist = Twist()
            # Facing south but towards west
            elif ((self.rad_orient < -math.pi/2) and (self.rad_orient > -math.pi/2 - math.pi/4)):
                twist.angular.z = rad_dist
                for i in range(10):
                    self.cmd_vel_pub.publish(twist)
                    rospy.sleep(0.1)
                    rospy.loginfo(self.rad_orient)
                    rospy.loginfo("3")
                twist = Twist()
            # Facing south but towards east
            elif ((self.rad_orient > -math.pi/2) and (self.rad_orient < -math.pi/2 + math.pi/4)):
                twist.angular.z = -rad_dist
                for i in range(10):
                    self.cmd_vel_pub.publish(twist)
                    rospy.sleep(0.1)
                    rospy.loginfo(self.rad_orient)
                    rospy.loginfo("4")
                twist = Twist()
            # Facing west, but towards north
            elif ((self.rad_orient > 3 * math.pi/4)):
                twist.angular.z = rad_dist
                for i in range(10):
                    self.cmd_vel_pub.publish(twist)
                    rospy.sleep(0.1)
                    rospy.loginfo(self.rad_orient)
                    rospy.loginfo("5")
                twist = Twist()
            # Facing west, but towards south
            elif ((self.rad_orient < (-3 * math.pi/4))):
                twist.angular.z = -rad_dist
                for i in range(10):
                    self.cmd_vel_pub.publish(twist)
                    rospy.sleep(0.1)
                    rospy.loginfo(self.rad_orient)
                    rospy.loginfo("6")
                twist = Twist()
            # Facing north, but towards east
            elif ((self.rad_orient < (math.pi/2)) and (self.rad_orient > math.pi/4)):
                twist.angular.z = rad_dist
                for i in range(10):
                    self.cmd_vel_pub.publish(twist)
                    rospy.sleep(0.1)
                    rospy.loginfo(self.rad_orient)
                    rospy.loginfo("7")
                twist = Twist()
            # Facing north, but towards west
            elif ((self.rad_orient > (math.pi/2)) and (self.rad_orient < (3 * math.pi/4))):
                twist.angular.z = -rad_dist
                for i in range(10):
                    self.cmd_vel_pub.publish(twist)
                    rospy.sleep(0.1)
                    rospy.loginfo(self.rad_orient)
                    rospy.loginfo("8")
                twist = Twist()
        else:
            rospy.loginfo(remainder)

                    
    def wait(self, seconds):
        runtime = int(10 * seconds)
        twist = Twist()

        rospy.loginfo("Waiting for %s seconds!", seconds)

        # publish a twist of 0 linear & angular velocity
        for i in range(runtime):
            self.cmd_vel_pub.publish(twist)
            rospy.sleep(0.1)

        rospy.loginfo("Awake!")


# The block below will be executed when the python file is executed
# __name__ and __main__ are built-in python variables and need to start and end with *two* underscores
if __name__ == '__main__':
    pass
    # rospy.init_node("robot_4")  # Create a node of name laser_roomba
    # l = node(rospy.get_name(), False)  # Create an instance of above class
    # l.wait(5)
    # new_position = Point(38, 5.0, 0.0)
    # l.move_to(new_position)
    # rospy.spin()  # Function to keep the node running until terminated via Ctrl+C
