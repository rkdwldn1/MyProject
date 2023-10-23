import sys
import numpy as np
import cv2


def on_level_change(pos):
    value = pos * 16
    if value >= 255:
        value = 255

        img[:] = value
        cv2.imshow("image", img)


img = np.zeros((480, 640), np.uint8)

cv2.namedWindow("image")
cv2.createTrackbar("level", "image", 0, 16, on_level_change)
# 트랙바 이름, 트랙바를 생성할 창 이름, 트랙바 위치 초기값, 트랙바 최대값, 트랙바 위치가 변경될 때 마다 호출할 콜백 함수 이름

cv2.imshow("image", img)
cv2.waitKey()
cv2.destroyAllWindows()
