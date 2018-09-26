import random as r

#Create a list of 15 random numbers from 0-100
#Ask the user for one input from 0-100
#Append this input to the list
#Sort the list into descending order


#solution
a = []
for x in range(15):
	a.append(r.randrange(100))
print("The random list is:", a)
def list():
	user = int(input("What value would you like to add to the list? This value must be an integer between 0-100.\n>> "))
	if user <0 or user >100:
		print("Sorry,", user, "is not in the range I described. Please enter another value.")
		list()
	else:
		a.append(user)
	a.sort(reverse = True)
	print("The sorted list with your added value is:", a)

list()
