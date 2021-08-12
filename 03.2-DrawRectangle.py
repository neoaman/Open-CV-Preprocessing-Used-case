import cv2 as cv
import numpy as np

# blank = np.zeros((500,500,3),dtype='uint8')
blank = cv.imread('static/sampleimg.jpg')
cv.rectangle(blank,(0,0),(250,250),(0,255,0,0.5),thickness=cv.FILLED)
# image, point1(x,y), point2(x,y), colour(r,g,b), thickness(int or cv.FILLED), linetype(str)
cv.imshow('Rectangle',blank)

cv.waitKey(0)