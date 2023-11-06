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

print('initialize object detection')
# initialize object detection
base_options = python.BaseOptions(model_asset_path='assets//efficientdet_lite0.tflite') #this is the model file
options = vision.ObjectDetectorOptions(base_options=base_options,
                                       score_threshold=0.5) #score threshold shows 
detector = vision.ObjectDetector.create_from_options(options)

def deleteTempFiles():

    subdirectories = ['temp//','code//__pycache__//'] #get all needed subdirectories to delete

    for subdir in subdirectories:

        dir_list = os.listdir(subdir) #get all file names in subdirectory
        #print(dir_list)
        for file in dir_list:
            os.remove(subdir+file) #delete each file

def main():
    
    #initialize camera
    CAM1 = cv2.VideoCapture(0) #change camera port if nesscary
    CAM1.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc('M','J','P','G')) #compress the camera footage or else rasp pi collapses
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

                    #print('Frame is found, proceding')

                    #save image for formatting
                    cv2.imwrite("temp//frame1.jpg",frame1)
                    frame1 = mp.Image.create_from_file("temp//frame1.jpg")
                    cv2.imwrite("temp//frame2.jpg",frame2)
                    frame2 = mp.Image.create_from_file("temp//frame2.jpg")

                    #get results
                    results1 = detector.detect(frame1)
                    results2 = detector.detect(frame2)

                    #print(results1,results2) #here for debug
                    #print('getting results')

                    distanceInLs, distanceInMeters, distanceHorizontal = twoCamDis(results1,results2) #this gives us the distance, look for 
                    #print(distanceInLs, distanceInMeters, distanceHorizontal) #print for debug
                    
                    #export annotated images to temp so that another 
                    image1 = np.copy(frame1.numpy_view())
                    annotated_image1,text1 = obj.visualizeObject(image1, results1)
                    rgb_annotated_image = cv2.cvtColor(annotated_image1, cv2.COLOR_BGR2RGB)
                    cv2.imwrite('temp//objDectCam1.jpg',rgb_annotated_image)
                    #cv2.imshow("image1",rgb_annotated_image) #this is to show the file, but one program in rasp pi may not be able to handle showing two images
                    image2 = np.copy(frame2.numpy_view())
                    annotated_image2,text2 = obj.visualizeObject(image2, results2)
                    rgb_annotated_image = cv2.cvtColor(annotated_image2, cv2.COLOR_BGR2RGB)
                    cv2.imwrite('temp//objDectCam2.jpg',rgb_annotated_image)
                    #cv2.imshow("image2",rgb_annotated_image) #this is to show the file, but one program in rasp pi may not be able to handle showing two images

                    #export the distance to a temp file so that anyother parrallel program can deal with it
                    with open('temp//distance.output', 'w') as fout:
                        if distanceInLs != None:
                            fout.write(f"{distanceInMeters},{distanceHorizontal}")
                        else:
                            fout.write('None')

                #else:
                    #print('Frames are not found')

                #userInterfaceShow(distanceInLs, distanceInMeters, distanceHorizontal)
                #if esc is pressed, break
                if cv2.waitKey(100) == 27:
                    break

    CAM1.release()
    CAM2.release()
    cv2.destroyAllWindows

if __name__ == '__main__':
    deleteTempFiles()
    main()
    #deleteTempFiles()