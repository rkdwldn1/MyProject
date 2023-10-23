import sys
import numpy as np
import cv2


src = cv2.imread("cells.png", cv2.IMREAD_GRAYSCALE)

if src is None:
    print("Image load failed!")
    sys.exit()

_, dst1 = cv2.threshold(
    src, 100, 255, cv2.THRESH_BINARY
)  # 100을 포함한 앞 부분은 0으로, 나머지는 255(1)로 표현
_, dst2 = cv2.threshold(
    src, 210, 255, cv2.THRESH_BINARY
)  # 210을 포함한 앞 부분은 0으로, 나머지는 255(1)로 표현

cv2.imshow("src", src)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()
