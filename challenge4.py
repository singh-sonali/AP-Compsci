#Sonali Singh
#Ryan, Roshni, and Leo Challenge 
#Sources:
#https://pythontips.com/2013/07/28/generating-a-random-string/
import random
import string
import re
a= []
for x in range(10):
	a.append(''.join([random.choice(string.ascii_lowercase) for x in range(5)]))
print(a)

#[re.sub('['a']+','',_) for _ in a]
#print(a)