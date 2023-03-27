from PIL import Image
import os
import sys
import numpy as np
import subprocess

def main():
    avg_arr = None
    all_filenames = os.listdir(sys.argv[1])
    #print(type(all_filenames))
    #print(all_filenames)
    # tifのみ抽出
    filenames = [filenames for filenames in all_filenames if filenames.endswith('.tif')]
    filenames.sort()
    #print(filenames)

    for file in filenames:
        input_file = sys.argv[1] + '/'+file
        print(input_file)
        img = Image.open(input_file)
        if type(avg_arr) == type(None):
            avg_arr = np.asarray(img) / len(filenames)
        else:
            avg_arr += np.asarray(img) / len(filenames)
    avg_img = Image.fromarray(np.uint16(avg_arr))
    avg_folder = sys.argv[1] + '/avg/'
    print('mkdir ' + avg_folder)
    args = ['mkdir', avg_folder]
    res = subprocess.run(args) #フォルダ作成
    avg_img_file = avg_folder + 'avg.tiff'
    avg_img.save(avg_img_file)
    
if __name__ == '__main__':
    main()