import sys
import random as r

width = int(sys.argv[1])
height = int(sys.argv[2])
bombs = int(sys.argv[3])


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
	h = int(r.randrange(2, height))
	w = int(r.randrange(2, width))
	while a[h][w] is '*':
		h = int(r.randrange(2, height))
		w = int(r.randrange(2, width))
	a[h][w] = '*'


#check the surrounding squares for bombs
for x in range(1,height + 1):
	for y in range(1,width + 1): #loops through all the x's and y's of the 2D array
	
		if a[x][y] is not '*':
			if a[x+1][y] == '*': #down
				a[x][y] += 1
			if a[x-1][y] == '*':					a[x][y] += 1
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
for x in range(1, height + 1):
	for y in range(1, width + 1):
		print(a[x][y],end=" ")
	print("")

#Game board
z = []
for x in range(height + 2):
	b=['x']*(width + 2)
	z.append(b)

#determine whether the flag was put in the right place
flagcount = 0
wrongflag = 0
def choice():
	global flagcount
	global wrongflag
	coordinate = input("Enter an X,Y coordinate to place a flag in or reveal. \nNote: x is the number of spaces across and Y is the number of spaces down\n>> ")
	#splits the x and y coordinates into two values 
	loc = coordinate.split(",")
	placechoice = input("Would you like to... \n1. Place a flag in this space\nor\n2. Reveal the contents of this space?\n>> ")
	#Place an "F" in the coordinate chosen
	if placechoice == '1':
		z[int(loc[1])][int(loc[0])] = 'F'
		if a[int(loc[1])][int(loc[0])] == '*':
			flagcount += 1 #if the flag was placed correctly
		else:
			wrongflag +=1 #if the flag was placed incorrectly

#reveal function depends on if you have a 0, a nonzero, or a bomb
	if placechoice == '2':
		if a[int(loc[1])][int(loc[0])] == 0:
			checkaround(loc) #prints spaces around 0
		elif a[int(loc[1])][int(loc[0])] == '*':
			print("Oh no! That's a bomb. Game over.")
			quit() #Can't reveal a bomb!
		else:
			z[int(loc[1])][int(loc[0])] = a[int(loc[1])][int(loc[0])] #If you reveal a non-zero number it simply is shown and you choose a new coordinate
	if flagcount == bombs and wrongflag == 0: #if you've placed all the flags where the bombs are and no wrong flags, you win
		print("You flagged all the bombs correctly! You've won the game:) Congrats!")
		quit()

		
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
				z[x][y] = a[x][y]
				if a[x][y] == 0 and [x,y] not in visited:
					#add the zeroes that haven't been checked to the checking list
					zeroes.append([x,y])
					

stateboard()
choice()

