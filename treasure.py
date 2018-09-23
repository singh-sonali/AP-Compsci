import sys
import random
lives = 3
riddlenumber = 0

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
	
	print("\nAlright", username, "let me tell you how this works. Each clue will be presented to you as a riddle. The answer to the riddle is always one word. If you answer the riddle correctly, you move on to the next clue with all lives intact.")
	test = input("Let's give you a practice riddle. \n What gets wet while drying? \n >> A...")
	if test == 'towel':
		print("\nYou're on fire! The answer is a towel. Nice going. If you get a riddle wrong on the journey ahead, you will have a choice to make. You may play a guessing game against me, and if you win in five tries, you may move ahead without losing a life. However, if you choose to play the game, and cannot guess my number in five tries, you lose all three lives and are out of the hunt. Of course your other option is to simply lose a life, and move on. Hopefully", username, "you'll never have to make that choice. Okay, enough talking. Let's begin!")
		r_one()
	else:
		print("\nOh no, that's disappointing. Your answer,", test, "is not correct. I will allow you to start the hunt without consequence but you should know... if you get another riddle wrong on the journey ahead, you will have a choice to make. You may play a guessing game against me, and if you win in five tries, you may move ahead without losing a life. However, if you choose to play the game, and cannot guess my number in five tries, you lose all three lives and are out of the hunt. Of course your other option is to simply lose a life, and move on. Hopefully" ,username ,"you'll never have to make that choice. Okay, enough talking. Let's begin!")
		r_one()

def shame():
	tryagain = input("\nOh, I'm sorry to hear that " + username + ". It takes a very unique soul to turn down the chance for an amazing treasure and journey. Since I'm feeling generous, I'll give you one more chance to change your mind. Do you want to: \n 1) Admit you were too hasty in saying no, and begin the treasure hunt \nor\n 2) Stick with your decision, and leave treasure island. \n>> ")
	if tryagain == '1':
		start()
	elif tryagain == '2':
		print("Oh well. Not everyone loves adventure, I guess. Goodbye for now " + username + " !")
	else:
		print("\nThat's not a number. Enter a 1 or a 2.")
		shame()

def r_one():
	global lives
	#provides a reference so the user can go back to the exact riddle it was on
	global riddlenumber 
	riddlenumber += 1

	r_one = input("\nTime for your first riddle.\nWhich word in the dictionary is spelled incorrectly? \n>>The word...")
	if r_one == 'incorrectly' or r_one == 'Incorrectly':
		print("Correct. Nice going. You have", lives, "lives left. You get to move on to Riddle 2, and are one step closer to the treasure!")
		r_two()
	else:
		print("Your answer", r_one, "is not correct. The correct answer is the word 'incorrectly'.")
		lives -= 1
		wrong()

def r_two():
	global lives
	global riddlenumber
	riddlenumber +=1

	r_two = input("\n Whoopee! Riddle two here you come! \n What gets bigger the more you take away?\n>> A...")
	if r_two == 'hole' or r_two == "Hole":
		print("Heck yeah! Another riddle down, four more to go. You have", lives, "left. Let's move on!")
		r_three()
	else:
		print("Your answer", r_two, "is not correct. The correct answer is a hole.")
		lives -= 1
		wrong()

def r_three():
	global lives
	global riddlenumber
	riddlenumber +=1
def r_four():
	global lives
	global riddlenumber
	riddlenumber +=1

	r_four = input("\nNext riddle. \nI have keys but no locks. I have a space but no room. You can enter but you can't go outside. What am I?\n>> I am a...")
	if r_four == 'keyboard' or r_four == "Keyboard":
		print("Correct. Nice going. You have", lives, "lives left. You get to move on to Riddle 5, and are one step closer to the treasure!")
		r_five()
	else:
		print("Your answer", r_four, "is not correct. The correct answer is a keyboard.")
		lives -= 1
		wrong()
def r_five():
	global lives
	global riddlenumber
	riddlenumber +=1
def r_six():
	global lives
	global riddlenumber
	riddlenumber +=1
def grandprize():
	global lives
	global riddlenumber
	riddlenumber +=1
#edit
def wrong():
	choice = input("\nYou got that riddle wrong and you now have a choice. Do you want to... \n1)Move on to the next riddle with one less life \n2)Play a guessing game against me, in which you must guess the number I'm thinking of in five tries to keep your life. If you are unsuccessful in guessing, you lose all your lives and are out of the hunt. \n>> ")
	if choice == '1':
		if riddlenumber == 1:
			r_two()
		elif riddlenumber == 2:
			r_three()
		elif riddlenumber == 3:
			r_four()
		elif riddlenumber == 4:
			r_five()
		elif riddlenumber == 5:
			r_six()
		else:
			print("You were so close! Sorry, but you don't get the lovely treasure just yet. I have to say goodbye for now, but please play again!")
	elif choice == '2':
		guessgame()
	else:
		print("Sorry," , choice, "is not a choice. Please enter a 1 or a 2.\n>>")
		wrong()


#The code for the guessing game starts here.
guess = 0
guessCounter = 1
number = random.randrange(0,100,1)
def guessgame():
	print(number)
	global guess
	while True:
		try:
			guess = int(input("The stakes are high! Guess the integer I'm thinking of, between 1 and 100. \n >> "))
			if guess != number:
				if (guess > 100 or guess < 0):
					print("I won't count that as a guess because the number you guessed is not in the range I described. Please guess again.")
					guessgame()

				elif guess > number:
					lower()

				elif guess < number:
					higher()

			if guess == number:
				win()
			break
		except ValueError:
			print("I won't count that as a guess because that's not a number [ex; 1]. Try again.")
			guessgame()


def win():
	global number
	global riddlenumber
	if guessCounter <=5:
		print("Congratulations! You are a star guesser. You guessed my number," , number,", correctly in", guessCounter, "tries!" )
		if riddlenumber == 1:
			r_two()
		elif riddlenumber == 2:
			r_three()
		elif riddlenumber == 3:
			r_four()
		elif riddlenumber == 4:
			r_five()
		elif riddlenumber == 5:
			r_six()
	if guessCounter > 5:
		print("Sorry, your attempt to save one of your lives was futile. You didn't guess my number in five tries. Unfortunately that means you lose all your lives and are out of the treasure hunt. Goodbye for now!")
		quit()
	#repeat = input("Would you like to play again? [Yes or No] \n >> ")
	#if repeat == 'Yes':
		#number = random.randrange(0,100,1)
		#guessgame()
	#else:
		#quit()
		

def lower():
	global guessCounter
	guessCounter += 1
	print("Good guess, but you're shooting too high. My number is less than", guess, "\n")
	print("GUESS AGAIN!")
	guessgame()


def higher():
	global guessCounter
	guessCounter += 1
	print("Good guess, but you're swinging a bit low. My number is higher than", guess, "\n")
	print("GUESS AGAIN!")
	guessgame()


	



start()

