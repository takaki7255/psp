# マスク処理
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import img_as_float
from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage.util import random_noise
import rawpy

# 画像の読み込み
img = cv2.imread("./run/psp/Camera_1000002のコピー.tif")

# 画像のサイズを取得
height, width = img.shape[:2]

# マスク画像の読み込み
mask = cv2.imread("./mask.jpg", 0)

# マスク画像のサイズを取得
mask_height, mask_width = mask.shape[:2]

# マスク画像のサイズを元画像のサイズに合わせる
# mask = cv2.resize(mask, (width, height))

# img = cv2.resize(img, (mask_width, mask_height))

# マスク処理
masked_img = cv2.bitwise_and(img, img, mask=mask)

# ここからノイズ除去
# median
median = cv2.medianBlur(masked_img, 5)
median = cv2.bitwise_and(median, median, mask=mask)

# bilateral
bilateral = cv2.bilateralFilter(masked_img, 9, 75, 75)
bilateral = cv2.bitwise_and(bilateral, bilateral, mask=mask)

# estimate the noise standard deviation from the noisy image
# sigma_est = np.mean(estimate_sigma(masked_img, multichannel=True))
# estimated noise standard deviation = 98.744137491433
# print("estimated noise standard deviation = {}".format(sigma_est))

# patch_kw = dict(patch_size=5,      # 5x5 patches
#                 patch_distance=6,  # 13x13 search area
#                 multichannel=True)

# denoise image
# denoise_img = denoise_nl_means(masked_img, h=1.15 * sigma_est, fast_mode=False,
#                                  **patch_kw,channel_axis=2)

# # slowalgorithm, sigma procvided
# denoise2 = denoise_nl_means(masked_img, h=0.8 * sigma_est, sigma=sigma_est,
#                                 fast_mode=False, **patch_kw,channel_axis=2)

# # fast algorithm, sigma provided
# denoise3 = denoise_nl_means(masked_img, h=0.6 * sigma_est, sigma=sigma_est,
#                                 fast_mode=True, **patch_kw,channel_axis=2)


# 結果，マスク画像の表示
print(mask_height, mask_width)
print(height, width)
cv2.imshow("Masked Image", masked_img)
# cv2.imshow("Mask", mask)
cv2.imshow("median", median)
# cv2.imshow("bilateral", bilateral)
# cv2.imshow("denoise_img", denoise_img)
# cv2.imshow("denoise2", denoise2)
# cv2.imshow("denoise3", denoise3)
cv2.waitKey(0)
cv2.destroyAllWindows()

# マスク画像の保存
# cv2.imwrite("masked_img.jpg", masked_img)
cv2.imwrite("./test_img/bilateral.jpg", bilateral)
cv2.imwrite("./test_img/median.jpg", median)
# cv2.imwrite("./test_img/skdenoise/denoise_img.tiff", denoise_img)
# cv2.imwrite("./test_img/skdenoise/denoise2.tiff", denoise2)
# cv2.imwrite("./test_img/skdenoise/denoise3.tiff", denoise3)
