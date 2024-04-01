import easyocr
import cv2
import numpy as np

img = cv2.imread('images/1.jpg')

reader = easyocr.Reader(['en'])
result = reader.readtext('images/1.jpg')

print(result)

# 矩形左上角和右上角的坐标，绘制一个绿色矩形
point_color = (0, 255, 0)  # BGR
thickness = 1
lineType = 4

fontcolor = (0, 255, 0)  # BGR
fontScale = 1

for (bbox, text, prob) in result:
    print(text)
    cv2.rectangle(img, bbox[0], bbox[2], point_color, thickness, lineType)
    cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_DUPLEX, fontScale, fontcolor, thickness, lineType)

    cv2.imshow("image", img)
cv2.waitKey(0)  # 等待按键
