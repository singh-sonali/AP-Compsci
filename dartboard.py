# Sonali
import random as r
import math
#The special value approaches pi (3.14) as more and more darts are thrown. 
def dartboard(darts):
	win = 0
	for d in range(darts):
		# dart_x = 2*r.random()
		# dart_y = 2*r.random()
		dart_x = (r.randrange(-1001,1001))/1000
		dart_y = (r.randrange(-1001,1001))/1000
		position = [dart_x, dart_y]
		if math.sqrt((position[0])**2+(position[1])**2) < 1:
			win+=1
	output = (win*4)/darts
	print("Wins:", win)
	print("Special value:", output)

dartboard(1000)