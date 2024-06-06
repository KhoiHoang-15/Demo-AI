import speech_recognition

robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
	print("Robot: I am Listening")
	audio = robot_ear.listen(mic)

print("Robot: ...")

try:
	you = robot_ear.recognize_google(audio)
except:
	you =""

print("You: " + you)


you = "hello"

if you == "":
	robot_brain ="I can not hear you, please try again"
elif you == "hello":
	 robot_brain = "Hello Ms.Hanh"
elif you == "Today":
	robot_brain = "Monday"
else:
	robot_brain = "I am fine thank you, what about you"

print(robot_brain)

import pyttsx3
robot_brain= "I can not hear you, please try again"

engine = pyttsx3.init()
engine.say("robot_brain")
engine.runAndWait()

