import cv2

# 웹캠 열기
cap = cv2.VideoCapture(0)  # 0은 기본 웹캠을 나타냅니다. 다른 카메라를 사용하려면 숫자를 변경하세요.

if not cap.isOpened():
    print("웹캠을 열 수 없습니다. 종료합니다.")
    exit()

while True:
    # 웹캠에서 프레임 읽기
    ret, frame = cap.read()

    if not ret:
        print("Hi")
        break

    # 프레임을 화면에 표시
    cv2.imshow("Webcam", frame)

    # 's' 키를 눌러 사진 저장
    if cv2.waitKey(1) & 0xFF == ord("s"):
        # 현재 시간을 파일 이름으로 사용
        filename = "captured_image.png"
        cv2.imwrite(filename, frame)
        print(f"{filename}을 저장했습니다.")
        break

# 작업 완료 후 정리
cap.release()
cv2.destroyAllWindows()
