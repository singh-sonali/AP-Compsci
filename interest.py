import sys
import math 

P = float(sys.argv[1])
r = float(sys.argv[2])
t = (float(sys.argv[3]))/100


# e = math.e
from decimal import Decimal
# source = https://gist.github.com/jackiekazil/6201722

money = Decimal(P * (math.e ** (r*t)))
output = round(money, 2)

print("You would have...")
print("Dollars:" , output)