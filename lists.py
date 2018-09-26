import random as r
#empty list
a = []
#add something to list
a.append(4)
a.append(5)
a.append(3)
a.insert(0,1)
a = [1] + a

print(a[0],a[4])

#print(a)

b = [1,1,4,5,3]

#Removes first element it finds with the same value
#b.remove(2)

del b[0]

print(b)

#Prints last thing on the list and takes it off
print(b.pop())
print(b)

#Taking length of something and subtracting 1 will give you last thing in the list
print(b[len(b)-1])
#shortcut
print(b[-1])

#get variables to switch values
c = 5
d = 7

c, d = 5, 7
c, d = d, c #swap 

#swap
temp = c
c = d
d = temp

e = [1,2,3,7,5,6,4]
e[3], e[6] = e[6], e[3]

print(e)

f = []
for x in range(7, 707, 7):
	f.append(x)
print(f)
print(len(f))

g = []
for x in range(10):
	g.append(r.randrange(100))
print(g)
#g.sort()
#print(sorted(g))
g = sorted(g)
print(g)
