import numpy as np
from PIL import Image
import subprocess
import cv2
import os


class Video:
    def __init__(self, mp4, rgb, r, g, b):
        self.mp4 = mp4
        self.rgb = rgb
        self.r = r
        self.g = g
        self.b = b
        self.n = 0

    # 動画の読み込み
    def read_video(self):
        self.video = cv2.VideoCapture(self.mp4) # 動画の読み込み
        if not self.video.isOpened(): # 動画ファイルとして開けるか
            return

    # 画像の保存
    def save_img(self, dirc, x=None, y=None):
        img = self.img.copy()
        # x, yで指定した成分の値を0に
        if (x is None) and (y is None):
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        else:
            img[:, :, (x, y)] = 0
        img = Image.fromarray(img) # nadarray型からImage型に変換
        img.save('{}/{}.{}'.format(dirc, self.n, 'png')) #  指定したディレクトリに保存

    # 動画をフレームごとに切り出して処理
    def write(self):
        while True:
            ret, frame = self.video.read() # (ret, frame) = (boolean型、ndarray型)
            if ret:
                self.img = np.array(frame)

                self.save_img(self.rgb)
                self.save_img(self.r, 1, 2)
                self.save_img(self.g, 0, 2)
                self.save_img(self.b, 0, 1)

                self.n += 1
            else:
                return

    # 指定したディレクトリを開く
    def open_dir(self):
        input_dir = os.path.dirname(os.path.abspath(self.mp4)) # 動画ファイルのカレントディレクトリの取得
        # openコマンドの実行
        cmd = 'open {} {} {} {} {}'.format(input_dir, self.rgb, self.r, self.g, self.b)
        subprocess.call(cmd.split())
