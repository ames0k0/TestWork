#!/usr/bin/env python

import cv2
import numpy as np


# SEE: https://stackoverflow.com/a/47922732
names = ['cam1.avi', 'cam2.avi'];
window_titles = ['left', 'front']

# cap = [cv2.VideoCapture(i) for i in names]
left = cv2.VideoCapture(names[0])
left_name = window_titles[0]

while True:
  ret, frame = left.read()
  if not ret:
    break

  cv2.imshow(left_name, frame)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break


if left is not None:
  left.release()

cv2.destroyAllWindows()


# def main():
# 
#   while (read):
#     cam1_frame = ''
#     cam2_frame = ''
# 
#     detect_humans = ''
#     match_detected_humans = ''
# 
# 
# if __name__ == '__main__':
#   main()
