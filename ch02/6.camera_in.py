import sys
import cv2

cap = cv2.VideoCapture(0)  # 기본 카메라 장치 열기

while True:
    ret, frame = cap.read()  # 카메라로부터 프레임을 정상적으로 받아오면 ret에는 True. frame에는 해당 프레임이 저장됨

    inversed = ~frame  # 현재 프레임 반전

    cv2.imshow("frame", frame)
    cv2.imshow("inversed", inversed)

    if cv2.waitKey(10) == 27:  # 일정시간 기다린 후 다음 프레임 처리
        break

cap.release()  # 사용한 자원 해제
cv2.destroyAllWindows()
