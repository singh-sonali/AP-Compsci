# Sonali Singh
# Monte Carlo Soccer Simulation
# 1/21/19
import random as r
from collections import Counter
import matplotlib.pyplot as plt

# keeps track of average miles per game run by player in season
miles_run = []
# number of games per season
games = 10

# function for season
def soccer_player(seasons):
    # run function for thousands of seasons to get Monte Carlo simulation
    for s in range(seasons):
        distance = 0

        # win_percent adds element of randomness and determines how many games are won and lost
        win_percent = r.randrange(0,100,10)
        games_won = int((win_percent/100)*games)
        games_lost = games - games_won

        # player can either be offensive, a goalie, or defensive
        position = ["Off", "Goal", "Def"]
        player = r.choice(position)

        # in games where the team wins, different players run different amounts (miles)
        for g in range(games_won):
            # offensive players run anywhere from 5-9 miles
            if player == "Off":
                distance += r.uniform(5,9)
            # defensive players run anywhere from 2-7 miles
            if player == "Def":
                distance += r.uniform(2,7)
            # goalies run anywhere from 0.5-1.5 miles
            if player == "Goal":
                distance += r.uniform(0.5,1.5)

        # in games where team loses, players run within different distributions (different ranges used to make outcome more interesting)
        for g in range(games_lost):
            # offensive players run less than in winning games
            if player == "Off":
                distance += r.uniform(3,7.5)
            # defensive players run more than in winning games
            if player == "Def":
                distance += r.uniform(4,7)
            # goalies run more than in winning games
            if player == "Goal":
                distance += r.uniform(1.5, 2.5)
        # average distance per game is calculated and appended to the list for every season
        distance = round(distance/games,1)
        miles_run.append(distance)

# run simulation for many seasons to get defined results with nice smooth curve
soccer_player(100000)

# sorted & counter separate recurring distances
results = sorted(Counter(miles_run).items())
# has occurences for each distance
y_data = []
# distances
x_data = []

# add each sorted point to its respective dataset
for tuples in results:
    y_data.append(tuples[1])
    x_data.append(tuples[0])

# plot on line graph
plt.plot(x_data,y_data, color=(.5,0,.5,1.0))
plt.xlabel("Average Miles Run Per Game in Season")
plt.ylabel("Occurrences")
plt.title("How Much Does A Soccer Player Run?")
plt.show()
# OMH: Sonali Singh