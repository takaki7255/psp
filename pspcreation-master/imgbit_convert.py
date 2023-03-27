from PIL import Image
import os
import sys
import subprocess
import re

# 12bitの画像から16bitの画像作成
def cvt_func(input_img_name, output_img_name):
    #org_img = Image.open('/Users/sawano/Downloads/psp/ref/Camera_1000001.tif')
    org_img = Image.open(input_img_name)
    # print(org_img.format, org_img.size, org_img.mode)
    # print(org_img.getextrema())
    width, height = org_img.size

    bit_converted_img = Image.new("I;16", org_img.size)
    
    for y in range(height):
        for x in range(width):
            org_val = org_img.getpixel((x, y))
            bit_converted_img.putpixel((x,y), org_val)
    bit_converted_img.save(output_img_name)

def main():
    filenames = os.listdir(sys.argv[1])
    cvtfolder = sys.argv[1] + '/cvt/'
    print('mkdir ' + cvtfolder)
    args = ['mkdir', cvtfolder]
    res = subprocess.run(args) #フォルダ作成
    for file in filenames:
        match = re.search("\.tif", file)
        if not match: #.tif以外は実施しない
            continue
        input_file = sys.argv[1] + '/'+file
        output_file = cvtfolder+file
        print(input_file, output_file)
        cvt_func(input_file, output_file)

if __name__ == '__main__':
    main()