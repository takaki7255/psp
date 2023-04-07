import cv2
import numpy as np
from PIL import Image

def denoise(input):
    img = cv2.imread(input)
    # 画像のサイズを取得
    # height, width = img.shape[:2]

    # gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # median
    median = cv2.medianBlur(img, 5)

    # bilateral
    bilateral = cv2.bilateralFilter(img, 9, 75, 75)

    # 結果，マスク画像の表示
    cv2.imshow("input", img)
    cv2.imshow("gray", gray)
    cv2.imshow("median", median)
    cv2.imshow("bilateral", bilateral)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    denoise("./masked_img.jpg")
