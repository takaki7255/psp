import numpy as np
import cv2

# 画像の読み込み
inputImg = cv2.imread('./input/Camera_1000001.jpg')
# グレースケール変換
gray = cv2.cvtColor(inputImg, cv2.COLOR_BGR2GRAY)
# 収縮処理
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
gray = cv2.erode(gray, kernel,iterations=1)
# 膨張処理
gray = cv2.dilate(gray, kernel,iterations=1)
# 輪郭抽出
contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# 輪郭を描画
cv2.drawContours(inputImg, contours, -1, (0, 255, 0), 3)
# エッジ検出
# edgeImg = cv2.Canny(gray, 50, 150)
cv2.imshow('input', inputImg)
cv2.imshow('gray', gray)
# cv2.imshow('edge', edgeImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

