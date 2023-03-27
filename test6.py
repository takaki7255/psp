import cv2
import numpy as np

# 画像の読み込み
img = cv2.imread('./masked_img.jpg')

# HLS色空間に変換
hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

# 青色部分のみを抽出
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([130, 255, 255])
mask = cv2.inRange(hls, lower_blue, upper_blue)

# 5x5のフィルタを定義
kernel = np.ones((5, 5), np.uint8)

# モルフォロジー演算でノイズを除去
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# 画像の大きさを取得
height, width = opening.shape[:2]

# 結果画像の初期化
result = np.zeros((height, width, 3), np.uint8)

# 周辺5x5の青色画素の密集度を求めて，密集度に応じてグラデーションで色つける
for i in range(2, height-2):
    for j in range(2, width-2):
        count = 0
        for k in range(i-2, i+3):
            for l in range(j-2, j+3):
                if opening[k, l] == 255:
                    count += 1
        if count == 0:
            result[i, j] = [255, 255, 255]
        else:
            blue_value = int(255 - (255 / 25) * count)
            result[i, j] = [255, 255 - blue_value, blue_value]

# 結果画像の保存
cv2.imwrite('./test_img/density_cv.jpg', result)
