import cv2
import time

video = cv2.VideoCapture(0)

check1, frame1 = video.read()
time.sleep(1)

check2, frame2 = video.read()
time.sleep(1)

check3, frame3 = video.read()

print(frame3)
# 打出一些 帧
# [[[131 143 155]
#   [130 141 154]
#   [130 141 154]
#   ...
