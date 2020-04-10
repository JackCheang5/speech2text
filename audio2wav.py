import os
from pydub import AudioSegment

def audio2wav():
  AudioSegment.converter = "./ffmpeg/bin/ffmpeg.exe"
  path = "./input/"
  for audio in os.listdir(path):
    file_name, file_extension = os.path.splitext(audio)
    file_extension_fin = file_extension.replace('.', '')
    audio_path = path + audio
    wav_path = path + audio.replace(file_extension_fin, 'wav')
    try:
      audio = AudioSegment.from_file(audio_path, file_extension_fin)
      file_handle = audio.export(wav_path, format='wav')
    except:
      print("Error occurred")

audio2wav()