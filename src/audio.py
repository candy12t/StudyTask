from scipy import int16, int32
import wave
import math
import numpy as np
import subprocess
import os


class Audio:
    def __init__(self, wavfile, output_dir):
        self.wavfile = wavfile
        self.output_dir = output_dir
        self.nchannels = 0
        self.sampwidth = 0
        self.framerate = 0
        self.nframes = 0
        self.audio_data = ''

    # 音声ファイルの読み込み
    def read(self):
        wavRead = wave.open(self.wavfile, 'rb') # 読み込みモードで開く
        wavRead.rewind() # ポインタを先頭に戻す

        self.nchannels = wavRead.getnchannels() # オーディオチャンネル数の取得(モノラル→1, ステレオ→2)
        self.sampwidth = wavRead.getsampwidth() # サンプルサイズの取得
        self.framerate = wavRead.getframerate() # サンプリングレートの取得
        self.nframes = wavRead.getnframes() # オーディオフレーム数の取得

        data = wavRead.readframes(self.nframes) # オーディオフレームをバイト列に変換
        wavRead.close()

        # バイト列をndarray型に変換
        if self.nchannels == 1:
            self.audio_data = np.frombuffer(data, dtype=int16)
        elif self.nchannels == 2:
            self.audio_data = np.frombuffer(data, dtype=int32)

    # 音声ファイルをフレーム数ごとに切り出し保存
    def write(self, frame_count):
        num = math.ceil(self.nframes/frame_count) # 切り出す回数を算出
        for i in range(num):
            output_file = '{}/{}.wav'.format(self.output_dir, i) # 指定したディレクトリに保存
            # 切り出すフレームの始点と終点の指定
            start = i * frame_count
            end = start + frame_count

            wavWrite = wave.open(output_file, 'wb') # 指定したファイルを書き込みモードで開く
            wavWrite.setnchannels(self.nchannels) # チャンネル数の設定
            wavWrite.setsampwidth(self.sampwidth) # サンプルサイズの設定
            wavWrite.setframerate(self.framerate) # サンプリングレートの設定
            wavWrite.writeframes(self.audio_data[start:end]) # フレームの書き込み
            wavWrite.close()

    # 指定したディレクトリを開く
    def open_dir(self):
        input_dir = os.path.dirname(os.path.abspath(self.wavfile)) # 入力音声ファイルのカレントディレクトリの取得
        # openコマンドの実行
        cmd = 'open {} {}'.format(input_dir, self.output_dir)
        subprocess.call(cmd.split())
