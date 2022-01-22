# Aida

import speech_recognition as sr
import webbrowser as wb
import sys
import pyttsx3
from colorama import Fore

def talk(text):
	print( text )
	engine = pyttsx3.init()
	engine.say(text)
	engine.runAndWait()

def cmd():
	r = sr.Recognizer()

	with sr.Microphone(device_index = 1) as source:
		audio = r.listen(source)

	try:
		task = r.recognize_google(audio, language = 'ru-RU').lower()
		print(f"[log] Распознано --> {task}")

	except:
		pass
		task = command()

	return task

def work(task):
	if 'привет' in task:
		talk("Hello World!")

	elif 'открой youtube' in task:
		wb.open("www.youtube.com")

	elif 'я дома' and 'я вернулся' in task:
		talk("Приветствую")

while True:
	work(cmd())