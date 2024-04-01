#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time

import cv2
import easyocr

video = "videos/video2.mkv"
result_video = "videos/demo-result-2.mp4"
# 读取视频
cap = cv2.VideoCapture(video)
# 获取视频帧率
fps_video = cap.get(cv2.CAP_PROP_FPS)
# 设置写入视频的编码格式
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
# 获取视频宽度
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# 获取视频高度
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
videoWriter = cv2.VideoWriter(result_video, fourcc, fps_video, (frame_width, frame_height))
frame_id = 0

# 矩形左上角和右上角的坐标，绘制一个绿色矩形
point_color = (0, 255, 0)  # BGR
thickness = 1
lineType = 4

fontcolor = (0, 255, 0)  # BGR
fontScale = 1

sum = 0
timef = 5  # 隔15帧保存一张图片

reader = easyocr.Reader(['en'])
result = 0
while (cap.isOpened()):
    ret, frame = cap.read()
    print(time.time())
    if ret == True:
        if sum % timef == 0:
            result = reader.readtext(frame)

        for (bbox, text, prob) in result:
            if (len(text) != 0):
                # print(text)
                cv2.rectangle(frame, (int(bbox[0][0]), int(bbox[0][1])), (int(bbox[2][0]), int(bbox[2][1])),
                              point_color, thickness, lineType)
                cv2.putText(frame, text, (int(bbox[0][0]), int(bbox[0][1])), cv2.FONT_HERSHEY_DUPLEX, fontScale,
                            fontcolor, thickness,
                            lineType)
        videoWriter.write(frame)
    else:
        videoWriter.release()
        break
    sum += 1

cap.release()
