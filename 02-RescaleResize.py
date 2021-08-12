import cv2 as cv

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

img = cv.imread('static/sampleimg.jpg')
cv.imshow('Sample Image',rescaleFrame(img,5))
cv.waitKey(0) # 0 will set no time limit untill we press a key.



capture = cv.VideoCapture('static/sampleseed.mp4') 
while True:
    isTrue,frame = capture.read()
    if isTrue :
        cv.imshow("Seed",rescaleFrame(frame,0.5)) # We can Rescale the frame to 0.5
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()