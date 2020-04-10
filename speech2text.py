import os
import speech_recognition

def audio2text(audio): 
  recognizer = speech_recognition.Recognizer()
  with speech_recognition.AudioFile(audio) as source:
    recognizer.adjust_for_ambient_noise(source, duration=0)
    audio = recognizer.record(source)
  try:
    text = recognizer.recognize_google(audio, language="zh-TW")
  except recognizer.UnknowValueError:
    text = "Unable to translate: Unknown Value."
  except recognizer.RequestError as error:
    text = "Unable to translate: Error = {}".format(error)
  return text

def multi_files_converting():
  input_path = "./input/"
  output_path = "./output/"
  for audio in os.listdir(input_path):
    file_name, file_extension = os.path.splitext(audio)
    file_extension_fin = file_extension.replace('.', '')
    audio_path = input_path + audio
    text_path = output_path + file_name + ".txt"
    fw = open(text_path, 'w', encoding="CP950")
    text = audio2text(audio_path)
    fw.write(text)
    fw.close()
    