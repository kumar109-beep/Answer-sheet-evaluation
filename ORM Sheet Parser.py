import cv2
import numpy as np

# Read the original image
img = cv2.imread('test2.jpg') 

#widthImg = 700
#heightImg = 700
# -----------------------------------------------------------------
# -----------------------------------------------------------------
#img = cv2.resize(img,(widthImg,heightImg))
# Display original image
#cv2.imshow('Original', img)
#cv2.waitKey(0)

# Convert to graycsale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 

# Sobel Edge Detection
#sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
#sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
#sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
# Display Sobel Edge Detection Images
#cv2.imshow('Sobel X', sobelx)
#cv2.waitKey(0)
#cv2.imshow('Sobel Y', sobely)
#cv2.waitKey(0)
#cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
#cv2.waitKey(0)

# Canny Edge Detection
edges = cv2.Canny(image=img_blur, threshold1=50, threshold2=100) # Canny Edge Detection

contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0,255,0), 2)
# Display Canny Edge Detection Image
cv2.imshow('Canny Edge Detection', img)
cv2.waitKey(0)

cv2.destroyAllWindows()