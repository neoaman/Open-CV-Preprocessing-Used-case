import cv2 as cv
import numpy as np
blank = np.zeros((500,500,3),dtype='uint8')

# Paint all Pixels
blank[:] = 0,255,0 # Green for all the pixels
cv.imshow('Green canvas',blank)

blank[0:100,10:100] = 255,0,0 # Row 0 to 100 and then column 10:100
cv.imshow('Green canvas',blank)

blank[0:100,200:300] = 0,0,255 # Row 0 to 100 and then column 200:300
cv.imshow('Green canvas',blank)
cv.waitKey(0)
