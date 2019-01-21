import random as r
from collections import Counter
import matplotlib.pyplot as plt 

miles_run = []
games = 10
def soccer_player(seasons):
	for s in range(seasons):
		distance = 0
		win_percent = r.randrange(0,100,10)
		print(win_percent)
		games_won = int((win_percent/100)*games)
		games_lost = games - games_won
		position = ["Off", "Def", "Goal"]
		player = r.choice(position)
		for g in range(games_won):
			if player == "Off":
				distance += r.uniform(7.5,9)
			if player == "Def":
				distance += r.uniform(6,7.5)
			if player == "Goal":
				distance += r.uniform(1.5,2.5)
		for g in range(games_lost):
			if player == "Off":
				distance += r.uniform(6,7.5)
			if player == "Def":
				distance += r.uniform(7.5,9)
			if player == "Goal":
				distance += r.uniform(0.5, 1.5)
		distance = int(round(distance))
		miles_run.append(distance)

soccer_player(100000)

results = sorted(Counter(miles_run).items())
y_data = []
x_data = []
for tuples in results:
	y_data.append(tuples[1])
	x_data.append(tuples[0])


plt.plot(x_data,y_data)
plt.show()