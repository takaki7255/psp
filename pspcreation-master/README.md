# PSP生成
PSP画像を生成するプログラム

# How to Use (使い方)
## 方法
1. avgimg_creation.py (16ビット画像の平均画像の生成)
	- refとdarkで生成する
2. pimg_creation.py (psp画像の生成)


## 画像群から平均画像 (16ビット) の生成

```
python3 avgimg_cration.py フォルダ名 (16bit変換済み)
```
ref画像とdark画像それぞれで実施する。このときavgフォルダが生成される

## P画像の生成
run画像，refとdarkの平均画像を使用してP画像を出力する。
```
python3 pimg_creation.py run画像のフォルダ refの平均画像 darkの平均画像
```

## 以下，ボツプログラム
### cvt.py
12ビット画像を16ビットに変換 (正規化あり)

```
python3 cvt.py フォルダ名
```

例
```
python3 cvt.py /Users/x19000xx/Downloads/psp/Run6/dark
```

出力結果
該当のフォルダにcvtフォルダが追加されて，
そこに16ビット変換された画像が格納されます．
ただし，正規化されます．



### imgbit_convert.py
12ビット画像を16ビットに変換 (正規化なし)

```
python3 imgbit_convert.py フォルダ名
```

例
```
python3 cvt.py /Users/x19000xx/Downloads/psp/Run6/dark
```

出力結果
該当のフォルダにcvtフォルダが追加されて，
そこに16ビット変換された画像が格納されます．
正規化はされません．

確かめ方 (ImageMagick)
```
identify -verbose 画像ファイル名
```
