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
    file1 = app1.file

    text2 = 'RGBカラー画像の出力先フォルダ'
    num2 = 1
    app2 = Application(frame, text2, num2)
    cmd2 = app2.load_folder
    create(app2, cmd2)
    file2 = app2.file

    text3 = 'R成分画像の出力先フォルダ'
    num3 = 2
    app3 = Application(frame, text3, num3)
    cmd3 = app3.load_folder
    create(app3, cmd3)
    file3 = app3.file

    text4 = 'G成分画像の出力先フォルダ'
    num4 = 3
    app4 = Application(frame, text4, num4)
    cmd4 = app4.load_folder
    create(app4, cmd4)
    file4 = app4.file

    text5 = 'B成分画像の出力先フォルダ'
    num5 = 4
    app5 = Application(frame, text5, num5)
    cmd5 = app5.load_folder
    create(app5, cmd5)
    file5 = app5.file


    frame2 = ttk.Frame(root, padding=10)
    frame2.grid()

    start_button = ttk.Button(frame2, text='Run', command=run)
    start_button.pack(side=LEFT)

    exit_button = ttk.Button(frame2, text='Cancel', command=quit)
    exit_button.pack(side=LEFT)

    root.mainloop()