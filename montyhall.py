#Sonali Singh
#Monty Hall
#I would always switch, for the hypothesis confirmed at the end of the code. 

import random as r

def noswitch():
	win = 0
	lose = 0
	for x in range(1000):
		boxA = "A"
		boxB = "B"
		boxC = "C"

		boxes = ["A", "B", "C"]

		#choose a random box to have the car, and a random box as your selection
		car = r.choice(boxes)
		choice = r.choice(boxes)

		#if you choose correctly you win because you don't switch
		if choice == car:
			boxes.remove(choice)
			box_opened = r.choice(boxes)
			win +=1

		#if you choose incorrectly, the other incorrect box is opened, but you lose because you can't switch
		else:
			#delete your choice
			for x in range(0, 3):
				if boxes[x] == choice:
					del boxes[x]
					break

			#open the one of the remaining two boxes that doesn't have the keys
			for x in range(0, 2):
				if car!= boxes[x]:
					del boxes[x]
					lose+=1
					break
	print("No switches... Wins:",win,"and Losses:", lose)
noswitch()

def switch():
	win = 0
	lose = 0
	for x in range(1000):
		boxA = "A"
		boxB = "B"
		boxC = "C"

		boxes = ["A", "B", "C"]

		#choose a random box to have the car, and a random box as your selection
		car = r.choice(boxes)
		choice = r.choice(boxes)

		#if you choose correctly initially, you switch to an incorrect box and you automatically lose
		if choice == car:
			boxes.remove(choice)
			alternate_choice = r.choice(boxes)
			lose +=1
			
		#if you choose incorrectly, the other incorrect box is opened , and you switch to the correct box!
		else:
			#delete your choice
			for x in range(0, 3):
				if boxes[x] == choice:
					del boxes[x]
					break

			#open the other incorrect of the remaining two boxes that doesn't have the keys
			for x in range(0, 2):
				if car!= boxes[x]:
					del boxes[x]
					break

			#the box you switch to is the third box (the one not chosen or revealed), and contains the car keys
			if boxes[0] == car:
				win+=1

	print("Always switch... Wins:",win,"and Losses:", lose)
switch()


#RESULTS EXPLAINED:
#You win more if you always switch. This is because initially there's a greater chance of opening a penny box (2:1). Since the other penny box that you didn't choose would be revealed right after, if you switched, the only box left would be the one with the keys! Basically, if you switch after choosing incorrectly initially, you win -  there's a greater chance of this happening because there are more incorrect boxes with pennies, thus a greater chance of winning.










