#!/usr/bin/env python

from collections import defaultdict

import cv2
import numpy as np

from utils import show_image


def contour_neighbors(contours, max_dist=100):
  new_list = defaultdict(list)
  for i, (x, y) in enumerate(contours):
    if not i:
      prev_x = x
      prev_y = y
      continue
    if (x - prev_x) < max_dist:
      if (y - prev_y) < max_dist//2:
        new_list[(prev_x, prev_y)].append((x, y))
        continue
    prev_x = x
    prev_y = y
  return new_list


def motion_detector():

  frame_count = 0
  previous_frame = None

  names = ['cam1.avi', 'cam2.avi'];
  cap = cv2.VideoCapture(names[0])

  while True:
    frame_count += 1

    ret, frame = cap.read()
    if not ret:
      break

    # 1. Load image; convert to RGB
    img_brg = frame
    img_rgb = cv2.cvtColor(src=img_brg, code=cv2.COLOR_BGR2RGB)

    if ((frame_count % 2) != 0):
      continue

    # 2. Prepare image; grayscale and blur
    prepared_frame = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    prepared_frame = cv2.GaussianBlur(src=prepared_frame, ksize=(5,5), sigmaX=0)

    # 3. Set previous frame and continue if there is None
    if (previous_frame is None):
      # First frame; there is no previous one yet
      previous_frame = prepared_frame
      continue

    # calculate difference and update previous frame
    diff_frame = cv2.absdiff(src1=previous_frame, src2=prepared_frame)
    if not np.any(diff_frame):
      continue

    previous_frame = prepared_frame

    # 4. Dilute the image a bit to make differences more seeable; more suitable for contour detection
    kernel = np.ones((5, 5))
    diff_frame = cv2.dilate(diff_frame, kernel, 1)

    # 5. Only take different areas that are different enough (>20 / 255)
    thresh_frame = cv2.threshold(src=diff_frame, thresh=20, maxval=255, type=cv2.THRESH_BINARY)[1]

    contours, _ = cv2.findContours(image=thresh_frame, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
    cnts = {}
    for contour in contours:
      area = cv2.contourArea(contour)
      if area < 50:
        # too small: skip!
        continue
      x, y, _, _ = cv2.boundingRect(contour)
      cnts[(x,y)] = contour

    cnts_neighbors = contour_neighbors(cnts.keys())

    for key, values in cnts_neighbors.items():
      cnn = []
      cnn.append(cnts.get(key))
      for value in values:
        cnn.append(cnts.get(value))
      cnn = np.array(cnn)
      cv2.fillConvexPoly(img_rgb, cnn, lineType=8, shift=0, color=(0, 255, 0))
      # cv2.drawContours(image=img_rgb, contours=cnn, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
      show_image(img_rgb)

    exit()

    contours = np.vstack(cnts.values())

    cv2.fillConvexPoly(img_rgb, contours, lineType=8, shift=0, color=(0, 255, 0))
    # cv2.drawContours(image=img_rgb, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

    show_image(img_rgb)
    continue

    if not np.any(contours):
      continue

    for contour in contours:
      area = cv2.contourArea(contour)
      if area < 50:
        # too small: skip!
        continue
      (x, y, w, h) = cv2.boundingRect(contour)
      cv2.rectangle(img=img_rgb, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=2)

    # img_edges = cv2.Canny(image=img_rgb, threshold1=50, threshold2=155)

    show_image(img_rgb)


motion_detector()
exit()


names = ['cam1.avi', 'cam2.avi'];
left = cv2.VideoCapture(names[0])
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



previous_frame = frames[0]
previous_frame = cv2.cvtColor(src=previous_frame, code=cv2.COLOR_BGR2RGB)
previous_frame = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2GRAY)
previous_frame = cv2.GaussianBlur(src=previous_frame, ksize=(5,5), sigmaX=0)


# 1. Load image; convert to RGB
img_brg = frames[6]
img_rgb = cv2.cvtColor(src=img_brg, code=cv2.COLOR_BGR2RGB)

# 2. Prepare image; grayscale and blur
prepared_frame = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
prepared_frame = cv2.GaussianBlur(src=prepared_frame, ksize=(5,5), sigmaX=0)

# calculate difference and update previous frame
diff_frame = cv2.absdiff(src1=previous_frame, src2=prepared_frame)

# 4. Dilute the image a bit to make differences more seeable; more suitable for contour detection
kernel = np.ones((5, 5))
diff_frame = cv2.dilate(diff_frame, kernel, 1)

# 5. Only take different areas that are different enough (>20 / 255)
thresh_frame = cv2.threshold(src=diff_frame, thresh=20, maxval=255, type=cv2.THRESH_BINARY)[1]

contours, _ = cv2.findContours(image=thresh_frame, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image=img_rgb, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

contours, _ = cv2.findContours(image=thresh_frame, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

# show_image(img_rgb)
for contour in contours:
  if cv2.contourArea(contour) < 50:
    # too small: skip!
    continue
  (x, y, w, h) = cv2.boundingRect(contour)
  cv2.rectangle(img=img_rgb, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=2)
