#!/usr/bin/env python
import rospy
import dynamicObjects
from geometry_msgs.msg import Twist



class picker():

    #pub = rospy.Publisher('chatter', String, queue_size=10)

    #node is publishing "cmd_val" topic
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    #initilasing a node named "talker"
    rospy.init_node('pubnode', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
	twist = Twist()
	twist.linear.x = 3
	twist.angular.z = 0.0;
	
        rospy.loginfo(twist)
        pub.publish(twist)
        rate.sleep()


if __name__ == '__main__':
 picker()



"""     #node is publishing "cmd_val" topic
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    #initilasing a node named "talker"
    rospy.init_node('picker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        twist = Twist()
        twist.linear.x = 1
        twist.angular.z = 0.01;

        rospy.loginfo(twist)
        pub.publish(twist)
        rate.sleep()


	def laser_callback(self,msg):
		ranges = msg. laser
		min_distance = numpy.nanmin(ranges)
        rospy.loginfo("Minimum distance : %f")

    def pick (self):
			#every 1 second "pick" kiwifruit
			  #sends signal to nearest carrier to updateBin()

	#def goThroughRow(self):

    #def goToNextRow(self):
	#assumes the picker is  """
