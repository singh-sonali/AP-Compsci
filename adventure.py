
def start():
	result = input("\n\nYou are here to save the princess! \n\nShe has been kidnapped by Bowser and Bowser Jr. You are at a fork in the road, and you can either... \n\n1) Go ahead and save the Princess \n2) Turn back in shame and dishonor. \n\n>> ")

	if result == '1':
		savePrincess()
	elif result == '2':
		shame()
	else:
		print("I don't know what "+result+" means. Please type a 1 or a 2.")
		start()

def savePrincess():
	username = input("Brave soul, I believe you shall succeed on your journey! \nBefore we continue, tell me your name so the whole kingdom will know it is you who will save their beloved princess. \n\n >> ")
	result = input("Okay, " + username + " time for your journey to begin. Shall we head to \n 1)the mountains \n2)the forest to search for the princess? \n\n>> ")
	if result == '1':
		mountains()
	elif result == '2':
		forest()
	else: 
		print("Sorry", username, "I don't know what", result, "means. Please enter 1 or 2 to proceed.")


def shame():
	pass


start()