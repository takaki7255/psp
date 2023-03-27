import cv2
import os

# 画像が保存されているフォルダのパス
folder_path = "./input"

# 画像ファイルのパスのリストを取得
image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".jpeg")]

# 動画の設定
frame_width = 640
frame_height = 480
fps = 30
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # codec
out = cv2.VideoWriter('output.mp4', fourcc, fps, (frame_width, frame_height))

for image_file in image_files:
    # 画像の読み込み
    img = cv2.imread(image_file)
    # メディアんフィルタを適用
    img = cv2.medianBlur(img, 5)
    # 画像のリサイズ
    img = cv2.resize(img, (frame_width, frame_height))
    # 画像を動画に追加
    out.write(img)

# 動画の保存
out.release()
