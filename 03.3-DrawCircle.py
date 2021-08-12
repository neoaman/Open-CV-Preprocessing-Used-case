import cv2 as cv
import numpy as np

# blank = np.zeros((500,500,3),dtype='uint8')
blank = cv.imread('static/sampleimg.jpg')
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,255,0),thickness=-1)
# image, cenetr point(x,y), redious(int), colour(r,g,b), thickness(int or cv.FILLED), linetype(str)
cv.imshow('Circle',blank)

cv.waitKey(0)