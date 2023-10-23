from ultralytics import YOLO
import cv2

src = cv2.imread("Images/9.webp")
src = cv2.resize(src, (1024, 683), interpolation=cv2.INTER_AREA)

model = YOLO("../Yolo-Weights/yolov8n.pt")  # 욜로 실행
results = model(src, show=True)
cv2.waitKey(0)
