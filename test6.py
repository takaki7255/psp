import cv2
import numpy as np

# 画像を読み込み
img = cv2.imread('./masked_img.jpg')

# HSL色空間に変換
hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

# 青色成分のみを抽出
blue_mask = cv2.inRange(hls, (80, 70, 0), (140, 255, 255))

# 密集度を計算
kernel = np.ones((9, 9), np.uint8)
density = cv2.dilate(blue_mask, kernel, iterations=1)

# グラデーションのための配列を作成
gradient = np.linspace(255, 0, 256, dtype=np.uint8)

# グラデーションによる色付け
colored_density = cv2.LUT(density, gradient)

# 密集度が高い箇所を青色にする
result = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
result[colored_density > 200] = [255, 0, 0]

# マスク処理
# マスク画像を読み込み
mask = cv2.imread('./mask.jpg', 0)

result = cv2.bitwise_and(result, result, mask=mask)

# 結果を表示して保存
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.imwrite('output_image.jpg', result)
cv2.destroyAllWindows()
