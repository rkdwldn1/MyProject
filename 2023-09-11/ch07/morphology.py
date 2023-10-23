import sys
import numpy as np
import cv2


src = cv2.imread("circuit.bmp", cv2.IMREAD_GRAYSCALE)

if src is None:
    print("Image load failed!")
    sys.exit()

se = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 3))
dst1 = cv2.erode(src, se)  # 이진 영상의 침식

dst2 = cv2.dilate(src, None)  # 이진 영상의 팽창

cv2.imshow("src", src)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()
