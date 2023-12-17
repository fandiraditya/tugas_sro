#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32MultiArray

# Robot Velocities
linear_vel = 10
angular_vel = 10

# Publisher
publish_velocity = rospy.Publisher('robot/velocity', Float32MultiArray, queue_size=1)

# Subscriber
def CllbckObjectData(data):
    print(f"Object dist {data.data[0]}")
    print(f"Object ang {data.data[1]}")

subscribe_object_data = rospy.Subscriber('/robot/object', Float32MultiArray, CllbckObjectData)

# Utilities
def PublishAll():
    velocity_data = Float32MultiArray()
    velocity_data.data.append(linear_vel)
    velocity_data.data.append(angular_vel)
    publish_velocity.publish(velocity_data)

def MainCallback():
    rospy.init_node('mission')
    main_frequency = rospy.Rate(60)
    while not rospy.is_shutdown():
        PublishAll()
        main_frequency.sleep()

if __name__ == '__main__':
    try:
        MainCallback()
    except rospy.ROSInterruptException:
        pass