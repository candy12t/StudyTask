from tk import Subframe, create_gui
from tkinter import Tk, ttk
from video2img import Video


# 動画処理
def run_video():
    video = Video(files[0].get(), files[1].get(), files[2].get(), files[3].get(), files[4].get())
    video.read_video()
    video.process()
    video.open_dir()
    exit()


# rootの作成
root = Tk()
root.title('課題1')

# frameの作成
frame = ttk.Frame(root, padding=10)
frame.grid()

texts = [
    '処理する動画ファイル',
    'RGBカラー画像の出力先フォルダ',
    'R成分画像の出力先フォルダ',
    'G成分画像の出力先フォルダ',
    'B成分画像の出力先フォルダ'
    ]

# GUI表示部分の作成
files = []
for i in range(len(texts)):
    if i == 0:
        cmd = 'v'
    else:
        cmd = 'f'
    # ファイルパスを取得し、リストに追加
    file = create_gui(frame, texts[i], i, cmd)
    files.append(file)

# 実行、キャンセルボタン部分のフレーム作成
run_cmd = run_video
sub_frame = Subframe(frame)
sub_frame.create_subfame()
sub_frame.create_start_button(run_cmd)
sub_frame.create_exit_button()

root.mainloop()
