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
        self.file = StringVar()

    def label(self):
        self.string = StringVar()
        self.string.set(self.text)
        label = ttk.Label(self.frame, textvariable=self.string)
        label.grid(row=self.num, column=0)

    def textbox(self):
        textbox = ttk.Entry(self.frame, textvariable=self.file, width=50)
        textbox.grid(row=self.num, column=1)

    def btn(self, cmd):
        button = ttk.Button(self.frame, text='参照', command=cmd)
        button.grid(row=self.num, column=2)

    def load_video(self):
        fTyp = [('', '*.mp4')]
        iDir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        filepath = filedialog.askopenfilename(filetypes = fTyp, initialdir = iDir)
        self.file.set(filepath)

    def load_folder(self):
        iDir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        dirc = filedialog.askdirectory(initialdir = iDir)
        self.file.set(dirc)


def run():
    process(file1.get(), file2.get(), file3.get(), file4.get(), file5.get())
    exit()


def create(frame, text, num, flag):
    app = Application(frame, text, num)
    if flag:
        cmd = app.load_video
    else:
        cmd = app.load_folder
    app.label()
    app.textbox()
    app.btn(cmd)
    file = app.file
    return file


if __name__ == '__main__':
    root = Tk()
    root.title('課題1')

    frame = ttk.Frame(root, padding=10)
    frame.grid()

    flag1 = True
    text1 = '処理する動画ファイル'
    num1 = 0
    file1 = create(frame, text1, num1, flag1)

    flag2 = False
    text2 = 'RGBカラー画像の出力先フォルダ'
    num2 = 1
    file2 = create(frame, text2, num2, flag2)

    text3 = 'R成分画像の出力先フォルダ'
    num3 = 2
    file3 = create(frame, text3, num3, flag2)

    text4 = 'G成分画像の出力先フォルダ'
    num4 = 3
    file4 = create(frame, text4, num4, flag2)

    text5 = 'B成分画像の出力先フォルダ'
    num5 = 4
    file5 = create(frame, text5, num5, flag2)


    subFrame = ttk.Frame(frame, padding=10)
    subFrame.grid(row=5, column=1)

    start_button = ttk.Button(subFrame, text='Run', command=run)
    start_button.pack(side=LEFT)

    exit_button = ttk.Button(subFrame, text='Cancel', command=quit)
    exit_button.pack(side=LEFT)

    root.mainloop()