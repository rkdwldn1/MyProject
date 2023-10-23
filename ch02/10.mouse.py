import sys
import numpy as np
import cv2

oldx = oldy = -1


def on_mouse(event, x, y, flags, param):
    global oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:  # 오른쪽 마우스 버튼 클릭
        oldx, oldy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:  # 마우스가 창 위에서 움직이는 경우
        if flags & cv2.EVENT_FLAG_LBUTTON:  # 마우스 왼쪽 버튼이 눌러져 있음
            cv2.line(img, (oldx, oldy), (x, y), (0, 0, 255), 4, cv2.LINE_AA)
            cv2.imshow("image", img)
            oldx, oldy = x, y


img = np.ones((480, 640, 3), dtype=np.uint8) * 255

cv2.imshow("image", img)
cv2.setMouseCallback("image", on_mouse)
cv2.waitKey()
