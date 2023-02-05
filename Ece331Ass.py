import speech_recognition as sr

r = sr.Recognizer()



h = sr.AudioFile('audio.wav')
with h as source:
    audio = r.record(source)
    
r.recognize_google(audio)