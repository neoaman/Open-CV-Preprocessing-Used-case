import cv2 as cv
import numpy as np

# blank = np.zeros((500,500,3),dtype='uint8')
blank = cv.imread('static/sampleimg.jpg')
cv.line(blank,(10,10),(50,50),(0,255,0),thickness=5)
# image, point1(x,y), point2(x,y), colour(r,g,b), thickness(+ve int), linetype(str)
cv.imshow('Rectangle',blank)

cv.waitKey(0)