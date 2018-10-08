import sys
import random as r

width = int(sys.argv[1])
height = int(sys.argv[2])
bombs = int(sys.argv[3])

w = [0] * width
h = [0] * height 

w = [w for x in range(10)]