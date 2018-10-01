i = [[1,2,3],[4,5,6],[7,8,9]]
i[0][0]

print(i[2][1])

j=[]
for x in range(10):
	j.append(0)
#print(j)

j = [0]*10
#print(j)

#creating a 2D list
j=[]
for x in range(10):
	k = [0]*10
	j.append(k)
print(j)

#this line is equivalent to lines 15-18
j = [[0]*10 for x in range(10)]
#j = [[x]*10 for x in range(10)]
#print(j)

#printing pretty!
for x in range(len(j)):
	print(*j[x])
# * "unpacks" the list, which takes away the extra syntax
