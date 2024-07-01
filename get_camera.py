import os
import glob
import time
import cv2
from emailings import  send_email

# 创建 images 文件夹，如果不存在
if not os.path.exists('images'):
    os.makedirs('images')

# 这个地方打开摄像头 如果 数字 0 不行🙅 用 1试试
video = cv2.VideoCapture(1)
time.sleep(1)

if not video.isOpened():
    print("摄像头未打开")
    exit()

first_frame = None
status_list = []
count = 1

while True:
    status = 0
    check, frame = video.read()
    if not check:
        print("未能读取帧")
        break

    # 1. 转为灰度图像
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_frame_gau
        continue

    # 2. 计算差异
    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)
    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # 3. 找轮廓并绘制矩形
    contours, _ = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) < 10000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        if rectangle.any():
            status = 1
            # 当出现物体时 记录下 images
            cv2.imwrite(f'images/{count}.png', frame)
            count = count + 1
            all_images = glob.glob('images/*.png')
            if all_images:  # 检查是否为空
                index = int(len(all_images) / 2)
                images_with_object = all_images[index]

    status_list.append(status)
    status_list = status_list[-2:] # 取最后2个

    # 这个时候 就是物体离开🏃的时候
    if status_list[0] == 1 and status_list[1] == 0:
        send_email()

    cv2.imshow('Video', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
