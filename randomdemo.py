import math
import random


# random.random() 
# produces a random number between 0 (inclusive) and 1
# random.randrange(0,101,10) # random between 0, 100 inclusive, multiples of 10

theta = input("Please enter a radian value for angle theta: ")
sintheta = math.sin(float(theta))
costheta = math.cos(float(theta))

result = ((sintheta) ** 2) + ((costheta) ** 2)
print (result)
