# 이미지 상태가 안좋은 애를 이진화 시켜서 테스트

import easyocr
import cv2
import matplotlib.pyplot as plt

reader = easyocr.Reader(["ko", "en"])

img_path = "04.png"
img = cv2.imread(img_path)

result = reader.readtext(img_path)

print(result)

THRESHOLD = 0.6

for bbox, text, conf in result:
    if conf > THRESHOLD:
        print(text)
        cv2.rectangle(img, pt1=bbox[0], pt2=bbox[2], color=(0, 0, 255), thickness=3)

plt.figure(figsize=(8, 8))
plt.imshow(img[:, :, ::-1])
plt.axis("off")
plt.show()
