import sys 
import math 

g = float(sys.argv[1])

if (g<0 or g>5):
	print ("The value you entered is not in the grade range 0-5")
	quit()

elif (g>= 4.85):
	print("A+")
elif (g<4.85 and g>= 4.7):
	print("A")
elif (g<4.7 and g>=4.5):
	print("A-")
elif (g<4.5 and g>=4.2):
	print("B+")
elif (g<4.2 and g>=3.85):
	print("B")
elif(g<3.85 and g>=3.5):
	print("B-")
elif(g<3.5 and g>=3.2):
	print("C+")
elif(g<3.2 and g>=2.85):
	print("C")
elif(g<2.85 and g>=2.5):
	print("C-")
elif(g<2.5 and g>=2):
	print("D+")
elif(g<2 and g>=1.5):
	print("D")
elif(g<1.5 and g>=1):
	print("D-")
else:
	print("Sorry, you failed. F.")
	

