import numpy as np
import cv2

img = cv2.imread("cat.bmp", cv2.IMREAD_COLOR)  # 사진 위에 도형 올리기
# img = np.full((400, 400, 3), 255, np.uint8) #흰 바탕에 도형 올리기

# 직선 그리기 함수 line
cv2.line(
    img, (50, 50), (200, 160), (0, 0, 255), 5
)  # x축과 y축, 선 색상 또는 밝기, 선 두께, 선 타입, 축소비율
cv2.line(img, (50, 20), (150, 160), (0, 0, 128))

# 사각형 그리기 함수 rectangle
cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 2)
cv2.rectangle(img, (70, 220), (180, 280), (0, 128, 0), -1)

# 원 그리기 함수 circle
cv2.circle(img, (300, 100), 30, (255, 255, 0), -1, cv2.LINE_AA)
cv2.circle(img, (300, 100), 60, (255, 0, 0), 3, cv2.LINE_AA)

# 다각형 그리기 함수 ploylines
pts = np.array([[250, 200], [300, 200], [350, 300], [250, 300]])
cv2.polylines(img, [pts], True, (255, 0, 255), 2)

# 문자열 출력 함수 putText
text = "Hello? OpenCV " + cv2.__version__
cv2.putText(
    img, text, (50, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1, cv2.LINE_AA
)

cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()
