import sys
import math


binarynum = sys.argv[1]
number = 0
def toDecimal(binarynum):
i=0
#reverse string
	binarynum = binarynum[::-1]
#converts to decimal
	for num in binarynum:
		number += int(num)*2**i
		i+=1
	print(number)




toDecimal(binarynum)