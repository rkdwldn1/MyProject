import sys
import numpy as np
import cv2


src = cv2.imread("cloud1.jpg")

if src is None:
    print("Image load failed!")
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)


def on_trackbar(pos):  # 트랙바 조절 함수
    hmin = cv2.getTrackbarPos("H_min", "dst")
    hmax = cv2.getTrackbarPos("H_max", "dst")

    dst = cv2.inRange(src_hsv, (hmin, 150, 0), (hmax, 255, 255))
    cv2.imshow("dst", dst)


cv2.imshow("src", src)  # 원본 이미지 출력
cv2.namedWindow("dst")

cv2.createTrackbar("H_min", "dst", 90, 179, on_trackbar)
cv2.createTrackbar("H_max", "dst", 135, 179, on_trackbar)
on_trackbar(0)

cv2.waitKey()

cv2.destroyAllWindows()
