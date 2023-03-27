import cv2

# 画像ファイルを読み込みます
img = cv2.imread('./run/psp/Camera_1000002のコピー.tif')

# ウィンドウを作成して、画像を表示します
cv2.namedWindow('image')
cv2.imshow('image', img)

# マウスイベントのコールバック関数を定義します
def crop_image(event, x, y, flags, param):
    global ix, iy, dragging

    if event == cv2.EVENT_LBUTTONDOWN:
        # マウスボタンが押されたときの処理
        ix, iy = x, y
        dragging = True

    elif event == cv2.EVENT_MOUSEMOVE:
        # マウスが移動したときの処理
        if dragging:
            # 現在の座標を保持し、長方形を描画します
            rect_img = img.copy()
            cv2.rectangle(rect_img, (ix, iy), (x, y), (0, 255, 0), 2)
            cv2.imshow('image', rect_img)

    elif event == cv2.EVENT_LBUTTONUP:
        # マウスボタンが離されたときの処理
        dragging = False

        # 選択範囲を切り抜きます
        cropped_img = img[iy:y, ix:x]

        # 切り抜いた画像を新しいウィンドウに表示します
        cv2.imshow('cropped image', cropped_img)
        cv2.imwrite('./test_img/cropped.jpg', cropped_img)

# マウスイベントのコールバック関数を設定します
cv2.setMouseCallback('image', crop_image)

# キー入力を待ちます
cv2.waitKey(0)

# ウィンドウを閉じます
cv2.destroyAllWindows()
