import random as r
import matplotlib.pyplot as plt

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


for a in range(10000):
	coinflip()
#plt.plot([0,1,2,3,4,5,6,7,8,9,10],results, 'rs')
plt.bar([0,1,2,3,4,5,6,7,8,9,10],results, color=(.5,0,.5,1.0))
plt.show()
#print(results)
