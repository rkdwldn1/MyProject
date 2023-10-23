import cv2
import numpy as np

# 게임 화면 생성
width, height = 800, 600
screen = np.zeros((height, width, 3), dtype=np.uint8)

# 두더지 이미지 로드
mole_img = cv2.imread("mole.png")  # 두더지 이미지 파일을 로드해야 합니다.

# 손 위치 초기화
hand_x, hand_y = 0, 0

# 스코어 초기화
score = 0

while True:
    # 화면 초기화
    screen.fill((0, 0, 0))

    # 두더지 위치 설정 (랜덤 위치 또는 미리 정의된 위치)
    mole_x, mole_y = 400, 300

    # 두더지와 손의 충돌 감지
    mole_rect = cv2.Rect(mole_x, mole_y, mole_img.shape[1], mole_img.shape[0])
    hand_rect = cv2.Rect(hand_x, hand_y, 50, 50)  # 손의 크기와 위치를 적절히 조절하세요

    if mole_rect.colliderect(hand_rect):
        # 충돌 감지 시 스코어 증가
        score += 1

    # 두더지 이미지를 화면에 그림
    screen[
        mole_y : mole_y + mole_img.shape[0], mole_x : mole_x + mole_img.shape[1]
    ] = mole_img

    # 손의 위치를 화면에 그림 (색상, 크기 및 모양을 조절하세요)
    cv2.rectangle(screen, (hand_x, hand_y), (hand_x + 50, hand_y + 50), (0, 0, 255), -1)

    # 스코어 표시
    cv2.putText(
        screen, f"Score: {score}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2
    )

    # 화면을 업데이트
    cv2.imshow("Whack-a-Mole Game", screen)

    # 사용자의 키 입력을 확인하여 게임 종료
    key = cv2.waitKey(30)
    if key == 27:  # ESC 키를 누르면 게임 종료
        break

# 게임 종료 시 OpenCV 창 닫기
cv2.destroyAllWindows()
