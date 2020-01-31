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

    def read(self):
        wavRead = wave.open(self.wavfile, 'rb')
        wavRead.rewind()

        self.nchannels = wavRead.getnchannels() # 1
        self.sampwidth = wavRead.getsampwidth() # 2
        self.framerate = wavRead.getframerate() # 20000
        self.nframes = wavRead.getnframes() # 13824
        # print('nchannels:{}, sampwidth:{}, framerate:{}, nframes:{}'.format(self.nchannels, self.sampwidth, self.framerate, self.nframes))

        data = wavRead.readframes(self.nframes)
        wavRead.close()

        if self.nchannels == 1:
            self.audio_data = np.frombuffer(data, dtype=int16)
        elif self.nchannels == 2:
            self.audio_data = np.frombuffer(data, dtype=int32)

    def write(self, frame_count):
        num = math.ceil(self.nframes/frame_count)

        for i in range(num):
            output_file = '{}/{}.wav'.format(self.output_dir, i)
            start = i * frame_count
            end = start + frame_count

            wavWrite = wave.open(output_file, 'wb')
            wavWrite.setnchannels(self.nchannels)
            wavWrite.setsampwidth(self.sampwidth)
            wavWrite.setframerate(self.framerate)
            wavWrite.writeframes(self.audio_data[start:end])
            wavWrite.close()

    def open_dir(self):
        input_dir = os.path.dirname(os.path.abspath(self.wavfile))
        cmd = 'open {} {}'.format(input_dir, self.output_dir)
        subprocess.call(cmd.split())


# if __name__ == '__main__':
#     wavfile = './sound/input/A_a.wav' # input()
#     output_dir = './sound/output' # input()
#     frame_count = 2765 # int(input()) 2765 → 5分割

#     audio = Audio(wavfile, output_dir)
#     audio.read()
#     audio.write(frame_count)
#     audio.open_dir()
