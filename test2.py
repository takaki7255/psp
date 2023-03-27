import cv2
import numpy as np

# 画像の読み込み
img = cv2.imread("./avg.jpg")

# gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 閾値250で2値化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)

# 収縮処理
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(thresh, kernel, iterations=1)

# 膨張処理
dilation = cv2.dilate(erosion, kernel, iterations=3)

erosion = cv2.erode(dilation, kernel, iterations=2)

# 最小外接円の描画
contours, hierarchy = cv2.findContours(erosion, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for i, cnt in enumerate(contours):
    # 最小外接円
    center, radius = cv2.minEnclosingCircle(cnt)
    # 円の描画
    cv2.circle(img, (int(center[0]), int(center[1])), int(radius), (0, 255, 0), 2)


cv2.imshow("img", img)
cv2.imshow("gray", gray)
cv2.imshow("thresh", thresh)
cv2.imshow("erosion", erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("mask.jpg", erosion)
