import cv2
import time

video = cv2.VideoCapture(0)
time.sleep(1)

while True:
    check, frame = video.read()
    cv2.imshow('My video', frame)

    key = cv2.waitKey(1)

    # 运行后可调用摄像头 📸️ 按 q 可退出
    if key == ord('q'):
        break

video.release()