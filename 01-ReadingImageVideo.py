import cv2 as cv

# Read image file using imread method
img = cv.imread('static/sampleimg.jpg')
# View image using the imshow method
cv.imshow('Sample Image',img)
cv.waitKey(0) # 0 will set no time limit untill we press a key.


capture = cv.VideoCapture('static/sampleseed.mp4') 
while True:
    isTrue,frame = capture.read()
    if isTrue :
        cv.imshow("Seed",frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()