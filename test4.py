from PIL import Image
import colorsys

# 画像を読み込み、RGB値に分解する
img = Image.open("./masked_img.jpg")
rgb_img = img.convert('RGB')
width, height = img.size

# 周辺の青色画素の割合を計算し、青色の密集度を求める
blue_density = []
for y in range(height):
    row = []
    for x in range(width):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx = x + dx
                ny = y + dy
                if nx < 0 or ny < 0 or nx >= width or ny >= height:
                    continue
                r, g, b = rgb_img.getpixel((nx, ny))
                if b > r and b > g:
                    count += 1
        density = count / 8.0  # 8は周辺8ピクセルの数
        row.append(density)
    blue_density.append(row)

# 青色の密集度に応じて、グラデーションを適用する
for y in range(height):
    for x in range(width):
        density = blue_density[y][x]
        # 色相を変更することで、連続的なグラデーションを適用する
        hue = density * 240.0 
        r, g, b = rgb_img.getpixel((x, y))
        h, l, s = colorsys.rgb_to_hls(r/255.0, g/255.0, b/255.0)
        h = hue / 360.0
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        rgb_img.putpixel((x, y), (int(r*255), int(g*255), int(b*255)))

# 画像を保存する
rgb_img.save('./test_img/density.jpg')
