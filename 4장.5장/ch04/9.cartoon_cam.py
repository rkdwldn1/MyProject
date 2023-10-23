# 카툰 필터 카메라

import sys
import numpy as np
import cv2


def cartoon_filter(img):  # 카툰 필터
    h, w = img.shape[:2]  # 이미지의 사이즈를 받아옴
    img2 = cv2.resize(img, (w // 2, h // 2))  # 사이즈 반으로 줄이기(속도를 위해)

    blr = cv2.bilateralFilter(img2, -1, 20, 7)  # 블러 처리
    edge = 255 - cv2.Canny(img2, 80, 120)  # Canny : 엣지를 따는 부분
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

    dst = cv2.bitwise_and(blr, edge)  # blr처리한 필터와 edge를 딴 필터의 공통으로 겹치는 부분 출력
    dst = cv2.resize(dst, (w, h), interpolation=cv2.INTER_NEAREST)  # 사이즈 다시 키우기

    return dst


def pencil_sketch(img):  # 스케치 필터
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # cvtColor함수를 통해 gray모드로 이미지가 들어옴
    blr = cv2.GaussianBlur(gray, (0, 0), 3)  # 블러처리
    dst = cv2.divide(gray, blr, scale=255)  # 그레이를 블러로 나누기
    return dst


def blue_highlight(img):  # 이미지에서 파란색 색상 강조
    b, g, r = cv2.split(img)
    b = cv2.equalizeHist(b)
    g = cv2.equalizeHist(g)
    r = cv2.equalizeHist(r)
    result = cv2.merge((b, g, r))
    return result


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("video open failed!")
    sys.exit()


# 스페이스바 누를대마다 모드 변경
cam_mode = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    if cam_mode == 1:  # 스페이스 누를때마다 필터 바뀜
        frame = cartoon_filter(frame)
    elif cam_mode == 2:
        frame = pencil_sketch(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    elif cam_mode == 3:  # 새로운 필터 적용
        frame = blue_highlight(frame)

    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)

    if key == 27:
        break
    elif key == ord(" "):
        cam_mode += 1
        if cam_mode == 4:  # 필터 모드가 3 이상이면 0으로 초기화
            cam_mode = 0


cap.release()
cv2.destroyAllWindows()
