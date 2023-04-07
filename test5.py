from PIL import Image, ImageFilter
import colorsys
import cv2

# 入力画像を開く
img = Image.open("./masked_img.jpg")

# 画像をRGBに変換する
rgb_img = img.convert("RGB")

# 画像の各ピクセルについて、周囲16ピクセルの青色画素の割合を計算する
width, height = rgb_img.size
blue_density = []
max = 0
min = 10000
for y in range(height):
    for x in range(width):
        blue_count = 0
        for i in range(-2, 3): # 範囲によってここの値を変える
            for j in range(-2, 3): # 範囲によってここの値を変える
                if i == 0 and j == 0:
                    continue
                px, py = x+i, y+j
                if px < 0 or px >= width or py < 0 or py >= height:
                    continue
                r, g, b = rgb_img.getpixel((px, py))
                if b > g and b > r:
                    blue_count += 1
        blue_density.append(blue_count / 24.0) # 範囲によってここの値を変える
        max = blue_count if blue_count > max else max
        min = blue_count if blue_count < min else min

print(max, min)

# # 密集度を0-255の範囲に変換する
# for i in range(len(blue_density)):
#     blue_density[i] = blue_density[i] * 255 / max

# for i in range(height):
#     for j in range(width):
#         density = blue_density[i*width+j]
#         r, g, b = rgb_img.getpixel((j, i))
#         r = 255
#         g = 255
#         b = 255 - density
#         rgb_img.putpixel((j, i), (int(r), int(g), int(b)))

# rgb_img.save("./test_img/density_rgb.jpg")


# 画像の各ピクセルについて、グラデーションを適用する
for y in range(height):
    for x in range(width):
        r, g, b = rgb_img.getpixel((x, y))
        density = blue_density[y*width+x]
        h, l, s = colorsys.rgb_to_hls(r/255.0, g/255.0, b/255.0)
        # h = 240.0 / 360.0 # hは青色に固定す
        h = 1.0 * (1.0 - density) / 360.0
        # s = density # sは密集度に比例する
        r, g, b = colorsys.hls_to_rgb(h, l, s) #(h, l, s)
        rgb_img.putpixel((x, y), (int(r*255), int(g*255), int(b*255)))

# 変換後の画像を保存する
rgb_img.save("./test_img/density.jpg")
