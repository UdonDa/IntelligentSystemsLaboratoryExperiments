# encoding: utf8
from __future__ import unicode_literals
from pylab import *
from cv2 import imread, hconcat

# 画像を読み込み
gazo = imread( "kadai5.bmp", 0 )

# 画像を表示
imshow(gazo, cmap="gray", vmin=0, vmax=255, interpolation="None")
print(gazo)

# ヒストグラムを表示
figure()
hist( gazo.flatten(), 256, (0,255) )

# 画像を変換
print("gazo.shape ({},{})".format(gazo.shape[0], gazo.shape[1])) # -> [396, 455]

def shori(gazo, gazo2, SIKII):
    for x in range(gazo.shape[1]):
        for y in range(gazo.shape[0]):
            # 課題：濃度ヒストグラムを参照して，画像の特徴を表わす二値画像を生成しなさい．
            #      レポートでは，作成したプログラムによってどのような処理が行われているのかを
            #      ヒストグラムを使って分かりやすく説明しなさい．
            value = gazo[y][x]
            if value < SIKII:
                gazo2[y][x] = 0
            else:
                gazo2[y][x] = 255
    return gazo2

gazoa = shori(gazo, zeros((gazo.shape[0],gazo.shape[1])), 220)
gazob= shori(gazo, zeros((gazo.shape[0],gazo.shape[1])), 225)
gazo2 = shori(gazo, zeros((gazo.shape[0],gazo.shape[1])), 230)
gazo3 = shori(gazo, zeros((gazo.shape[0],gazo.shape[1])), 235)
#gazo5 = shori(gazo, zeros((gazo.shape[0],gazo.shape[1])), 245)
#gazo6 = shori(gazo, zeros((gazo.shape[0],gazo.shape[1])), 250)


#gazo7 = shori(gazo, zeros((gazo.shape[0],gazo.shape[1]))





# 画像を表示
gazo2 = hconcat([gazoa, gazob, gazo2, gazo3])
figure()
imshow(gazo2, cmap="gray", vmin=0, vmax=255, interpolation="None")
show()
