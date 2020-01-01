import speech_recognition as sr

r = sr.Recognizer()

audio = '8pple/8P-5.flac'

with sr.AudioFile(audio) as source:
	audio = r.record(source)
	print('Processing')

try:
	value = r.recognize_google(audio)
	file = open("8P-5.txt", "a")
	file.write(value)
	print('Finished Processing')
	print(value)

except Exception as e:
	print(e)
