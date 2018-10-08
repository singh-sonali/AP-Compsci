#Sonali Singh
#Minesweeper Project
#10/8/18
import sys
import random as r
#NOTE: This version allows you to remove flags without revealing what is at that point.

width = int(sys.argv[1])
height = int(sys.argv[2])
bombs = int(sys.argv[3])

directions = ("Welcome to Minesweeper. Here are some directions before you begin.\nBombs are randomly placed at certain points on the player grid before you. Every other point on the grid has a number which shows how many bombs are touching that point.\nEach time, you will have a chance to choose a coordinate on the grid where you either can place a flag (F), remove a flag, or reveal what is at that point.\nThe goal of the game is to place flags over all of the bombs. If you place a flag where there is no bomb, nothing happens.\nYou must remove this wrongly placed flag to win - you cannot win the game if you have flags over all of the bombs, and additional flags in the wrong places.\nIf you try to reveal a bomb, you lose.\nIf you place a flag over a bomb, and try to reveal that point, you will lose.\nYou can only take away an incorrectly placed flag by removing it.\nIt's time to begin. Good luck! \nIf at any time you would like to see these directions again, enter '3'.")
print(directions)

#height corresponds to the x coordinate
#width corresponds to the y coordinate
a = []
for x in range(height + 2):
	b=[0]*(width + 2)
	a.append(b)

#changes gutters to 1 so they won't cause an error later
for x in range(height+2):
	a[x][0] = 1
for x in range(height+2):
	a[x][width+1] = 1
for y in range(width+2):
	a[0][y] = 1
for y in range(width+2):
	a[height+1][y] = 1

#placebombs
for x in range(bombs):
	h = int(r.randrange(1, height))
	w = int(r.randrange(1, width))
#if a successive bomb is placed where there's already a bomb, a new location will be generated 
	while a[h][w] is '*':
		h = int(r.randrange(1, height))
		w = int(r.randrange(1, width))
	a[h][w] = '*'


#check the surrounding squares for bombs
for x in range(1,height + 1):
	for y in range(1,width + 1): #loops through all the x's and y's of the 2D array
	
		if a[x][y] is not '*':
			if a[x+1][y] == '*': #down
				a[x][y] += 1
			if a[x-1][y] == '*':				
				a[x][y] += 1
			if a[x][y+1] == '*':
				a[x][y] += 1
			if a[x][y-1] == '*':
				a[x][y] += 1
			if a[x+1][y+1] == '*':
				a[x][y] += 1
			if a[x+1][y-1] == '*':
				a[x][y] += 1
			if a[x-1][y-1] == '*':
				a[x][y] += 1
			if a[x-1][y+1] == '*':
				a[x][y] += 1


#solution board
# for x in range(1, height + 1):
# 	for y in range(1, width + 1):
# 		print(a[x][y],end=" ")
# 	print("")

#Game board
z = []
for x in range(height + 2):
	b=['x']*(width + 2)
	z.append(b)

#determine whether the flag was put in the right place
rightflag = 0
wrongflag = 0
def choice():
	global rightflag
	global wrongflag
	coordinate = input("Enter an X,Y coordinate to place a flag in or reveal. \nNote: x is the number of spaces across and Y is the number of spaces down. Ex; the upper left hand corner is 1,1\n>> ")
	#splits the x and y coordinates into two values 
	loc = coordinate.split(",")
	placechoice = input("Would you like to... \n1. Place a flag in this space\nor\n2. Reveal the contents of this space\nor\n3. Remove a flag\nor\n4. See the directions again\n>> ")
	#Place an "F" in the coordinate chosen
	if placechoice == '1':
		if z[int(loc[1])][int(loc[0])] == 'F':
			z[int(loc[1])][int(loc[0])] == 'F' #if the user wants to put a flag where there's already a flag, the program will allow it but won't change any of the flag counts
		else:
			z[int(loc[1])][int(loc[0])] = 'F'
			if a[int(loc[1])][int(loc[0])] == '*':
				rightflag += 1 #if the flag was placed correctly
			else:
				wrongflag +=1 #if the flag was placed incorrectly
			checkflags()


#reveal function depends on if you have a 0, a nonzero, or a bomb
	if placechoice == '2':
		if z[int(loc[1])][int(loc[0])] == 'F':
			wrongflag -= 1 #if the user reveals an incorrectly placed flag the wrong flag count is decreased. Note: A flag placed correctly on a bomb cannot be revealed because the game will end.
		checkflags()
		if a[int(loc[1])][int(loc[0])] == 0:
			checkaround(loc) #prints spaces around 0
		if a[int(loc[1])][int(loc[0])] == '*':
			print("Oh no! That's a bomb. Game over.")
			quit() #Can't reveal a bomb!
		else:
			z[int(loc[1])][int(loc[0])] = a[int(loc[1])][int(loc[0])] #If you reveal a non-zero number it simply is shown and you choose a new coordinate
	if placechoice == '3':
		if z[int(loc[1])][int(loc[0])] == 'F':
			z[int(loc[1])][int(loc[0])] = 'x'
			if a[int(loc[1])][int(loc[0])] == '*':
				rightflag -=1 #if they removed a correctly placed flag, the rightflag count decreases
			else:
				wrongflag-=1 #if they removed a flag over anything other than a bomb, the wrongflag count decreases
		else:
			print("That's not a flag; you can't remove it.")
		checkflags()
	if placechoice == '4':
		print(directions)


	stateboard()
	choice()
def stateboard(): #prints the game board
	for x in range(1, height + 1):
		for y in range(1, width + 1):
			print(z[x][y],end=" ")
		print("")


def checkaround(loc):
	zeroes = [] #stores the locations of the zeroes
	visited = [] #stores the locations of the zeroes already checked
	row = int(loc[1]) #user input
	col = int(loc[0])
	zeroes.append([row,col])
	while zeroes:
	#these lines store the location of the first zero in the list into a variable and then remove it from the checking list and add it to the "already visited" list
		firstval = zeroes[0]
		row = int(firstval[0])
		col = int(firstval[1])
		zeroes.remove(firstval)
		visited.append(firstval)
		for x in range(row-1, row+2):
			for y in range(col-1, col+2):
				if z[x][y] != 'F':
					z[x][y] = a[x][y]
				if a[x][y] == 0 and [x,y] not in visited:
					#add the zeroes that haven't been checked to the checking list
					zeroes.append([x,y])
					
def checkflags():
	if rightflag == bombs and wrongflag == 0:
		print("Yay! You placed flags over all the bombs! You win the game:)")
		quit()

stateboard()
choice()

