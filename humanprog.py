#Problem is :- "Convert the OS based program into a menu driven program using Python Code which will execute the required user query when user will give the input as a text."


import os
import pyttsx3

pyttsx3.speak("Hii and Welcome to my program")

while True:
	print("chat with me with your requirements:", end=' ')
	a = input()

	#print(a)
	#os.system(a)

	if ("hii" in a) or ("hi" in a) or ("hello" in a):
		print("Hello how can I help you")

	elif ((("run" in a) or ("launch " in a) or ("open" in a)) and ("chrome" in a)) :
		os.system("chrome")

	elif (("run" in a) or ("execute" in a) or ("open" in a) or ("launch" in a)) and (("notepad" in a) or ("editor" in a)):
		os.system("notepad")

	elif (("open" in a) or ("run" in a) or ("play" in a)) and (("player" in a) or ("media" in a)):
		os.system("wmplayer")

	elif (("open" in a) or ("run" in a) or ("launch" in a)) and ("arduino" in a):
		os.system("arduino")

	elif (("open" in a) or ("run" in a)) and ("paint" in a):
		os.system("mspaint")
	
	elif (("open" in a) or ("run" in a) or ("connect" in a) or ("launch" in a)) and ("skype" in a):
		os.system("skype")

	elif (("open" in a) or ("run" in a) or ("launch" in a)) and ("google" in a):
		os.system("chrome www.google.co.in")

	elif (("open" in a) or ("launch" in a) or ("run" in a)) and ("yahoo" in a):
		os.system("chrome yahoo.com")

	elif (("open" in a) or ("run" in a) or ("launch" in a)) and (("calculator" in a) or ("calc" in a)):
		os.system("calc")

	elif ("open" in a) and ("settings" in a):
		os.system("set")

	elif (("send" in a) or ("message" in a)) and ("whatsapp" in a):
		x = input("enter number to send message: ")
		y = input("enter the message to send: ")
		os.system("chrome wa.me/91 "+x+" /? text = "+y+"")

	elif (("send" in a) or ("open" in a ) or ("message" in a)) and ("mail" in a):
		os.system("chrome mail.google.com")

	elif ("exit" in a) or ("stop" in a) or ("quit" in a) or ("close" in a):
		break
	else:
		print("dont support")