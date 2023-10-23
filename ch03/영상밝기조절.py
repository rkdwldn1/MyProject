import sys
import numpy as np
import cv2

# 그레이스케일 영상의 밝기 100만큼 증가시키기
# src = cv2.imread("lenna.bmp", cv2.IMREAD_GRAYSCALE)
# dst1 = cv2.add(src, 100)
# dst2 = src + 100
# dst2 = np.clip(src + 100.0, 0, 255).astype(np.uint8)

# 컬러 영상의 밝기 100만큼 증가시키기
src = cv2.imread("lenna.bmp")
dst1 = cv2.add(src, (100, 100, 100, 0))
dst2 = np.clip(src + 100.0, 0, 255).astype(np.uint8)

cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()
