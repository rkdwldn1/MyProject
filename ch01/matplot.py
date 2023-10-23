# import matplotlib.pyplot as plt
# import cv2

# imgBGR = cv2.imread("cloud.jpg")
# imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

# plt.axis("off")
# plt.imshow(imgRGB)
# plt.show()

# imgGray = cv2.imread("cat.bmp", cv2.IMREAD_GRAYSCALE)

# plt.axis("off")
# plt.imshow(imgGray, cmap="gray")
# plt.show()

import matplotlib.pyplot as plt
import cv2

imgBGR = cv2.imread("cat.bmp")
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
imgGray = cv2.imread("cloud.jpg", cv2.IMREAD_GRAYSCALE)

imgRED = cv2.imread("cloud2.jpg")
imgBLUE = cv2.imread("cloud3.jpg")

# 두 개의 영상을 함께 출력
plt.subplot(221), plt.axis("off"), plt.imshow(
    imgRGB
)  # 첫번째가 행, 두번째가 열, 세번째가 칸(총 2행 2열 중에 1번째)
plt.subplot(222), plt.axis("off"), plt.imshow(imgGray, cmap="gray")  # 총 2행 2열 중에 2번째 칸
plt.subplot(223), plt.axis("off"), plt.imshow(imgRED)  # 총 2행 2열 중에 3번째 칸 사진
plt.subplot(224), plt.axis("off"), plt.imshow(imgBLUE)  # 총 2행 2열 중에 4번째 칸 사진
plt.show()
