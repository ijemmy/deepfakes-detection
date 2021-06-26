import glob
import cv2
import numpy as np


def show(frame, frame_no):
  cv2.imshow('Frame', frame)
  # print(frame.shape)


def write(frame, frame_no):
  frame_no_padded = str(frame_no).rjust(3, '0')
  path = f'./output_folder/{frame_no_padded}.png'
  print(f'Writing to path {path}')
  cv2.imwrite(path, frame)


def read_and_process(filename, frame_action):
  cap = cv2.VideoCapture(filename)
  frame_no = 0

  if (cap.isOpened() == False):
    print("Error opening video stream or file")

  while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
      frame_action(frame, frame_no)
      if cv2.waitKey(25) and 0xFF == ord('q'):
        break
    else:
      break
    frame_no += 1

  cap.release()
  cv2.destroyAllWindows()


video_filenames = glob.glob('DeepfakeTIMIT/higher_quality/**/*.avi')
for filename in video_filenames:
  print("Displaying file: " + filename)
  read_and_process(filename, write)
