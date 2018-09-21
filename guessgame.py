import sys
import random

number = random.randrange(0,100,1)
#print(number)
guess = 0
guessCounter = 0
def start():
	global guess
	guess = int(input("Guess the integer I'm thinking of, between 1 and 100. \n >> "))
	if guess != number:
		if (guess > 100 or guess < 0):
			print("The number you guessed is not in the range I described. Please guess again.")
			start()

		elif guess > number:
			lower()

		elif guess < number:
			higher()

	if guess == number:
		win()


def win():
	global number
	print("Congratulations! You are a star guesser. You guessed my number," , number, ", correctly in", guessCounter, "tries!" )
	repeat = input("Would you like to play again? [Yes or No] \n >> ")
	if repeat == 'Yes':
		number = random.randrange(0,100,1)
		start()
	else:
		quit()
		

def lower():
	global guessCounter
	guessCounter += 1
	print("Good guess, but you're shooting too high. My number is less than", guess, "\n")
	print("GUESS AGAIN!")
	start()


def higher():
	global guessCounter
	guessCounter += 1
	print("Good guess, but you're swinging a bit low. My number is higher than", guess, "\n")
	print("GUESS AGAIN!")
	start()


	




start()