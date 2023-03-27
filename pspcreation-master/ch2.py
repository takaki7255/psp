# chatGPT によるPSP画像作成プログラムの出力
from cProfile import run
from PIL import Image
import os
import sys
import numpy as np
import subprocess
import cv2
import re
import multiprocessing

# psp画像の生成
def calc_psp_img(run_img, ref_avg_img, dark_avg_img):
    A = 0.3389
    B = 0.661
    Pref = 100.0
    pmin = 97
    pmax = 102
    # 発光強度画像
    Iref_per_I_arr = (np.asarray(ref_avg_img) - np.asarray(dark_avg_img)) / (np.asarray(run_img) - np.asarray(dark_avg_img))
    psp_array = (Iref_per_I_arr - A) * Pref / B
    print("PSP計測画像")
    # print(psp_array)
    # 92-102 kPaの範囲に収める
    psp_array = np.where(psp_array < pmin, pmin, psp_array)
    psp_array = np.where(psp_array > pmax, pmax, psp_array)
    # print("---")
    print("97:127に正規化")
    # print(psp_array)
    # 0-255に正規化
    psp_array = (psp_array - psp_array.min()) / (psp_array.max() - psp_array.min()) * 255
    # print("---")
    print("0-255の8bitに正規化")
    # print(psp_array)
    # print("---")

    # 8ビット画像に出力
    psp_img = Image.fromarray(np.uint8(psp_array))
    return psp_img


def process_image(run_filename, ref_avg_img, dark_avg_img, psp_dir):
    print(run_filename)
    run_img = Image.open(run_filename)
    psp_np_img = calc_psp_img(run_img, ref_avg_img, dark_avg_img)
    # PILからopenCVに変換
    psp_cv_img = np.array(psp_np_img, dtype=np.uint8)
    # JET画像の生成
    psp_jet_img = cv2.applyColorMap(psp_cv_img, cv2.COLORMAP_JET)
    psp_jet_filename = psp_dir + '/' + os.path.basename(os.path.dirname(run_filename)) + '_' + os.path.splitext(os.path.basename(run_filename))[0] + '_psp.tif'
    cv2.imwrite(psp_jet_filename, psp_jet_img)


def main():
    # 通風時画像が格納されるフォルダの読み込み
    run_dir_filenames = os.listdir(sys.argv[1])
    # 出力先のフォルダ作成
    psp_dir = os.path.join(sys.argv[1], 'psp')
    print('mkdir ' + psp_dir)
    try:
        os.makedirs(psp_dir)
    except FileExistsError:
        pass
    # print(run_dir_filenames)
    run_filenames = [filenames for filenames in run_dir_filenames if filenames.endswith('.tif')]
    run_filenames.sort()  # 並び替え
    # print(run_filenames)
    # 無風時画像 (平均) の読み込み
    ref_avg_img = Image.open(sys.argv[2])
    # print(ref_avg_img.format, ref_avg_img.size, ref_avg_img.mode)
    # 黒画像 (平均) の読み込み
    dark_avg_img = Image.open(sys.argv[3])
    # print(dark_avg_img.format, dark_avg_img.size, dark_avg_img.mode)
    # 通風時画像の処理
    for run_filename in run_filenames:
        process_image(os.path.join(sys.argv[1], run_filename), ref_avg_img, dark_avg_img, psp_dir)

    if __name__ == 'main':
        main()
