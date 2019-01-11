# Sonali Singh
# Monte Carlo Walk Simulation
# The longest walk you can take where you'll be within walking distance at least 50% of the time, is 22 blocks. 23 blocks is much over 50%. 21 blocks is consistently in the low 40s and high 30s percent range.

# Running a Monte Carlo simulation is what helps us determine the above solution. The Monte Carlo simulation is a mathematical technique that shows a range of possible outcomes and the probabilitiees they will occur for any path of action. It is used in decision-making processes. For example, in this random walk simulation, we used the Monte Carlo method by running a large random sample of walks, and seeing the probabilities that you would end up within walking distance at the end of each walk. By running this simulation 1000 times for many different walk lengths, you can see that on average, a 22 block walk is the length that will give you a probability of about 50%.


import random as r
home = (0,0)
num_walks = 1000
walkback = 0

def random_walk(blocks):
	#initial position is at home
	position = [0,0]
	directions = ["N","S","E","W"]
	for x in range(blocks):

		#choose a random direction, and change coordinates accordingly
		choice = r.choice(directions)
		if choice == "N":
			position[1]+=1
		if choice == "S":
			position[1]-=1
		if choice == "E":
			position[0]+=1
		if choice == "W":
			position[0]-=1

	#The distance from home is the sum of lateral and vertical blocks you are away from home. Sign doesn't matter when finding the total. (0,-10) and (0,10) are the same distance.
	dist_home = abs(position[0]) + abs(position[1])
	return dist_home

#Monte Carlo simulation
#Run large sample of walks with random outcomes displaying probabilities for any length of walk
for walks in range(num_walks):
	random_walk(22)
	if random_walk(22)<=4:
		walkback +=1

#Calculate percent
percent_walkback = 100*walkback//num_walks
print("You walked back home", percent_walkback,"percent of the time.")


