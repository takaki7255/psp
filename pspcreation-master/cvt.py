import sys
import subprocess
import re
import os

# メイン関数
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
        tiffile = sys.argv[1] + '/'+file
        print(tiffile)
        cvt_args = ['convert', tiffile, '-depth', '16', cvtfolder+file]
        res = subprocess.run(cvt_args) #16ビットに変換

if __name__ == '__main__':
    main()