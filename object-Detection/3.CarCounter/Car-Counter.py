import numpy as np
from ultralytics import YOLO
import cv2
import cvzone
import math
from sort import *

cap = cv2.VideoCapture("../Videos/cars.mp4")  # For Video

model = YOLO("../Yolo-Weights/yolov8n.pt")

classNames = [  # 클래스 정의
    "person",
    "bicycle",
    "car",
    "motorbike",
    "aeroplane",
    "bus",
    "train",
    "truck",
    "boat",
    "traffic light",
    "fire hydrant",
    "stop sign",
    "parking meter",
    "bench",
    "bird",
    "cat",
    "dog",
    "horse",
    "sheep",
    "cow",
    "elephant",
    "bear",
    "zebra",
    "giraffe",
    "backpack",
    "umbrella",
    "handbag",
    "tie",
    "suitcase",
    "frisbee",
    "skis",
    "snowboard",
    "sports ball",
    "kite",
    "baseball bat",
    "baseball glove",
    "skateboard",
    "surfboard",
    "tennis racket",
    "bottle",
    "wine glass",
    "cup",
    "fork",
    "knife",
    "spoon",
    "bowl",
    "banana",
    "apple",
    "sandwich",
    "orange",
    "broccoli",
    "carrot",
    "hot dog",
    "pizza",
    "donut",
    "cake",
    "chair",
    "sofa",
    "pottedplant",
    "bed",
    "diningtable",
    "toilet",
    "tvmonitor",
    "laptop",
    "mouse",
    "remote",
    "keyboard",
    "cell phone",
    "microwave",
    "oven",
    "toaster",
    "sink",
    "refrigerator",
    "book",
    "clock",
    "vase",
    "scissors",
    "teddy bear",
    "hair drier",
    "toothbrush",
]

mask = cv2.imread("mask.png")  # 마스크 이미지 불러오기

# Tracking / 객체 추적을 위한 SORT 초기화
tracker = Sort(max_age=20, min_hits=3, iou_threshold=0.3)

# 차량을 계산할 영역 정의 (화면 좌픅 상단부터 우측 상단까지의 선)
limits = [400, 297, 673, 297]
totalCount = []

while True:
    # 동영상 프레임 읽어오기
    success, img = cap.read()
    imgRegion = cv2.bitwise_and(img, mask)

    # 그래픽 이미지를 동영상에 오버레이
    imgGraphics = cv2.imread("graphics.png", cv2.IMREAD_UNCHANGED)
    img = cvzone.overlayPNG(img, imgGraphics, (0, 0))

    # YOLO 모델로 객체 검출 수행
    results = model(imgRegion, stream=True)

    # 검출된 객체 정보를 저장할 배열 초기화
    detections = np.empty((0, 5))

    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box 좌표 추출
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            # cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)
            w, h = x2 - x1, y2 - y1

            # Confidence 추출
            conf = math.ceil((box.conf[0] * 100)) / 100
            # 객체 클래스 추출
            cls = int(box.cls[0])
            currentClass = classNames[cls]

            # 차량 클래스에 대한 검출 및 신뢰도 조건
            if (
                currentClass == "car"
                or currentClass == "truck"
                or currentClass == "bus"
                or currentClass == "motorbike"
                and conf > 0.3
            ):
                # cvzone.putTextRect(img, f'{currentClass} {conf}', (max(0, x1), max(35, y1)),
                #                    scale=0.6, thickness=1, offset=3)
                # cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=5)
                currentArray = np.array([x1, y1, x2, y2, conf])
                detections = np.vstack((detections, currentArray))
    # SORT를 사용하여 객체 추적 수행
    resultsTracker = tracker.update(detections)

    # 지정된 영역을 나타내는 선 그리기(차량 통과 영역)
    cv2.line(img, (limits[0], limits[1]), (limits[2], limits[3]), (0, 0, 255), 5)

    for result in resultsTracker:
        x1, y1, x2, y2, id = result
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        print(result)

        # 객체의 Bounding Box 그리기
        w, h = x2 - x1, y2 - y1
        cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=2, colorR=(255, 0, 255))

        # 객체 ID와 함께 텍스트 표시
        cvzone.putTextRect(
            img,
            f" {int(id)}",
            (max(0, x1), max(35, y1)),
            scale=2,
            thickness=3,
            offset=10,
        )

        # 객체 중심에 원 그리기
        cx, cy = x1 + w // 2, y1 + h // 2
        cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

        # 차량이 통과한 영역 내부인지 확인하고 개수 세기
        if limits[0] < cx < limits[2] and limits[1] - 15 < cy < limits[1] + 15:
            if totalCount.count(id) == 0:
                totalCount.append(id)
                cv2.line(
                    img, (limits[0], limits[1]), (limits[2], limits[3]), (0, 255, 0), 5
                )

    # cvzone.putTextRect(img, f' Count: {len(totalCount)}', (50, 50))
    # 차량 개수를 화면에 표시
    cv2.putText(
        img,
        str(len(totalCount)),
        (255, 100),
        cv2.FONT_HERSHEY_PLAIN,
        5,
        (50, 50, 255),
        8,
    )

    # 결과 동영상 표시
    cv2.imshow("Image", img)
    # cv2.imshow("ImageRegion", imgRegion)
    cv2.waitKey(1)
