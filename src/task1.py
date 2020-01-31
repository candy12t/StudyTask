from tk import Application, Subframe, create_gui
from tkinter import *
from video2img import Video


def run_video():
    video = Video(file0.get(), file1.get(), file2.get(), file3.get(), file4.get())
    video.read_video()
    video.write()
    video.open_dir()
    exit()


root = Tk()
root.title('課題1')

frame = ttk.Frame(root, padding=10)
frame.grid()

load_v = 'v'
text0 = '処理する動画ファイル'
num0 = 0
file0 = create_gui(frame, text0, num0, load_v)

load_f = 'f'
text1 = 'RGBカラー画像の出力先フォルダ'
num1 = 1
file1 = create_gui(frame, text1, num1, load_f)

text2 = 'R成分画像の出力先フォルダ'
num2 = 2
file2 = create_gui(frame, text2, num2, load_f)

text3 = 'G成分画像の出力先フォルダ'
num3 = 3
file3 = create_gui(frame, text3, num3, load_f)

text4 = 'B成分画像の出力先フォルダ'
num4 = 4
file4 = create_gui(frame, text4, num4, load_f)


run_cmd = run_video
sub_frame = Subframe(frame)
sub_frame.create_subfame()
sub_frame.create_start_button(run_cmd)
sub_frame.create_exit_button()


root.mainloop()