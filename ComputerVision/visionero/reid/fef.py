#!/usr/bin/env python

import cv2
import numpy as np

from utils import show_image

# SEE: https://stackoverflow.com/a/47922732
names = ['cam1.avi', 'cam2.avi'];
window_titles = ['left', 'front']

# cap = [cv2.VideoCapture(i) for i in names]
left = cv2.VideoCapture(names[0])
left_name = window_titles[0]
cap = left


#Randomly selecting 30 frames
frame_get = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size = 30)

#Storing captured frames in an array
frames = []
for i in frame_get:
  cap.set(cv2.CAP_PROP_POS_FRAMES, i)
  ret, frame = cap.read()
  if ret:
    frames.append(frame)


frame_median = np.median(frames, axis = 0).astype(dtype = np.uint8)
gray_frame_median = cv2.cvtColor(frame_median, cv2.COLOR_BGR2GRAY)


frame_tot = cap.get(cv2.CAP_PROP_FRAME_COUNT)


frame_count = 0
while (frame_count < frame_tot - 1):
  frame_count+=1
  ret, frame = cap.read()
  # Converting frame to grayscale
  gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  # Calculating Absolute Difference between Current Frame and Median Frame
  dframe = cv2.absdiff(gray_frame, gray_frame_median)

  # Applying Gaussian Blur to reduce noise
  blur_frame = cv2.GaussianBlur(dframe, (11,11), 0)
  # Binarizing frame - Thresholding
  ret, threshold_frame = cv2.threshold(blur_frame, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
  # Identifying Contours
  (contours, _ ) = cv2.findContours(threshold_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  # Drawing Boundary Boxes for each Contour
  for i in contours:
    x, y, width, height = cv2.boundingRect(i)
    cv2.rectangle(frame, (x,y), (x + width, y + height), (123,0,255), 2)
  show_image(frame)
  # video_writer.write(cv2.resize(frame, (640,480)))

print(frame_count)
# Releasing Video Object
cap.release()
# video_writer.release()
