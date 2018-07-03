# laser_to_pointcloud2
A node to convert LaserScans to PointCloud2

## Usage:
Clone the repository into the src folder in your workspace - 

```
  git clone https://github.com/nkhedekar/laser_to_pointcloud2.git
  cd ..
  catkin build
  source devel/setup.bash
```

To run the node:

`rosrun laser_to_pointcloud2 laser_to_pc2.py`

The node subscribes to the `scan` topic and publishes to the `laser_point_cloud2` topic. These can be remapped as required in your implementation. This package depends upon `laser_geometry` which can be installed by `sudo apt-get install ros-kinetic-laser-geometry`. 

Thanks to The Contruct for its videos. 
