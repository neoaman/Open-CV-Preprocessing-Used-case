import cv2 as cv

def changeRes(capture,width,height):
    capture.set(3,width)
    capture.set(4,height)
    capture.set(10,100) # Brightness

    return capture

capture = cv.VideoCapture(0)
capture_resize = changeRes(capture,180,180)
while True:
    isTrue,frame = capture.read()
    if isTrue :
        cv.imshow("Seed",frame) 
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
