#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32MultiArray

# Robot Velocities
linear_vel = 0
angular_vel = 0

# Utilities
def PublishAll():
    print("nothing here")

# Callbacks
def CllbckVel(data):
    print(f"linear {data.data[0]}")
    print(f"ang {data.data[1]}")

def MainCallback():
    rospy.init_node('comm_motor')
    main_frequency = rospy.Rate(60)
    while not rospy.is_shutdown():
        main_frequency.sleep()

# Publisher

# Subscriber
sub_velocity = rospy.Subscriber("/robot/velocity", Float32MultiArray, 
                                        CllbckVel)

if __name__ == '__main__':
    try:
        MainCallback()
    except rospy.ROSInterruptException:
        pass