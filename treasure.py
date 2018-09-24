#Sonali Singh
#Adventure Game
#9-23-18
#Sources:
#https://www.thethings.com/15-stupidly-simple-riddles-most-people-cannot-solve-2/
#https://pulptastic.com/hurty-brains-ahead/
#https://thehelloworldprogram.com/python/python-string-methods/

import sys
import random
#These are variable counters that will change as the user goes through the game.
lives = 3
riddlenumber = 0

username = input("Before you begin, adventurous soul, tell me your name.\n>> ")

#This is the beginning method that is called at the bottom to begin the program.
def start():
	begin = input("\nWelcome to Treasure Island " + username + ". Should you choose to participate in this hunt, your mind will be stretched like never before. Answer each riddle correctly, and you will be one step closer to finding the secret treasure. \n\n Are you ready to begin? \n 1) Yes, I was born ready. \n 2) No, I don't want to find the super cool treasure. \n>> " )

	if begin == '1':
		hunt()
	elif begin == '2':
		shame()
#Simple error checking when the input is a string
	else:
		print("\nSorry," , begin , "is not a choice. Please select 1 or 2. \n")
		start()

def hunt():
	print("\nAlright", username, "let me tell you how this works. Each clue will be presented to you as a riddle. The answer to the riddle is always one word. If you answer the riddle correctly, you move on to the next clue with all lives intact.")
	test = input("Let's give you a practice riddle. \n What gets wet while drying? \n >> A...")

#This makes sure that even if a user capitalizes differently, the answer will still be correct.
	if test.upper() == 'TOWEL':
		print("\nYou're on fire! The answer is a towel. Nice going. If you get a riddle wrong on the journey ahead, you will have a choice to make. You may play a guessing game against me, and if you win in five tries, you may move ahead without losing a life. However, if you choose to play the game, and cannot guess my number in five tries, you lose all three lives and are out of the hunt. Of course your other option is to simply lose a life, and move on. Hopefully", username, "you'll never have to make that choice. Okay, enough talking. Let's begin!")
	else:
		print("\nOh no, that's disappointing. Your answer,", test, "is not correct. I will allow you to start the hunt without consequence but you should know... if you get another riddle wrong on the journey ahead, you will have a choice to make. You may play a guessing game against me, and if you win in five tries, you may move ahead without losing a life. However, if you choose to play the game, and cannot guess my number in five tries, you lose all three lives and are out of the hunt. Of course your other option is to simply lose a life, and move on. Hopefully" ,username ,"you'll never have to make that choice. Okay, enough talking. Let's begin!")
	r_one()

def shame():
	tryagain = input("\nOh, I'm sorry to hear that " + username + ". It takes a very unique soul to turn down the chance for an amazing treasure and journey. Since I'm feeling generous, I'll give you one more chance to change your mind. Do you want to: \n 1) Admit you were too hasty in saying no, and begin the treasure hunt \nor\n 2) Stick with your decision, and leave treasure island. \n>> ")
	if tryagain == '1':
		start()
	elif tryagain == '2':
		print("Oh well. Not everyone loves adventure, I guess. Goodbye for now " + username + "!")
		quit()
	else:
		print("\nThat's not a choice. Enter a 1 or a 2.")
		shame()
#the riddle functions are numbered: r_number
def r_one():
	global lives
	#riddlenumber assigns a number to each riddle so the user can go back to a specific riddle
	global riddlenumber 
	riddlenumber += 1

	r_one = input("\nTime for your first riddle.\nWhich word in the dictionary is spelled incorrectly? \n>> The word...")
	if r_one.upper() == 'INCORRECTLY':
		print("Correct. Nice going. You have", lives, "lives left. You get to move on to Riddle 2, and are one step closer to the treasure!")
		r_two()
	else:
		lives -= 1
		print("Your answer", r_one, "is not correct. You have" ,lives, "lives left.")
		#The wrong function is called everytime the user gets the answer to the riddle wrong.
		wrong()

def r_two():
	global lives
	global riddlenumber
	riddlenumber +=1

	r_two = input("\nWhoopee! Riddle two here you come! \nWhat gets bigger the more you take away?\n>> A...")
	if r_two.upper() == 'HOLE':
		print("Heck yeah! Another riddle down, four more to go. You have", lives, "lives left. Let's move on!")
		r_three()
	else:
		lives -= 1
		print("Your answer", r_two, "is not correct. You have" ,lives, "lives left.")
		wrong()

def r_three():
	global lives
	global riddlenumber
	riddlenumber +=1

	r_three = input("\nNext riddle. \nI have keys but no locks. I have a space but no room. You can enter but you can't go outside. What am I?\n>> I am a...")
	if r_three.upper() == 'KEYBOARD':
		print("Correct. Nice going. You have", lives, "lives left. You get to move on to Riddle 4, and are one step closer to the treasure!")
		r_four()
	else:
		lives -= 1
		print("Your answer", r_three, "is not correct. You have", lives, "lives left.")
		wrong()

