# import cv2
# import numpy as np
# from utility import *
# # -----------------------------------------------------------------
# path = "sample.tif"
# widthImg = 700
# heightImg = 700
# # -----------------------------------------------------------------
# # -----------------------------------------------------------------
# img = cv2.imread(path)

# img = cv2.resize(img,(widthImg,heightImg))
# imgContours = img.copy()

# imgBiggestContours = img.copy()
# imgBiggest_1Contours = img.copy()
# # preprocessing Image
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
# imgCanny = cv2.Canny(imgBlur,10,50)

# # -----------------------------------------------------------------
# # finding contures
# countours,hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
# cv2.drawContours(imgContours,countours,-1,(0,255,0),10)

# recCont = rectContours(countours)

# biggestCont = getCornerpoints(recCont[0])
# print('biggestCont >>> ',biggestCont)


# biggestCont_1 = getCornerpoints(recCont[10])
# print('biggestCont_1 >>> ',biggestCont_1)


# if biggestCont.size != 0 and biggestCont_1.size != 0:
#     cv2.drawContours(imgBiggestContours,biggestCont,-1,(0,255,0),10)
#     cv2.drawContours(imgBiggest_1Contours,biggestCont_1,-1,(0,255,0),10)

 
# # -----------------------------------------------------------------
# # cv2.imshow("original",imgGray)
# # cv2.imshow("original",imgBlur)
# # cv2.imshow("original",imgCanny)
# cv2.imshow("original",imgBiggest_1Contours)

# # cv2.imshow("original",img)
# cv2.waitKey(0)


import numpy as np
import cv2
from imutils.perspective import four_point_transform



def show_images(titles, images, wait=True):
    """Display multiple images with one line of code"""

    for (title, image) in zip(titles, images):
        cv2.imshow(title, image)

    if wait:
        cv2.waitKey(0)
        cv2.destroyAllWindows()



# declare some variables
height = 800
width = 600
green = (0, 255, 0) # green color
red = (0, 0, 255) # red color
white = (255, 255, 255) # white color
questions = 5
answers = 5
correct_ans = [0, 2, 1, 3, 4]



def get_rect_cnts(contours):
    rect_cnts = []
    for cnt in contours:
        # approximate the contour
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
        # if the approximated contour is a rectangle ...
        if len(approx) == 4:
            # append it to our list
            rect_cnts.append(approx)
    # sort the contours from biggest to smallest
    rect_cnts = sorted(rect_cnts, key=cv2.contourArea, reverse=True)
    
    return rect_cnts




img = cv2.imread('./fwdsampleflapimages/5014612711366.tif')
img = cv2.resize(img, (width, height))
img_copy = img.copy() # for display purposes
img_copy1 = img.copy() # for display purposes

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur_img = cv2.GaussianBlur(gray_img, (5, 5), 0)
edge_img = cv2.Canny(blur_img, 10, 70)

# find the contours in the image
contours, _ = cv2.findContours(edge_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
show_images(['canny image'], [edge_img]) # helper function in helper.py file

# draw the contours
cv2.drawContours(img, contours, -1, green, 3)

rect_cnts = get_rect_cnts(contours)
# warp perspective to get the top-down view of the document
document = four_point_transform(img_copy, rect_cnts[0].reshape(4, 2))
doc_copy = document.copy()  # for display purposes
doc_copy1 = document.copy() # for display purposes

cv2.drawContours(img_copy, rect_cnts, -1, green, 3)
# helper function in helper.py file
show_images(['contour image'], [img_copy])