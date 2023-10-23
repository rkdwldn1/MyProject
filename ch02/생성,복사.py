import sys
import cv2

img1 = cv2.imread("HappyFish.jpg")
# img2 = img1  # 이미지2에 이미지1의 사진을 넣는다
# img3 = img1.copy()  # 이미지3에 이미지1의사진 복사
# img1.fill(255)  # 이미지1의 fill을 255로 변경했을경우 이미지2도 같이 변경되지만 이미지3는 별개라서 변경 안됨


img2 = img1[40:120, 30:150]
img3 = img1[40:120, 30:150].copy()  # 뒤에 copy()를 쓸 경우에는 원본의 값을 바꾸더라도 값이 변경이 안됨
img2.fill(0)  # 이미지2를 검은색으로 채워버리면 이미지1도 영향을 받는다는 의미


cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("img3", img3)
cv2.waitKey()
cv2.destroyAllWindows()
