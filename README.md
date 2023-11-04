# Alternative Distance Detection with Stationary Computer Vision 

## Abstract

With more advancements in robotics, efficient communication through computer vision has become a subject of interest. The goal of this project is to develop an accurate, low-cost, low energy model for locating multiple objects through cameras paired with computer vision. Existing approaches for distance detection focus mainly on parallax or sonar with visible light, ultrasonics, infrared, or microwave lasers, which are either expensive, not accurate, or close ranged. Other approaches focus on highly trained neural network systems that require tremendous amounts of data and energy. In this paper, I present a method that uses two aligned cameras with object detection, creating a more accessible approach that relies less on the quality of the device and/or the trained machine learning model. Using Google’s Mediapipe for computer vision and two cameras, this method managed to achieve high success rates within three tests. It is theorized that this technology could be used for street infrastructure or other line-like places. In addition, this technology was tested with ROS2 and other computer vision technology, proving it to be a good, efficient component in robotic systems.  

### Keywords 

Computer Vision, Machine Vision, Object Detection, Gesture Detection, Mediapipe, Camera Technolgy, MQTT, Robotics, ROS2, Autonomous Vehicles 

## Quick Startup

Download this repository https://github.com/fa1k0or/Distance-Detection-with-Stationary-Computer-Vision 

And download all required packages in requirements.txt

And then execute run.py, 

and execute pubToMqtt.py for MQTT and visual.py for visualization.

### INTRODUCTION

Devices with significant vision computing power are necessary for more efficient autonomous systems. Many uprising, revolutionary robotic systems absolutely depend on complex systems of computer vision and location, such as automatic delivery systems. It is vital for these models to be perfected and therefore valuable to develop powerful camera detection models. However, it is difficult to extract 3-dimensional data from purely visual cameras.  

Many models have been developed to extract dimensional and distance data. Computer stereo vision that uses parallax and computer vision is used massively to do this very well (Fan et al. 2012). However, it is expensive and requires both cameras to be absolutely synchronized. Laser detecting and ranging, or Lidar (Wadinger et al. 2005) is another popular method of distance tracking, which calculates the distance through the rebounded light and the time it takes for the light to rebound. This method is also expensive and needs high processing power. Other approaches utilize highly trained neural networks, which require great amounts of data, processing power, and energy (Patterson et al. 2021). 

Since the techniques above are either expensive or not easily accessible, this method isn’t viable for street and other types of infrastructure that require high levels of implementation, high accessibility, and low costs. Smart cities that are optimized and automatic have been theorized to reduce threats such as urbanization and population growth (Drepaul 2020). Thus, developing accessible distance-finding technology is appealing. 

In this paper, I present a method that uses two aligned cameras with object detection, creating a more accessible approach that relies less on the quality of the device and/or the trained machine learning model. 

The contributions of this paper are: 

A. Describe an accessible approach to detect distances through computer vision and object detection (Figure 1). 

B. Assess the accuracy of such an approach. 

C. Prove that it is viable for high-performing robotic systems and other approaches. 

D. Discuss the limitations and implementations of such method.  

### Methodology  

 

## Results 

 

### Discussion 

