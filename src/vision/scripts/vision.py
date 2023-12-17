#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32MultiArray
import cv2 as cv

# Robot Velocities
object_dist = 100   # px
object_angle = 90   # deg

# Publisher
publish_object_data = rospy.Publisher('robot/object', Float32MultiArray, queue_size=1)

# Subscriber

# Utilities
def PublishAll():
    object_data = Float32MultiArray()
    object_data.data.append(object_dist)
    object_data.data.append(object_angle)
    publish_object_data.publish(object_data)

def MainCallback():
    rospy.init_node('vision')
    main_frequency = rospy.Rate(60)
    while not rospy.is_shutdown():
        PublishAll()
        main_frequency.sleep()

if __name__ == '__main__':
    try:
        MainCallback()
    except rospy.ROSInterruptException:
        pass