import sys
import math
#Source for creating an array: https://www.w3schools.com/python/python_lists.asp

m = int(sys.argv[1])
d = int(sys.argv [2])
y = int(sys.argv [3])
# for m, 1 corresponds with Jan, 2 with Feb and so on

y0 = (y  -  (14  -  m)  //  12)

x = y0  +  y0//4  -  y0//100  +  y0//400

m0  =  m  +  12  *  ((14  -  m)  //  12)  -  2 

d0  =  (d  +  x  +  (31*m0)//  12) %  7 

# Needed to put in // to ensure integer division because floats produce fractional numbers of days, when days are a whole entity.

dow = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday" , "Friday" , "Saturday"]
print(dow[d0])

#y = y - (14-m) / 12
#x = yorig + yorig/4 - yorig/100 + yorig/400
#morig = m + 12 * ((14-m)/12) - 2
#dorig = (d + x + ((31*morig)/12) % 7