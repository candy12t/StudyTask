from tk import Application, Subframe, create_gui
from tkinter import *
from audio import Audio


def run_audio():
    audio = Audio(file0.get(), file2.get())
    audio.read()
    audio.write(int(file1.get()))
    audio.open_dir()
    exit()


root = Tk()
root.title('課題2')

frame = ttk.Frame(root, padding=10)
frame.grid()

load_a = 'a'
text0 = '処理する音声ファイル'
num0 = 0
file0 = create_gui(frame, text0, num0, load_a)

text1 = '切り出すフレーム数'
num1 = 1
app1 = Application(frame, text1, num1)
app1.label()
app1.textbox()
file1 = app1.file

load_f = 'f'
text2 = '出力先フォルダ'
num2 = 2
file2 = create_gui(frame, text2, num2, load_f)

run_cmd = run_audio
sub_frame = Subframe(frame)
sub_frame.create_subfame()
sub_frame.create_start_button(run_cmd)
sub_frame.create_exit_button()

root.mainloop()