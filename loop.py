
while True:
	try:
		num = int(input("Pick a number between 1 and 5: "))
		while num< 1 or num>5:
			num = int(input("That's not in the right range. Pick a number between 1 and 5: "))
		break

		#if the above is successful, it will stop looping
	except ValueError:
		print("That's not a number. Try again.")

count = 0;



print("Success!")













#def Check(choice, a, b):
	#while choice!= a and choice!= b: 
		#choice = input("Please select "+a+" or "+b+" : ")

#choice = input("Input y or n")
#if Check(choice, 'y', 'n') == 'y':
	#start()
