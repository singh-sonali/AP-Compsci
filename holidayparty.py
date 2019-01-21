import random as r
from collections import Counter
import matplotlib.pyplot as plt

calorie_distribution=[]
def holiday_party(trials):
	for t in range(trials):
		party = r.randrange(1,14)
		total_calories = 0

		for p in range(party):
			serving = r.randrange(1,9)
			for s in range(serving):
				calories = r.randrange(40,501)
				total_calories+=calories
		calorie_distribution.append(total_calories)

holiday_party(100000)

results = sorted(Counter(calorie_distribution).items())
y_data = []
x_data = []
for tuples in results:
	y_data.append(tuples[1])
	x_data.append(tuples[0])


plt.plot(x_data,y_data)
plt.show()


