import cv2
import streamlit as st

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

        # 在帧上添加文字
        cv2.putText(img=frame, text='Hello', org=(50,50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN,color=(20,100,200),
                    thickness=2,lineType=cv2.LINE_AA,fontScale=2
                    )

        # 在Streamlit应用中显示处理后的帧
        streamlit_image.image(frame)