# September 8, 2018
# Sonali's Computer Conversation
# No outside sources (experimented with if and elif from a previous program).
print("Hello!")
username = input("What would you like me to call you? ")
print("Well, hello there " + username + "!")
feeling = input("How are you feeling today? Good or Bad? ")
if (feeling == "Bad"):
	print("Oh no, I'm sorry to hear that!")
elif (feeling == "Good"):
	print("Nice to hear you're feeling " + feeling + ", " + username + "!")
print("Let's get to know each other.")
color = input("What's your favorite color? ")
print("Isn't that weird? My favorite color is " + color + " too!")
origin = input("Where are you from " + username + "? ")
print("Nice! I hear " + origin + " is a really beautiful place!")
food = input("What's the best dish that you've eaten in " + origin + ", " + username + "? ")
print("Yum!")
icecream = input("Ok, now a game! Guess my favorite icecream flavor! Chocolate, Vanilla, or Strawberry? ")
if(icecream == "Chocolate"):
	print("Sorry, you guessed wrong! It's strawberry!!")
elif (icecream == "Vanilla"):
	print("Sorry, you guessed wrong! It's strawberry!!")
elif(icecream == "Strawberry"):
	print("You got it " + username + ", strawberry is my absolute favorite!")
meeting = input("When are you free to talk again? I feel like I know you so well already. ")
print("Ok, " + username + " I'll talk to you " + meeting + ". Maybe we can meet in " + origin + " and eat some " + food + "! ")
print("Bye for now!")