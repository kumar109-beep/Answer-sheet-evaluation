import cv2
import numpy as np


def rectContours(contours):
    rectangleContours = []
    for i in contours:
        area = cv2.contourArea(i)
        # print('Area >> ',area)

        if area > 50:
            param = cv2.arcLength(i,True)
            approx = cv2.approxPolyDP(i,0.02*param,True)
            # print("corner points >>>> ",len(approx))
            if(len(approx) == 4):
                print("")
                rectangleContours.append(i)

    rectCon = sorted(rectangleContours,key=cv2.contourArea,reverse=True)

    # print('rectCon >>> ',rectCon)
    return rectCon



def getCornerpoints(contour):
    param = cv2.arcLength(contour,True)
    approx = cv2.approxPolyDP(contour,0.02*param,True)

    return approx
