# Video counting and store trafic 
The `PeopleCounter.py` script records the trafic of people and store them in a local mysql database with the datetime.
It also takes a picture each time it detects a passage and store it in local + in the DB in format: dateimeImg.png.

## Installation
OpenCV and numpy  are required for the image detection :
```sh
#!/bin/bash
 
sudo apt-get install -y build-essential cmake pkg-config
sudo apt-get install -y libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install -y libxvidcore-dev libx264-dev
sudo apt-get install -y libgtk2.0-dev
sudo apt-get install -y libatlas-base-dev gfortran
sudo apt-get install -y python2.7-dev python3-dev
 
cd ~
wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.1.0.zip
unzip opencv.zip
 
wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.1.0.zip
unzip opencv_contrib.zip
 
pip install numpy
 
cd ~/opencv-3.1.0/
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.1.0/modules \
    -D BUILD_EXAMPLES=ON ..
 
 
make
sudo make install
sudo ldconfig
```
## How to Use
### PeopleCounter

Script with 2 lines detector (exits and entrance in border of the screen).

Go in the folder where is the script:
```sh
cd ~/Video
sudo python peopleCounter.py
```

### PeopleCounter2

Script with 1 line detector in the middle of the screen.

Go in the folder where is the script:
```sh
cd ~/Video
sudo python peopleCounter2.py
```
You need to use sudo or give the right to write, because it will create the image in the pictures folder.
## What it does
The camera is now launched and everytime a people will go through an exit or entrance line, it will store the date in the database.
