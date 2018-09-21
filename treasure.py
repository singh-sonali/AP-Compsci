import sys
import random
lives = 3

username = input("Before you begin, adventurous soul, tell me your name.\n>> ")

def start():
	begin = input("\nWelcome to Treasure Island " + username + ". Should you choose to participate in this hunt, your mind will be stretched like never before. Answer each riddle correctly, and you will be one step closer to finding the secret treasure. \n\n Are you ready to begin? \n 1) Yes, I was born ready. \n 2) No, I don't want to find the super cool treasure. \n>> " )

	if begin == '1':
		hunt()
	elif begin == '2':
		shame()
	else:
		print("\nSorry," , begin , "is not a choice. Please select 1 or 2. \n")
		start()

def hunt():
	
	print("Alright", username, "let me tell you how this works. Each clue will be presented to you as a riddle. The answer to the riddle is always one word. If you answer the riddle correctly, you move on to the next clue with all lives intact.")
	test = input("Let's give you a practice riddle. \n What gets wet while drying? \n >> A...")
	if test == 'towel':
		print("You're on fire! The answer is a towel. Nice going. If you get a riddle wrong on the journey ahead, you will have a choice to make. You may play a guessing game against me, and if you win in five tries, you may move ahead without losing a life. However, if you choose to play the game, and cannot guess my number in five tries, you lose all three lives and are out of the hunt. Of course your other option is to simply lose a life, and move on. Hopefully", username, "you'll never have to make that choice. Okay, enough talking. Let's begin!")
	else:
		print("Oh no, that's disappointing. Your answer,", test, "is not correct. I will allow you to start the hunt without consequence but you should know... if you get another riddle wrong on the journey ahead, you will have a choice to make. You may play a guessing game against me, and if you win in five tries, you may move ahead without losing a life. However, if you choose to play the game, and cannot guess my number in five tries, you lose all three lives and are out of the hunt. Of course your other option is to simply lose a life, and move on. Hopefully" ,username ,"you'll never have to make that choice. Okay, enough talking. Let's begin!")

		
	r_one()

def shame():
	tryagain = input("\nOh, I'm sorry to hear that " + username + ". It takes a very unique soul to turn down the chance for an amazing treasure and journey. Since I'm feeling generous, I'll give you one more chance to change your mind. Do you want to: \n 1) Admit you were too hasty in saying no, and begin the treasure hunt \nor\n 2) Stick with your decision, and leave treasure island. \n>> ")
	if tryagain == '1':
		start()
	if tryagain == '2':
		print("Oh well. Not everyone loves adventure, I guess. Goodbye for now " + username + " !")
		quit()

def r_one():
	r_one == "Time for your first riddle. "


def wrong():
	print("Oh no, that one tricked you out. In order to move on, you must show me your skills - in a guessing game. Guess the number I'm thinking of...")

#The code for the guessing game starts here.
guess = 0
guessCounter = 0
number = random.randrange(0,100,1)






start()

