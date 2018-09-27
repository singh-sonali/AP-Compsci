#Sonali Singh
#Ms. Healey Challenge
import random as r

a = []
for x in range(10):
	a.append(r.randrange(100))
print("This is the random list:", a)
a.sort(reverse=True)
print("This is the random list in descending order:"
	, a)
#Source for removing multiples
#https://thispointer.com/python-how-to-remove-multiple-elements-from-list/
a = [elem for elem in a if elem%3 != 0]
print("This is the list without multiples of three:", a)