#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import PointCloud2 as pc2
from laser_geometry import LaserProjection

pub = rospy.Publisher("laser_point_cloud2", pc2, queue_size=1)
projector = LaserProjection()

def laser_cb(msg):
	cloud = projector.projectLaser(msg)
	pub.publish(cloud)

def main():
	rospy.init_node("laser_to_pointcloud2", anonymous=True)
	sub = rospy.Subscriber("scan", LaserScan, laser_cb)
	rospy.spin()

if __name__=="__main__":
	try:
		main()
	except rospy.ROSInterruptException:
		pass
