import sys
import cv2

img1 = cv2.imread("dog.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("dog.jpg", cv2.IMREAD_COLOR)

print("type(img1):", type(img1))
print("img1.shape:", img1.shape)
print("img2.shape:", img2.shape)
print("img2.dtype:", img2.dtype)

h, w = img2.shape[:2]
print("img2 size:{}x{}".format(w, h))

if len(img1.shape) == 2:
    print("img1 is a grayscale image")
if len(img1.shape) == 3:
    print("img1 is a truecolor image")

img1 = cv2.imread("dog.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("dog.jpg", cv2.IMREAD_COLOR)

im

# for y in range(h):
#     for x in range(w):
#         img1[y, x] = 255
#         img2[y, x] = [0, 0, 255]

# img1[:, :] = 255  # 하얀색화면 출력
# img2[:, :] = (0, 0, 255)  # 빨간색화면 출력

img1[80:250, 80:300] = 1  # 앞에 부분이 세로, 뒤에 부분이 가로
img2[80:250, 80:300] = 1
