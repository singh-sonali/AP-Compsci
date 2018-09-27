#Sonali Singh
#Ms. Healey Challenge 2 
#Sources: 
#https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
#https://www.tutorialspoint.com/python/number_shuffle.htm

import random as r

a = [r.randrange(0,100) for x in range(10)]
print("Your random list with list comprehensions:", a)
r.shuffle(a)
print("Your newly shuffled list:", a)