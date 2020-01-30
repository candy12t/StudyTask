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

    def read_video(self):
        self.video = cv2.VideoCapture(self.mp4)
        if not self.video.isOpened():
            return

    # def save_img(self, img, dirc):
    #     img = Image.fromarray(img)
    #     img.save('{}/{}.{}'.format(dirc, n, 'png'))

    def write(self):
        n = 0
        for i in range(1):
            ret, frame = self.video.read()
            if ret:
                self.rgb_img = np.array(frame)
                r_img = self.rgb_img.copy()
                r_img[:, :, (1, 2)] = 0
                r_img = Image.fromarray(r_img)
                r_img.save('{}/{}.{}'.format(self.r, n, 'png'))

                g_img = self.rgb_img.copy()
                g_img[:, :, (0, 2)] = 0
                g_img = Image.fromarray(g_img)
                g_img.save('{}/{}.{}'.format(self.g, n, 'png'))

                b_img = self.rgb_img.copy()
                b_img[:, :, (0, 1)] = 0
                b_img = Image.fromarray(b_img)
                b_img.save('{}/{}.{}'.format(self.b, n, 'png'))


                # save_img(r_img, self.r)
                # save_img(g_img, self.g)
                # save_img(b_img, self.b)
                self.rgb_img = cv2.cvtColor(self.rgb_img, cv2.COLOR_BGR2RGB)
                self.rgb_img = Image.fromarray(self.rgb_img)
                self.rgb_img.save('{}/{}.{}'.format(self.rgb, n, 'png'))

                # save_img(self.rgb_img, self.rgb)

                n += 1
            else:
                return

    def open_dir(self):
        input_dir = os.path.dirname(os.path.abspath(self.mp4))
        cmd = 'open {} {} {} {} {}'.format(input_dir, self.rgb, self.r, self.g, self.b)
        subprocess.call(cmd.split())


if __name__ == '__main__':
    mp4 = input()
    rgb = input()
    r = input()
    g = input()
    b = input()

    video = Video(mp4, rgb, r, g, b)
    video.read_video()
    video.write()
    video.open_dir()