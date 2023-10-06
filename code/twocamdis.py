"""
Name: TwoCamDis 
Author: Jayden Chen
Purpose: 
    Get the distance of an object from Two Cameras

"""

import numpy as np

"""
Func: calcDis 
Author: Jayden Chen
Purpose: calculates the distance based on the equation: 

input: results from object detection
    
output:  width, orgin x of suitcase

remarks:

"""
def objProperties(detection_result) -> np.ndarray:
    properties = []

    for detection in detection_result.detections:

        #get object box dimensions and origin
        bbox = detection.bounding_box
        width = bbox.width
        height = bbox.height
        origin = (bbox.origin_x, bbox.origin_y)

        #get object category name and accuracy probability
        category = detection.categories[0]
        item = category.category_name
        score = category.score

        properties.append({'item':item,'score':score ,'width':int(width),'height':int(height),'origin':origin})

    return properties

"""
Func: calcDis 
Author: Jayden Chen
Purpose: calculates the distance based on the equation: 

input: results from object detection
    
output:  width, orgin x of suitcase

remarks:

"""
def plantProperties(detection_result) -> np.ndarray:
        
    for detection in detection_result.detections:

        #get object box dimensions and origin
        bbox = detection.bounding_box
        width = bbox.width
        originX = bbox.origin_x

        #get object category name and accuracy probability
        category = detection.categories[0]
        item = category.category_name
        if 'plant' in str(item):
            return width, originX
    
    return None, None

#test data 
#1m: 2.04 1.93 1.92 avg1.95
#1.25m: 1.82 1.86 avg1.85
#1.5m: 1.65 1.65, 1.68, 1.5 avg1.65
#1.75m: 1.5 1.51 1.41 avg1.5
#2m: 1.35 1.39 avg1.35

#P = b + a/(x + c)
#distance = L * (a / (P-b) -c)

#values for distance formula
with open('code/twoCamDisVariables.varfx','r') as fin:
    L = float(fin.readline().split()[1])
    a = float(fin.readline().split()[1])
    b = float(fin.readline().split()[1])
    c = float(fin.readline().split()[1])

"""
Func: calcDis 
Author: Jayden Chen
Purpose: calculates the distance based on the equation: 

input: P (the ratio of P1 and P2)
    
output: distance in meters, Ls

remarks:

"""
def calcDis(P):
    #P = b + a/(x*d + c)
    #x*d = a / (P-b) -c

    slopeMap = {1.95:(1,0.8),1.75:(1.25,0.6),1.6:(1.5,0.2),1.55:(1.75,0.4)}

    return round(((a/(P-b) + c)),4),round(((a/(P-b) + c)*L),4)
    
    #position = 1.95 #don't need to draw secant liness
    #return (P-position)*(-slopeMap[position][1]) + slopeMap[position][0]

"""
Func: twocamdis
Author: Jayden Chen
Purpose: returns the distance as fast as possible

input: results1, results2 from object detection
    
output: distance in meters, distance in Ls, distance in 

remarks: this version is different because it only considers one target instead of multiple
    
"""
def twoCamDis(results1,results2):

    P1,X1 = plantProperties(results1)
    P2,X2 = plantProperties(results2)

    if P1 != None:
        if P2 != None:
            #if raw2['item'] == 'suitcase':
            P = P1/P2
            distanceZMeters, distanceLMeters = calcDis(P)
            distanceX = X1

            return distanceLMeters, distanceZMeters, distanceX
        
    return None, None, None
        
if __name__ == '__main__':
    print(L,a,b,c)
    print(calcDis(1.5))