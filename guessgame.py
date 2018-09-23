import sys
import random

number = random.randrange(0,100,1)
print(number)
guess = 0
guessCounter = 1
def guessgame():
	global guess
	while True:
		try:
			guess = int(input("Guess the integer I'm thinking of, between 1 and 100. \n >> "))
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
		except ValueError:
			print("I won't count that as a guess because that's not a number [ex; 1]. Try again.")
			guessgame()


def win():
	global number
	while guessCounter <=5:
		print("Congratulations! You are a star guesser. You guessed my number," , number,", correctly in", guessCounter, "tries!" )
		print("You now get to ")
		quit()
		break
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


	




guessgame()