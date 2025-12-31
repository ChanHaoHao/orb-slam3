# ORB-SLAM3-STEREO-FIXED

This repository is a modified version of [ORB_SLAM3](https://github.com/zang09/ORB-SLAM3-STEREO-FIXED.git) from zang09, to perform orb-slam3 in dynamic scenes using ROS2, YOLO, SAM to remove dynamic objects
--- 

## Modification
- Succesfully tested in **Ubuntu 24.04** and **ROS2 Jazzy** (with OpenCV 4.6.0)
- It is only modified for RGB-D mode running with [Bonn RGB-D Dynamic Dataset](https://www.ipb.uni-bonn.de/data/rgbd-dynamic-dataset/index.html), removes MapPoints close to the masks.

## How to build
0. Clone the repo
1. Install Eigen3==3.4.0, 
```
sudo apt install libeigen3-dev
```
2. Install OpenCV==4.6.0 and ros-jazzy-cv-bridge==4.1.0
```
sudo apt install libopencv-dev
``` 
3. Install Pangolin==v0.9.2
```
sudo apt install libepoxy-dev

# Clone it in the root path where you cloned orb-slam3
git clone https://github.com/stevenlovegrove/Pangolin
cd ./Pangolin
git checkout v0.9.2
mkdir build
cd build
cmake ..
make
```
4. Install ORB-SLAM3
 ```
 cd $ORB_SLAM3_ROOT_PATH/ORB-SLAM3
chmod +x build.sh

./build.sh
```
5. Install Sophus
```
cd $ORB_SLAM3_ROOT_PATH/ORB-SLAM3/ThirdParty/Sophus/build
sudo make install
```

## Run the code
After building this orb-slam3 for ROS2, head over to [orb-slam3-ros-wrapper](https://github.com/ChanHaoHao/orb-slam3-ros-wrapper) for further instructions.