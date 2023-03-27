import cv2
# 画像に平滑かフィルタを使用する
def smooth_filter(image):
    # カーネルサイズ
    kernel_size = 5
    # ガウシアンフィルタを適用
    # image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    # メディアンフィルタを適用
    image = cv2.medianBlur(image, kernel_size)
    # バイラテラルフィルタを適用
    # image = cv2.bilateralFilter(image, kernel_size, 75, 75)
    return image

if __name__ == '__main__':
    # 画像を読み込み
    image = cv2.imread('./Camera_1000001.jpg')
    # 画像を表示
    # cv2.imshow('image', image)
    # 画像に平滑かフィルタを使用する
    image = smooth_filter(image)
    # 画像を表示
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
