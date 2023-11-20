"""
Name: Main
Author: Jayden Chen
Purpose: 
    
"""

import os
import cv2
import numpy as np

def main():
    return 0

if __name__ == "__main__":
    img = cv2.imread('assets//template.jpg')
    imgorg = img.copy()

    while True:
        frame1 = cv2.imread('temp//objDectCam1.jpg', 0)
        frame2 = cv2.imread('temp//objDectCam2.jpg', 0)

        scale_percent = 50
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)

        resized = cv2.resize(frame1, dim, interpolation = cv2.INTER_AREA)
        resized = cv2.resize(frame2, dim, interpolation = cv2.INTER_AREA)

        img[1060:1060+width,50:50+height] = frame2[0:width,0:height]
        img[1060:1060+width,100+height:100+height*2] = frame1[0:width,0:height]

        with open('distance.output','r') as fin:
            msg = fin.readline()
            lDistance = fin.readline()
        if 'None' not in msg:
            img = cv2.putText(img, str(msg), (780,250), cv2.FONT_HERSHEY_SIMPLEX,  
                   1, (255,255,255), 2, cv2.LINE_AA) 
            #780,250
            center_coordinates = (480,225+160*int(lDistance))
            img = cv2.circle(img, center_coordinates, 30, (0,0,0), 1) 

        cv2.imshow('visuals',img)

        if cv2.waitKey(50) == 27:
            break
