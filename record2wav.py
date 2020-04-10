import os
import wave
import pyaudio

def check(s, array):
  for string in array:
    if (s == string):
      return True
  return False

def name(path):
  counter = 0
  basic_name = "record"
  exist_names = os.listdir(path)
  while(True):
    if (counter == 0):
      name = basic_name + ".wav"
      if (check(name, exist_names)):
        counter += 1
      else:
        return name
    else:
      name = basic_name + str(counter) + ".wav"
      if (check(name, exist_names)):
        counter += 1
      else:
        return name

def record(seconds):
  seconds += 1
  fs = 16000
  chunk = 1024
  channels = 1
  path = "./input/"
  sample_format = pyaudio.paInt16
  p = pyaudio.PyAudio()
  stream = p.open(format=sample_format,
                  channels=channels,
                  rate=fs,
                  frames_per_buffer=chunk,
                  input=True)
  frames = []
  for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)
  stream.stop_stream()
  stream.close()
  p.terminate()
  wf = wave.open(path + name(path), 'wb')
  wf.setnchannels(channels)
  wf.setsampwidth(p.get_sample_size(sample_format))
  wf.setframerate(fs)
  wf.writeframes(b''.join(frames))
  wf.close()

record(5)