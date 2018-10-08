# def add(x,y):
# 	return x+y
# print(add(5,6))

# def is_even(n)
# 	if (n%2) == 0:
# 		return True
# 	return False

#base cases stop recursion from repeating itself
#no calculations are required for these, the program just knows them

# def fact(n):
# 	if n is 0 or n is 1:
# 		return 1
# 	return n * fact(n-1)
# ui = int(input("Pick a number:"))
# print(fact(ui))


# def countx(n):
# 	xcount = 0
# 	for letter in n:
# 		if letter == 'x':
# 			xcount +=1
# 	return xcount
# ui = input("Enter some characters and I'll count the x's: ")
# print(countx(ui))

# def crazy_eights(n):
# 	eightcount = 0
# 	for eight in n:
# 		if eight == '8':
# 			eightcount +=1
# 		if eight == '88':
# 			eightcount += 3

# 	return eightcount
# ui = input("Enter a group of numbers and I'll tell you how many 8s there are: ")
# print(crazy_eights(ui))

def euclid(a,b):
	if a<b:
		a,b = b,a
	r = a%b
	print(r)
	if r != 0:
		a = b
		b = r
		return euclid(a,b)
	if r == 0:
		return b
ui = input("Enter two numbers a,b for me to find the GCD of: ") 
value = ui.split(",")
print("GCD:", euclid(int(value[0]),int(value[1])))


