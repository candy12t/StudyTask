import numpy as np
from PIL import Image
import subprocess
import cv2
import os


def process(video_path, rgb_img_path, r_img_path, g_img_path, b_img_path):
  def img_save(img, subdir):
    img = Image.fromarray(img)
    img.save('{}/{}.{}'.format(subdir, n, 'png'))

  video = cv2.VideoCapture(video_path)

  if not video.isOpened():
    return

  count = video.get(cv2.CAP_PROP_FRAME_COUNT)

  n = 0
  # while True:
  for i in range(1):
    ret, frame = video.read()
    if ret:
      RGB_img = np.array(frame)

      R_img = RGB_img.copy()
      R_img[:, :, (1, 2)] = 0
      G_img = RGB_img.copy()
      G_img[:, :, (0, 2)] = 0
      B_img = RGB_img.copy()
      B_img[:, :, (0, 1)] = 0

      img_save(R_img, r_img_path)
      img_save(G_img, g_img_path)
      img_save(B_img, b_img_path)
      RGB_img = cv2.cvtColor(RGB_img, cv2.COLOR_BGR2RGB)
      img_save(RGB_img, rgb_img_path)

      n += 1
    else:
      return

  cmd = 'open {} {} {} {}'.format(rgb_img_path, r_img_path, g_img_path, b_img_path)
  subprocess.call(cmd.split())