# ORB-SLAM3-STEREO-FIXED

This repository is a modified version of [ORB_SLAM3](https://github.com/zang09/ORB-SLAM3-STEREO-FIXED.git) from zang09, and followed modifications from [Dennis Liu](https://hackmd.io/@dennis40816/rJqjMi6tJe).

--- 

## Modification
- Succesfully tested in **Ubuntu 24.04** and **ROS2 Jazzy**(with OpenCV 4.6.0)

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
1. Get EuRoC dataset
```
wget http://robotics.ethz.ch/~asl-datasets/ijrr_euroc_mav_dataset/machine_hall/MH_01_easy/MH_01_easy.zip
```
2. Unzip the dataset
```
unzip MH_01_easy.zip
mkdir MH01
mv mav0 MH01/mav0
```
3. Run the code
- EuRoC Monocular
```
./Examples/Monocular/mono_euroc \ 
    ./Vocabulary/ORBvoc.txt \ 
    ./Examples/Monocular/EuRoC.yaml \
    ./datasets/MH01 \
    ./Examples/Monocular/EuRoC_TimeStamps/MH01.txt
```
- EuRoC Monocular-Inertial
```
./Examples/Monocular-Inertial/mono_inertial_euroc \
    ./Vocabulary/ORBvoc.txt \
    ./Examples/Monocular-Inertial/EuRoC.yaml \
    ./datasets/MH01/ \
    ./Examples/Monocular-Inertial/EuRoC_TimeStamps/MH01.txt
```

- EuRoC Stereo
```
./Examples/Stereo/stereo_euroc \
    ./Vocabulary/ORBvoc.txt \
    ./Examples/Stereo/EuRoC.yaml \
    ./datasets/MH01/ \
    ./Examples/Stereo/EuRoC_TimeStamps/MH01.txt 
```

- EuRoC Stereo-Inertia (There is some issue with this currently!)