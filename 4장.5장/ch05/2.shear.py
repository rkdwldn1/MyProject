import sys
import numpy as np
import cv2


src = cv2.imread("tekapo.bmp")

if src is None:
    print("Image load failed!")
    sys.exit()

aff = np.array([[1, 0.3, 0], [0, 1, 0]], dtype=np.float32)  # 0.3의 값을 바꾸면 기울기가 달라짐

h, w = src.shape[:2]
dst = cv2.warpAffine(src, aff, (w + int(h * 0.3), h))
# dst = cv2.warpAffine(src, aff, (0, 0))

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()
