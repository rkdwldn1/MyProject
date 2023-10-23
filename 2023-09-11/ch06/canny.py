import sys
import numpy as np
import cv2


src = cv2.imread("building.jpg", cv2.IMREAD_GRAYSCALE)

if src is None:
    print("Image load failed!")
    sys.exit()

dst = cv2.Canny(src, 100, 200)  # 캐니 에지 검출 함수 (임력 영상, 하단 임계값, 상단 입계값)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()

cv2.destroyAllWindows()
