# GUI表示

import os

from tkinter import StringVar, LEFT, filedialog, ttk


class Application:
    def __init__(self, frame, text, num):
        self.frame = frame
        self.text = text
        self.num = num
        self.file = StringVar()

    # ラベルの作成
    def label(self):
        label = ttk.Label(self.frame, text=self.text)
        label.grid(row=self.num, column=0)

    # テキストボックスの作成
    def textbox(self):
        textbox = ttk.Entry(self.frame, textvariable=self.file, width=50)
        textbox.grid(row=self.num, column=1)

    # ボタンの作成
    def btn(self, cmd):
        # cmdが指定されているときボタンを作成する
        if cmd is not None:
            button = ttk.Button(self.frame, text='参照', command=cmd)
            button.grid(row=self.num, column=2)

    # mp4ファイルの読み込み
    def load_video(self):
        fTyp = [('', '*.mp4')] # mp4ファイルのみの読み込み
        iDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 初期パスの設定
        filepath = filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir) # ファイルダイアログの表示
        self.file.set(filepath) # テキストボックスにパスをセット

    # wavファイルの読み込み
    def load_wave(self):
        fTyp = [('', '*.wav')] # wavファイルのみ読み込み
        iDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 初期パスの設定
        filepath = filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir) # ファイルダイアログの表示
        self.file.set(filepath) # テキストボックスにパスをセット

    # ディレクトリの読み込み
    def load_folder(self):
        iDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 初期パスをの設定
        dirc = filedialog.askdirectory(initialdir=iDir) # ファイルダイアログの表示
        self.file.set(dirc) # テキストボックスにパスをセット


class Subframe:
    def __init__(self, frame):
        self.frame = frame

    # フレームの作成
    def create_subfame(self):
        self.subFrame = ttk.Frame(self.frame, padding=10)
        self.subFrame.grid(row=5, column=1)

    # 実行ボタンの作成
    def create_start_button(self, run_cmd):
        start_button = ttk.Button(self.subFrame, text='Run', command=run_cmd)
        start_button.pack(side=LEFT)

    # キャンセルボタンの作成
    def create_exit_button(self):
        exit_button = ttk.Button(self.subFrame, text='Cancel', command=quit)
        exit_button.pack(side=LEFT)

# GUI表示部分の作成
def create_gui(frame, text, num, cmd=None):
    app = Application(frame, text, num)
    # ボタンのcmdの指定
    if cmd == 'f':
        cmd = app.load_folder
    elif cmd == 'v':
        cmd = app.load_video
    elif cmd == 'a':
        cmd = app.load_wave
    else:
        cmd = None
    app.label()
    app.textbox()
    app.btn(cmd)
    file = app.file
    return file
