import cv2
import time

def frame_to_file(frame_name, frame):
  cv2.imwrite(frame_name, frame)

def show_image(image):
  cv2.imshow('show-image', image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  # exit()
