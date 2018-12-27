# encoding: utf8
from __future__ import unicode_literals
from pylab import *
from cv2 import imread
import cv2

# 画像を読み込み
gazo = imread( "kadai4.bmp", 0 )

# 画像を表示
imshow(gazo, cmap="gray", vmin=0, vmax=255, interpolation="None")

# 画像を変換
gazo_idou = zeros((12,12))
for x in range(1,11):
    for y in range(1,11):
        # 課題：filterの値を変えて様々なフィルタを作成し，画素値と画像の変化を確認しなさい．
        #      レポートでは原理（数式）と実行結果を照らし合わせて，それらフィルタの処理を分かりやすく説明しなさい．
        filter = [
            [0.5, 0.5, 0.5],
            [0.5, 0.5, 0.5],
            [0.5, 0.5, 0.5]
            ]

        gasochi = 0
        for xx in range(3):
            for yy in range(3):
                # ここでfilterの値をgazoに掛ける
                gasochi += gazo[y+yy-1][x+xx-1] * filter[yy][xx]

        # 0〜255の範囲内に収める
        gasochi = int(gasochi)
        if gasochi<0:
            gasochi = 0
        elif gasochi>255:
            gasochi = 255
        gazo_idou[y][x] = gasochi

gazo_lap = zeros((12,12))
for x in range(1,11):
    for y in range(1,11):
        # 課題：filterの値を変えて様々なフィルタを作成し，画素値と画像の変化を確認しなさい．
        #      レポートでは原理（数式）と実行結果を照らし合わせて，それらフィルタの処理を分かりやすく説明しなさい．
        filter = [
            [0.0, 0.5, 0.0],
            [0.5, -2.0, 0.5],
            [0.0, 0.5, 0.0]
            ]

        gasochi = 0
        for xx in range(3):
            for yy in range(3):
                # ここでfilterの値をgazoに掛ける
                gasochi += gazo[y+yy-1][x+xx-1] * filter[yy][xx]

        # 0〜255の範囲内に収める
        gasochi = int(gasochi)
        if gasochi<0:
            gasochi = 0
        elif gasochi>255:
            gasochi = 255
        gazo_lap[y][x] = gasochi

gazo2 = cv2.hconcat([gazo_idou, gazo_lap])
# 画像を表示
figure()
imshow(gazo2, cmap="gray", vmin=0, vmax=255, interpolation="None")
show()
