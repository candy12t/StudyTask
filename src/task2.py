from tk import Application, Subframe, create_gui
from tkinter import Tk, ttk
from audio import Audio


def run_audio():
    audio = Audio(files[0].get(), files[2].get())
    audio.read()
    audio.write(int(files[1].get()))
    audio.open_dir()
    exit()


root = Tk()
root.title('課題2')

frame = ttk.Frame(root, padding=10)
frame.grid()

texts = ['処理する音声ファイル', '切り出すフレーム数', '出力先フォルダ']
files = []
for i in range(len(texts)):
    if i == 0:
        cmd = 'a'
    elif i == 2:
        cmd = 'f'
    else:
        cmd = None
    file = create_gui(frame, texts[i], i, cmd)
    files.append(file)

run_cmd = run_audio
sub_frame = Subframe(frame)
sub_frame.create_subfame()
sub_frame.create_start_button(run_cmd)
sub_frame.create_exit_button()

root.mainloop()
