#!/usr/bin/env python

import cv2
import os
import time
timeout = time.time() + 60*1 

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

height , width , layers =  frame.shape
fourcc = cv2.cv.CV_FOURCC(*'XVID') # Incase of error replace with this - cv2.VideoWriter_fourcc(*'XVID')
fps=30
size = (width, height)
is_color=True
output_video = 'video.avi'

video = cv2.VideoWriter(output_video, fourcc, float(fps), size, is_color)

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    cv2.imwrite('frame.jpg',frame)
    img = cv2.imread('frame.jpg')
    video.write(img)

    if time.time() > timeout:
        break
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

video.release()
cv2.destroyWindow("preview")






