#Sonali Singh
#Kaki, Stephanie, Alex, Daniel
import random
base = int(input("Enter an INTEGER to serve as the base.\n>> "))
exponent = int(input("Enter an INTEGER to serve as the exponent.\n>> "))

def exponential():
	a = []
	i=0
	for x in range(exponent + 1):
		a.append(base**i)
		i+=1
	print("Tada:", a)

exponential()
