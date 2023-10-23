import sys
import numpy as np
import cv2

src = cv2.imread("cat.bmp")

dst1 = cv2.flip(src, 1)  # 좌우
dst2 = cv2.flip(src, 0)  # 상하
dst3 = cv2.flip(src, -1)  # 상하&좌우

cv2.imshow("src", src)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)
cv2.waitKey()
cv2.destroyAllWindows()
