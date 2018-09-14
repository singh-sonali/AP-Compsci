#Source: https://docs.python.org/3/library/math.html

import sys
import math

t = float(sys.argv[1])
v = float(sys.argv[2])

windchill = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * v ** 0.16
if (math.fabs(t) > 50 or v < 3 or v > 120):
	print("Windchill formula is not valid because either t or v is out of range.")

else:
	print("Windchill:" , windchill)

#is there a way to do the above three commands in one function?