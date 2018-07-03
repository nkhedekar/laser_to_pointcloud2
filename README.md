# laser_to_pointcloud2
A node to convert LaserScans to PointCloud2

##Usage:
The node subscribes to the `scan` topic and publishes to the `laser_point_cloud2` topic. These can be remapped as required in your implementation. This package depends upon `laser_geometry` which can be installed by `sudo apt-get install ros-kinetic-laser-geometry`. 

Thanks to The Contruct for its videos. 
