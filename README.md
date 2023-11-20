# Alternative Distance Detection with Stationary Computer Vision 

## ABSTRACT

With more advancements in robotics, efficient communication through computer vision has become a subject of interest. The goal of this project is to develop an accurate, low-cost, low energy model for finding multiple objects through cameras paired with computer vision. Existing approaches for distance detection focus on parallax or sonar with visible light, or infrared lasers, which are expensive or close ranged. Other approaches focus on highly trained neural network systems that require tremendous amounts of data and energy. In this paper, I present a method that uses two aligned cameras with object detection, creating a more accessible approach that relies less on the quality of the device and/or the trained machine learning model. Using Google’s Mediapipe for computer vision and two web-cameras, this method managed to achieve high success rates within three tests. This technology was tested with ROS2 and other computer vision technology, proving it to be a good, efficient component in robotic systems. It is theorized that this technology could be used for smart city infrastructure or other line-like places that require detailed object locating.  

### KEYWORDS

Machine Vision, Distance Ranging, Object Detection, Smart Infrastructure, Mediapipe, MQTT

## INSTALLATION

    # clone the repo
    $ git clone https://github.com/fa1k0or/Distance-Detection-with-Stationary-Computer-Vision

    # change the working directory to this
    $ cd Distance-Detection-with-Stationary-Computer-Vision

    # install the requirements
    $ python3 -m pip install -r requirements.txt

## USAGE

    # starting camera feed, mediapipe, and distance
    python run.py

    # publish results to mqtt
    python pub.py

    # starting visuals
    python vsl.py

### ACKNOWLEDGEMENTS

This project has only been tested on Python 3.8.

See the pdf for more infomation on the project.

![Hardware Mind Map](/assets/images/readmeImages/HardwareSetup.png "hardware")



![Software Mind Map](/assets/images/readmeImages/figureSevenButDetailed2.png "software")
