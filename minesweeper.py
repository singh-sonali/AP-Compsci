import sys
import random as r

width = int(sys.argv[1])
height = int(sys.argv[2])
bombs = int(sys.argv[3])
a = []
#board
for x in range(height + 2):
	b=[0]*(width + 2)
	a.append(b)
#placebombs
for x in range(bombs):
	w = r.randrange(width)
	h = r.randrange(height)
	a[w][h] = '*'

#couldn't really figure out how to check the surrounding squares
for i in range(height):
	if a[i+1][h] == '*':
		a[i][h] = 'B'
	if a[i-1][h] == '*':
		a[i][h] = 'U'
	if a[w][i+1] == '*':
		a[w][i] = 'R'
	if a[w][i-1] == '*':
		a[w][i] = 'L'

#Worked for around 1.5 hours, couldn't figure it out


#final 
for x in range(len(a)):
	print(*a[x])

