import sys
import random

def start():
	begin = input("\nWelcome to Treasure Island. Should you choose to participate in this hunt, your mind will be stretched like never before. Answer each riddle correctly, and you will be one step closer to finding the secret treasure. \n\n Are you ready to begin? \n 1) Yes, I was born ready. \n 2) No, I don't want to find the super cool treasure. \n>>" )

	if begin == '1':
		hunt()
	elif begin == '2':
		shame()
	else:
		print("Sorry, " + begin + " is not a choice. Please select 1 or 2.")
		start()

def hunt():
	pass

def shame():
	pass




def wrong():
	"Oh no, that one tricked you out. In order to move on, you must show me your skills - in a guessing game. Guess the number I'm thinking of..."
start()

