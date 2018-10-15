def moves(n, left):
	if n==0:
		return
	moves(n-1, not left)
	if left:    
		print(str(n)+'  left')
	else:    
		print(str(n)+'  right')
	moves(n-1,not left) 

print(moves(2,True))

#n discs where n is the biggest disc and 1 is the smallest disc


