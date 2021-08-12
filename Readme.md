# Table of Contents
1. [Reading Images and Video](#-1.-reading-images-and-video)
2. [Resizing and Reshaping](#-2.-resizing-and-rescaling)
3. [Draw on image Rectangle,Circle,Line](#-3.-draw-on-image)

# Image preprocessing with OpenCV

Image preprocessing is an emerging field in data science, processing an unstructured data like image is never been simple without CV. 

#### Install required packages
```sh
pip install opencv-contrib-python
```
## 1. Reading Images and Video <a name='-1.-reading-images-and-video'></a>   
### 1.1 Read image
```py
import cv2 as cv

# Read image file using imread method
img = cv.imread('path/to/image.jpg')
# View image using the imshow method
cv.imshow('window name',img)
cv.waitKey(0) # 0 will set no time limit untill we press a key.
```
### 1.2 Read video
```py
import cv2 as cv

# Can able to yield frames from video using VideoCapture method, it takes video path(str) or webcam (int : 0,1...) as input argument.
capture = cv.VideoCapture('path/to/video.mp4') 
while True:
    isTrue,frame = capture.read()
    if isTrue :
        cv.imshow("Seed",frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

```
## 2. Resizing and Rescaling <a name='-2.-resizing-and-rescaling'></a>   
### 2.1 Rescaling video and image   
Using resize method, we can change resize the image
```python
import cv2 as cv

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

img = cv.imread('path/to/image.jpg')
cv.imshow('Window name',rescaledFrame(img))

capture = VideoCapture('path/to/video/mp4')
while True:
    isTrue,frame = capture.read()

    frame_rescaled = rescaleFrame(frame,0.75)
    cv.imshow('Video resized',frame)
    if waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindow()
        
```
### 2.2 Resizing Frame   
We can resize the video frame with the set method, where **3** represented as **width** and we represent **4** as **height**   
<details>
  <summary>Expand see more parameters ...</summary>
  
  - POS_MSEC = **0**,
  
  - POS_FRAMES = **1**,
  
  - POS_AVI_RATIO = **2**,
  
  - FRAME_WIDTH = **3**,
  
  - FRAME_HEIGHT = **4**,
  
  - FPS = **5**,
  
  - FOURCC = **6**,
  
  - FRAME_COUNT = **7**,
  
  - FORMAT = **8**,
  
  - MODE = **9**,
  
  - BRIGHTNESS = **10**,
  
  - CONTRAST = **11**,
  
  - SATURATION = **12**,
  
  - HUE = **13**,
  
  - GAIN = **14**,
  
  - EXPOSURE = **15**,
  
  - CONVERT_RGB = **16**,
  
  - WHITE_BALANCE_BLUE_U = **17**,
  
  - RECTIFICATION = **18**,
  
  - MONOCHROME = **19**,
  
  - SHARPNESS = **20**,
  
  - AUTO_EXPOSURE = **21**,
  
  - GAMMA = **22**,
  
  - TEMPERATURE = **23**,
  
  - TRIGGER = **24**,
  
  - TRIGGER_DELAY = **25**,
  
  - WHITE_BALANCE_RED_V = **26**,
  
  - ZOOM = **27**,
  
  - FOCUS = **28**,
  
  - GUID = **29**,
  
  - ISO_SPEED = **30**,
  
  - BACKLIGHT = **32**,
  
  - PAN = **33**,
  
  - TILT = **34**,
  
  - ROLL = **35**,
  
  - IRIS = **36**,
  
  - SETTINGS = **37**,
  
  - BUFFERSIZE = **38**,
  
  - AUTOFOCUS = **39**,
  
  - SAR_NUM = **40**,
  
  - SAR_DEN = **41**,
  
  - BACKEND = **42**,
  
  - CHANNEL = **43**,
  
  - AUTO_WB = **44**,
  
  - WB_TEMPERATURE = **45**,
  
  - CODEC_PIXEL_FORMAT = **46**,
  
  - BITRATE = **47**,
  
  - ORIENTATION_META = **48**,
  
  - ORIENTATION_AUTO = **49**
</details>



[Read the Doc](https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html#ggaeb8dd9c89c10a5c63c139bf7c4f5704da6223452891755166a4fd5173ea257068)
```python
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
```

## 3. Draw on Image <a name="-3.-draw-on-image"></a>   
```python
import cv2 as cv
import numpy as np
blank = np.zeros((500,500,3),dtype='uint8')
```
Whenever we create a blank image, we pass 3 arguments in `height`, `width` and `colour` channels.   
**uint8** is an image type   
#### Paint the blank canvas to a colour   
```python
blank[:] = 0,255,0 # Green for all the pixels
cv.imshow('Green canvas',blank)
cv.waitKey(0)
```
#### Paint specific area of the canvas to certain colour   
```python

# Paint all Pixels
blank[:] = 0,255,0 # Green for all the pixels
cv.imshow('Green canvas',blank)

blank[0:100,10:100] = 255,0,0 # Row 0 to 100 and then column 10:100
cv.imshow('Green canvas',blank)

blank[0:100,200:300] = 0,0,255 # Row 0 to 100 and then column 200:300
cv.imshow('Green canvas',blank)
cv.waitKey(0)
```
#### Draw a Rectangle
```python
blank = cv.imread('static/sampleimg.jpg')
cv.rectangle(blank,(0,0),(250,250),(0,255,0,0.5),thickness=cv.FILLED)
# image, point1(x,y), point2(x,y), colour(r,g,b), thickness(int or cv.FILLED), linetype(str)
cv.imshow('Rectangle',blank)

cv.waitKey(0)
```
#### Draw a Circle
```python
blank = cv.imread('static/sampleimg.jpg')
cv.circle(blank,(blank.shape[1]//2,blank.shape[1]//2),40,(0,255,0),thickness=1)
# image, cenetr point(x,y), redious(int), colour(r,g,b), thickness(int or cv.FILLED), linetype(str)
cv.imshow('Rectangle',blank)

cv.waitKey(0)
```
#### Draw a Line
```python
blank = cv.imread('static/sampleimg.jpg')
cv.line(blank,(10,10),(50,50),(0,255,0),thickness=5)
# image, point1(x,y), point2(x,y), colour(r,g,b), thickness(+ve int), linetype(str)
cv.imshow('Rectangle',blank)

cv.waitKey(0)
```
