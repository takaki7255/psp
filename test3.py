# なぜかうごきません
import cv2
import numpy as np
from PIL import Image

def tiff_to_jpg(input):
    img = Image.open(input)
    # filename
    filename = input.split('/')[-1].split('.')[0]
    # save
    img.save('./run/psp_jpg/' + filename + '.jpg')


def P(input):
    img = cv2.imread(input)
    # 画像のサイズを取得
    height, width = img.shape[:2]

    # マスク画像の読み込み
    mask = cv2.imread("./mask.jpg", 0)

    # マスク処理
    masked_img = cv2.bitwise_and(img, img, mask=mask)

    # ここからノイズ除去
    # median
    median = cv2.medianBlur(masked_img, 5)

    # bilateral
    bilateral = cv2.bilateralFilter(masked_img, 9, 75, 75)

    # 結果，マスク画像の表示
    cv2.imshow("input", img)
    cv2.imshow("Masked Image", masked_img)
    cv2.imshow("Mask", mask)
    cv2.imshow("median", median)
    cv2.imshow("bilateral", bilateral)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if __name__ == "__main__":
        tiff_to_jpg("./run/psp/Camera_1000002のコピー.tif")
        P("./run/psp_jpg/Camera_1000002のコピー.jpg")
