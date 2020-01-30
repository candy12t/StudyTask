import os
import sys
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from task1 import process


class Application:
  def __init__(self, frame, text, num):
    self.frame = frame
    self.text = text
    self.num = num

  def label(self):
    self.string = StringVar()
    self.string.set(self.text)
    self.label = ttk.Label(self.frame, textvariable=self.string)
    self.label.grid(row=self.num, column=0)

  def textbox(self):
    self.file = StringVar()
    self.textbox = ttk.Entry(self.frame, textvariable=self.file, width=50)
    self.textbox.grid(row=self.num, column=1)

  def btn(self, cmd):
    self.cmd = cmd
    self.button = ttk.Button(self.frame, text='参照', command=self.cmd)
    self.button.grid(row=self.num, column=2)

  def load_video(self):
    self.fTyp = [('', '*.mp4')]
    self.iDir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    self.filepath = filedialog.askopenfilename(filetypes = self.fTyp, initialdir = self.iDir)
    self.file.set(self.filepath)

  def load_folder(self):
    self.iDir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    self.dirc = filedialog.askdirectory(initialdir = self.iDir)
    self.file.set(self.dirc)


def run():
  process(app1.file.get(), app2.file.get(), app3.file.get(), app4.file.get(), app5.file.get())
  exit()


def create(app, cmd):
  app.label()
  app.textbox()
  app.btn(cmd)


if __name__ == '__main__':
  root = Tk()
  root.title('課題1')

  frame = ttk.Frame(root, padding=10)
  frame.grid()

  text1 = '処理する動画ファイル'
  num1 = 0
  app1 = Application(frame, text1, num1)
  cmd1 = app1.load_video
  create(app1, cmd1)

  text2 = 'RGBカラー画像の出力先フォルダ'
  num2 = 1
  app2 = Application(frame, text2, num2)
  cmd2 = app2.load_folder
  create(app2, cmd2)

  text3 = 'R成分画像の出力先フォルダ'
  num3 = 2
  app3 = Application(frame, text3, num3)
  cmd3 = app3.load_folder
  create(app3, cmd3)

  text4 = 'G成分画像の出力先フォルダ'
  num4 = 3
  app4 = Application(frame, text4, num4)
  cmd4 = app4.load_folder
  create(app4, cmd4)

  text5 = 'B成分画像の出力先フォルダ'
  num5 = 4
  app5 = Application(frame, text5, num5)
  cmd5 = app5.load_folder
  create(app5, cmd5)


  frame2 = ttk.Frame(root, padding=10)
  frame2.grid()

  start_button = ttk.Button(frame2, text='Run', command=run)
  start_button.pack(side=LEFT)

  exit_button = ttk.Button(frame2, text='Cancel', command=quit)
  exit_button.pack(side=LEFT)

  root.mainloop()