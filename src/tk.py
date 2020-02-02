import os
from tkinter import StringVar, LEFT, filedialog, ttk


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
        filepath = filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)
        self.file.set(filepath)

    def load_wave(self):
        fTyp = [('', '*.wav')]
        iDir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        filepath = filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)
        self.file.set(filepath)

    def load_folder(self):
        iDir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        dirc = filedialog.askdirectory(initialdir=iDir)
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


def create_gui(frame, text, num, load):
    app = Application(frame, text, num)
    if load == 'f':
        cmd = app.load_folder
    elif load == 'v':
        cmd = app.load_video
    elif load == 'a':
        cmd = app.load_wave
    app.label()
    app.textbox()
    app.btn(cmd)
    file = app.file
    return file
