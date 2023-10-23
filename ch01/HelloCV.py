import sys
import cv2

print("Hello OpenCV", cv2.__version__)

img = cv2.imread("cloud.jpg")

if img is None:
    print("image load failed")
    sys.exit()

cv2.namedWindow("image")
cv2.imshow("image", img)
cv2.waitKey()

cv2.destoryAllWindows()
