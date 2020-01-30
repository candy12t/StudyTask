import os
import sys
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from video2img import Video
from audio import Audio


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

    def load_wave(self):
        fTyp = [('', '*.wav')]
        iDir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        filepath = filedialog.askopenfilename(filetypes = fTyp, initialdir = iDir)
        self.file.set(filepath)

    def load_folder(self):
        iDir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        dirc = filedialog.askdirectory(initialdir = iDir)
        self.file.set(dirc)


class Subframe:
    def __init__(self, frame):
        self.frame = frame

    def create_subfame(self):
        self.subFrame = ttk.Frame(self.frame, padding=10)
        self.subFrame.grid(row=5, column=1)

    def create_start_button(self, run_cmd):
        start_button = ttk.Button(self.subFrame, text='Run', command=run_cmd)
        start_button.pack(side=LEFT)

    def create_exit_button(self):
        exit_button = ttk.Button(self.subFrame, text='Cancel', command=quit)
        exit_button.pack(side=LEFT)


def run_video():
    video = Video(file0.get(), file1.get(), file2.get(), file3.get(), file4.get())
    video.read_video()
    video.write()
    video.open_dir()
    exit()


def run_audio():
    audio = Audio(file0.get(), file2.get())
    audio.read()
    audio.write(int(file1.get()))
    audio.open_dir()
    exit()


def create(frame, text, num, flag):
    app = Application(frame, text, num)
    if flag:
        cmd = app.load_folder
    else:
        cmd = app.load_video
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

    text0 = '処理する音声ファイル'
    num0 = 0
    app0 = Application(frame, text0, num0)
    cmd0 = app0.load_wave
    app0.label()
    app0.textbox()
    app0.btn(cmd0)
    file0 = app0.file

    text1 = '切り出すフレーム数'
    num1 = 1
    app1 = Application(frame, text1, num1)
    # cmd1 = app1.load_folder
    app1.label()
    app1.textbox()
    # app1.btn(cmd1)
    file1 = app1.file

    text2 = '出力先フォルダ'
    num2 = 2
    app2 = Application(frame, text2, num2)
    cmd2 = app2.load_folder
    app2.label()
    app2.textbox()
    app2.btn(cmd2)
    file2 = app2.file
    
    # flag0 = False
    # text0 = '処理する動画ファイル'
    # num0 = 0
    # file0 = create(frame, text0, num0, flag0)

    # flag1 = True
    # text1 = 'RGBカラー画像の出力先フォルダ'
    # num1 = 1
    # file1 = create(frame, text1, num1, flag1)

    # text2 = 'R成分画像の出力先フォルダ'
    # num2 = 2
    # file2 = create(frame, text2, num2, flag1)

    # text3 = 'G成分画像の出力先フォルダ'
    # num3 = 3
    # file3 = create(frame, text3, num3, flag1)

    # text4 = 'B成分画像の出力先フォルダ'
    # num4 = 4
    # file4 = create(frame, text4, num4, flag1)


    run_cmd = run_audio
    sub_frame = Subframe(frame)
    sub_frame.create_subfame()
    sub_frame.create_start_button(run_cmd)
    sub_frame.create_exit_button()


    root.mainloop()