def r_four():
	global lives
	global riddlenumber
	riddlenumber +=1

	r_four = input("\nRiddle up! \nIf you have me, you will want to share me. If you share me, you will no longer have me. What am I?\n>> I am a...")
	if r_four.upper() == 'SECRET':
		print("Good job! You have", lives, "lives left. Ready to move on? That's a rhetorical question. Onward!")
		r_five()
	else:
		lives -= 1
		print("Aw shucks! Your answer" ,r_four, "is not right. You have", lives, "lives left.")
		wrong()

def r_five():
	global lives
	global riddlenumber
	riddlenumber +=1

	r_five = input("\nRiddle number five!\nWhat travels around the world but always stays in the corner?\n>> A...")
	if r_five.upper() == 'STAMP':
		print("Oh my goodness! You are so close! Only one more riddle to go. Lives left:" , lives)
		r_six()
	else:
		lives -= 1
		print("Oh no, you were so close!! Your answer", r_five, "is not correct. You have", lives, "lives left.")
		wrong()

def r_six():
	global lives
	global riddlenumber
	riddlenumber +=1

	r_six = input("\nLAST RIDDLE!\nIt is greater than God; it is more evil than the Devil; the poor have it; the rich need it; and if you eat it, you will die. What is it?\n>>It is...")
	if r_six.upper() == 'NOTHING':
		print("AHHH!!! You did it!")
		grandprize()
	else:
		lives-=1
		print("SHOOT! You were so so close! You have", lives, "lives left!")
		if (lives >0):
			lastchance()

		else:
			print("You don't have any lives left! You almost had it! Please try playing again", username, "at some point! I have full faith in you that one day you'll get the treasure! Goodbye...")
			quit()

def grandprize():
	global lives
	global riddlenumber
	riddlenumber +=1
	print("YOU'VE REACHED THE TREASURE!!!!" ,username, "this is unbelievable. Are you ready for your booty?")
	print("Here you go!!!!!!")
	print("~~~DIAMONDS, RUBIES, SAPPHIRES, GLOWING GOLD~~~ all pop up in a chest in front of you. It all is yours. Enjoy, sensei", username, ",enjoy.")
	quit()

def lastchance():
	last_chance = input("You still have lives left. You can still try to win! Do you want to \n1) Play a guessing game against me for one last chance to get the treasure.\n2) Accept you've come this far, and leave with dignity to return another day. \n>> ")
	if last_chance == '1':
		print("You've got this.")
		guessgame()
	elif last_chance == '2':
		print("Oh man", username,"! You put forth a valiant effort. Congratulations, and goodbye.")
		quit()
	else:
		print("Sorry, I don't know what", last_chance, "means. Please enter a 1 or 2.")
		lastchance()


def wrong():
	while lives>0:
		choice = input("\nYou got that riddle wrong and you now have a choice. Do you want to... \n1)Move on to the next riddle with one less life \n2)Play a guessing game against me, in which you must guess the number I'm thinking of in five tries to keep your life. If you are unsuccessful in guessing, you lose all your lives and are out of the hunt. \n>> ")
		#If the user wants to move on to the next function while losing a life, the programs checks what riddle they were on and goes to the next riddle. 
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
		elif choice == '2':
			guessgame()
		else:
			print("Sorry," , choice, "is not a choice. Please enter a 1 or a 2.")
			wrong()
		break 
	else:
		print("Oh no! You're out of lives. Sorry, but you're out of the hunt!")
		quit()


#The code for the guessing game starts here.
guess = 0 #this is the value of the actual numerical guess
guessCounter = 1 #This is the number of guesses the user has made
number = random.randrange(0,100,1)
def guessgame():
	global guess
	#The user has five chances to guess the number, otherwise the program ends and asks to play again.
	while guessCounter <=5:
		try:
			guess = int(input("The stakes are high! Guess the integer I'm thinking of, between 1 and 100. \n>> "))
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

	print("Sorry, your attempt to save one of your lives was futile. You didn't guess my number in five tries. Unfortunately that means you lose all your lives and are out of the treasure hunt. Goodbye for now!")
	playagain()

def win():
	global number
	global riddlenumber
	print("Congratulations! You are a star guesser. You guessed my number," , number,", correctly in", guessCounter, "tries! You get to move on to the next riddle!!")
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
	elif riddlenumer == 6:
		grandprize()
		
		
def lower():
	global guessCounter
	guessCounter += 1
	print("\nGood guess, but you're shooting too high. My number is LESS than", guess, "\n")
	print("GUESS AGAIN!")
	guessgame()


def higher():
	global guessCounter
	guessCounter += 1
	print("\nGood guess, but you're swinging a bit low. My number is GREATER than", guess, "\n")
	print("GUESS AGAIN!")
	guessgame()

def playagain():
	again = input("Would you like to play again? [Y or N]\n>> ")
	if again == 'Y' or again == 'y':
		global username
		username = input("\nHi adventurous soul, what's your name?\n>> ")
		global number 
		number = random.randrange(0,100,1)
		start()
	elif again == 'N' or again == 'n':
		quit()
	else:
		print("That's not a choice!! Please enter a 1 or 2.")
		playagain()


	



start()

