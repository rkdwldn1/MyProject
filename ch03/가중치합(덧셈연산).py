import sys
import numpy as np
import cv2

src1 = cv2.imread("sky.jpg")
src2 = cv2.imread("cloud1.jpg")
dst = cv2.addWeighted(src1, 0.3, src2, 0.7, 0, dst=None, dtype=None)


cv2.imshow("dst1", dst)  # 이미지 출력 imshwo(이름, 이미지)
cv2.waitKey()  # 이미지를 계속 띄우는 함수
cv2.destroyAllWindows()
