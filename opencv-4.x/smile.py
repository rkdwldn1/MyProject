import cv2
import numpy as np
import random
import mediapipe as mp

# MediaPipe Face 모듈 초기화
mp_face = mp.solutions.face_detection
face_detection = mp_face.FaceDetection()

# MediaPipe Hands 모듈 초기화
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# 두더지 이미지 로드
mole_img = cv2.imread("mole.png")  # 두더지 이미지 파일을 로드해야 합니다.

# 카메라 열기
cap = cv2.VideoCapture(0)

# 게임 초기 설정
score = 0
game_started = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 게임 시작을 기다림
    if not game_started:
        # 얼굴 감지
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_results = face_detection.process(frame_rgb)

        if face_results.detections:
            # 얼굴이 감지되면 게임 시작
            game_started = True

    else:
        # 화면 초기화
        frame_height, frame_width, _ = frame.shape

        # 두더지 위치 설정 (랜덤 위치)
        mole_x = random.randint(0, frame_width - mole_img.shape[1])
        mole_y = random.randint(0, frame_height - mole_img.shape[0])

        # 두더지 이미지를 화면에 그립니다.
        frame[
            mole_y : mole_y + mole_img.shape[0], mole_x : mole_x + mole_img.shape[1]
        ] = mole_img

        # 손 감지 및 손의 위치 확인
        with hands as hands_context:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands_context.process(frame_rgb)

            if results.multi_hand_landmarks:
                # 손이 감지되면 두더지를 잡았는지 확인
                for hand_landmarks in results.multi_hand_landmarks:
                    # 손의 위치 (x, y)를 사용하여 두더지를 잡았는지 확인
                    hand_x = int(hand_landmarks.landmark[8].x * frame_width)
                    hand_y = int(hand_landmarks.landmark[8].y * frame_height)

                    if (
                        mole_x < hand_x < mole_x + mole_img.shape[1]
                        and mole_y < hand_y < mole_y + mole_img.shape[0]
                    ):
                        # 두더지를 잡았을 경우
                        score += 1

        # 스코어 표시
        cv2.putText(
            frame,
            f"Score: {score}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )

        # 화면 업데이트
        cv2.imshow("Whack-a-Mole Game", frame)

    # 키 입력 확인 (게임 시작 및 종료)
    key = cv2.waitKey(1)
    if key == 27:  # ESC 키를 누르면 게임 종료
        break

cap.release()
cv2.destroyAllWindows()
