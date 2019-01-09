import random as r
results = [0,0,0,0,0,0,0,0,0,0,0]
def coinflip():
	heads = 0
	for x in range(10):
		flip = r.randrange(1,3,1)
		if flip == 1:
			heads +=1
	for x in range(0,11):
		if heads == x:
			results[x] = results[x] + 1


for a in range(120):
	coinflip()
print(results)
