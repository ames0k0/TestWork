#!/usr/bin/env python

"""Simple Object Detection as a Human Detection

- Detect Circles: https://docs.opencv.org/3.4/d4/d70/tutorial_hough_circle.html
"""

import cv2
import numpy as np

from utils import show_image

frame = 'left.jpg'

image = cv2.imread(frame)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_blur = cv2.medianBlur(image_gray, 9)

threshold = 10

# contours, _ = cv2.findContours(image_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
canny_output = cv2.Canny(image_blur, threshold, threshold * 2)
contours, _ = cv2.findContours(canny_output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cnt = []
for c in contours:
  min_c = cv2.contourArea(c)
  if min_c > 30:
    cnt.append(c)

cv2.drawContours(image_blur, cnt, -1, (255,0,0), cv2.FILLED)
show_image(image_blur)


exit()

rows = image_gray.shape[0]
circles = cv2.HoughCircles(image_gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                           param1=100, param2=30,
                           minRadius=1, maxRadius=40)

src = image.copy()

if circles is not None:
  circles = np.uint16(np.around(circles))
  for i in circles[0, :]:
    center = (i[0], i[1])
    # circle center
    cv2.circle(src, center, 1, (0, 100, 100), 3)
    # circle outline
    radius = i[2]
    cv2.circle(src, center, radius, (255, 0, 255), 3)

show_image(src)
