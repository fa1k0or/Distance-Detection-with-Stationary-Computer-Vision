"""
Name: Main
Author: Jayden Chen
Purpose: 
    

"""

from code.twoCamDis import twoCamDis
import code.objDetection as obj

import os
import cv2
import numpy as np

import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# initialize object detection
base_options = python.BaseOptions(model_asset_path='assets/efficientdet_lite0.tflite') #this is the model file change file name if nesscary
options = vision.ObjectDetectorOptions(base_options=base_options,
                                       score_threshold=0.5) #score threshold shows 
detector = vision.ObjectDetector.create_from_options(options)

def deleteTempFiles():
    subdirectories = ['temp//','code//__pycache__//']
    for subdir in subdirectories:
        dir_list = os.listdir(subdir)
        #print(dir_list)
        for file in dir_list:
            os.remove(subdir+file)

def main():
    
    #initialize camera
    CAM1 = cv2.VideoCapture(0)
    CAM1.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc('M','J','P','G'))
    CAM2 = cv2.VideoCapture(2)
    CAM2.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc('M','J','P','G'))
    #wait a while
    cv2.waitKey(100)

    print('starting')
 
    if CAM1.isOpened():
        print('One Camera Open')
        if CAM2.isOpened():
            print("Cameras Open!")

            while True:

                #get frame and success
                read_code1, frame1 = CAM1.read()
                read_code2, frame2 = CAM2.read()

                if read_code1 and read_code2:

                    print('Frame is found, proceding')

                    #save image for formatting
                    cv2.imwrite("temp/frame1.jpg",frame1)
                    frame1 = mp.Image.create_from_file("temp/frame1.jpg")
                    cv2.imwrite("temp/frame2.jpg",frame2)
                    frame2 = mp.Image.create_from_file("temp/frame2.jpg")

                    #get results
                    results1 = detector.detect(frame1)
                    results2 = detector.detect(frame2)

                    distanceInLs, distanceInMeters, distanceHorizontal = twoCamDis(results1)
                    distanceInLs, distanceInMeters, distanceHorizontal = twoCamDis(results2)
                    
                    #show frames
                    image1 = np.copy(frame1.numpy_view())
                    annotated_image1,text1 = obj.visualizeObject(image1, results1)
                    rgb_annotated_image = cv2.cvtColor(annotated_image1, cv2.COLOR_BGR2RGB)
                    image2 = np.copy(frame2.numpy_view())
                    annotated_image2,text2 = obj.visualizeObject(image2, results2)
                    rgb_annotated_image = cv2.cvtColor(annotated_image2, cv2.COLOR_BGR2RGB)

                else:
                    print('Frames are not found')

                #if esc is pressed, break
                if cv2.waitKey(60) == 27:
                    break

    CAM1.release()
    CAM2.release()
    cv2.destroyAllWindows

if __name__ == '__main__':
    deleteTempFiles()