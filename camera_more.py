import cv2
import streamlit as st
from datetime import  datetime

st.title('Motion Detector')
start = st.button('Start Camera')

if start:
    # 初始化显示图像的空占位符
    streamlit_image = st.image([])
    # 打开默认摄像头
    camera = cv2.VideoCapture(1)

    while True:
        # 从摄像头捕获一帧
        check, frame = camera.read()
        # 将BGR图像转换为RGB以便Streamlit显示
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # 获取当前时间
        now = datetime.now()

        # 在帧上添加文字
        # cv2.putText(img=frame, text='Hello', org=(50,50),
        #             fontFace=cv2.FONT_HERSHEY_PLAIN,color=(20,100,200),
        #             thickness=2,lineType=cv2.LINE_AA,fontScale=2
        #             )


        # 获取 day 和 time 添加到 frame
        cv2.putText(img=frame, text=now.strftime("%A"), org=(30, 80),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=3,
                    color=(255, 255, 255),
                    thickness=2, lineType=cv2.LINE_AA)
        cv2.putText(img=frame, text=now.strftime("%H:%M:%S"), org=(30, 140),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=3, color=(255, 0, 0),
                    thickness=2, lineType=cv2.LINE_AA)
        # 在Streamlit应用中显示处理后的帧
        streamlit_image.image(frame)