#!/usr/bin/env python
import rospy
import time

from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class Mover():

    def Callback_left_f(self, data):
        self.dist_left_f = round(data.ranges[0], 1)

    def Callback_left_r(self, data):
        self.dist_left_r = round(data.ranges[0], 1)

    def Callback_front(self, data):
        self.dist_front = round(data.ranges[0], 1)

    def listen(self):

        while not rospy.is_shutdown():
            time.sleep(0.2)
            rospy.Subscriber('/base_scan_0/', LaserScan, self.Callback_left_f)
            rospy.Subscriber('/base_scan_1/', LaserScan, self.Callback_left_r)
            rospy.Subscriber('/base_scan_2/', LaserScan, self.Callback_front)
            self.move_till_wall()

    def move_till_wall(self):

        if (self.dist_front != 1.0):
            self.vel_msg.linear.x = 0.1
            self.vel_msg.angular.z = -1
            self.velocity_publisher.publish(self.vel_msg)

        elif ((self.dist_left_r == self.dist_left_f) & (self.dist_left_f < 1.0)):
            self.vel_msg.linear.x = 1
            self.vel_msg.angular.z = 0
            self.velocity_publisher.publish(self.vel_msg)

        elif ((self.dist_left_f > 0.3) & (self.dist_left_r > 0.3) & (self.dist_left_f < 1) & (self.dist_left_r < 1)):
            self.vel_msg.linear.x = 1
            self.vel_msg.angular.z = 2*(self.dist_left_f-self.dist_left_r)
            self.velocity_publisher.publish(self.vel_msg)

        elif ((self.dist_left_f <= 0.3) & (self.dist_left_r <= 0.3)):
            self.vel_msg.linear.x = 1
            self.vel_msg.angular.z = -0.5
            self.velocity_publisher.publish(self.vel_msg)

        elif ((self.dist_left_f >= 1)):
            self.vel_msg.linear.x = 0.5
            self.vel_msg.angular.z = 0.5
            self.velocity_publisher.publish(self.vel_msg)

        else:
            self.vel_msg.linear.x = 1
            self.vel_msg.angular.z = 0
            self.velocity_publisher.publish(self.vel_msg)


    def __init__(self):
        self.dist_left_f = 0.3
        self.dist_left_r = 0.3
        self.dist_front = 1
        rospy.init_node('scan_and_go', anonymous=False)
        self.vel_msg = Twist()
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.listen()

move = Mover()
