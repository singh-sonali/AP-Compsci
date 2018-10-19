"""
Notes:
Mandelbrot equation: z = z^2 + c

Sources;
http://0pointer.de/blog/projects/mandelbrot.html
https://introcs.cs.princeton.edu/python/32class/mandelbrot.py.html
"""
from PIL import Image
import math

#image size dimensions
imgx = 256
imgy = 256

#Grid dimensions
#In class practice went from (-2,-2) to (2,2)
#Chose to use lower left corner and upper right corner coordinates because it was easier to scale
x1 = -2
y1 = -2
x2 = 2
y2 = 2

maxCalc = 1000 #how many times value should be calculated to see if it escapes

image = Image.new("RGB",(imgx, imgy))

for y in range(imgy):
	#cy: y component of complex number c
	#have to scale the grid values (-2 to 2) to fit in (0 to 255)
	cy = y *(y2-y1)/(imgy-1) +y1
	for x in range(imgx):
		#cx: x component of complex number c
		#used same scaling method as above for cx
		cx = x * (x2-x1)/(imgx-1) + x1
		# initial value of z is always 0
		z = 0
		# put the imaginary component (cy) and real component of (cx) into one complex number c
		c = complex(cx, cy)

		#loop only checks first -maxCalc- z values to see if point has escaped
		for count in range(maxCalc):
			#if the point escapes (higher than 2), the loop is exited
			if abs(z) >= 2:
				break
			#if on the first iteration, the point hasn't escaped, the next value of z is calculated and loops through again
			z = z*z + c
		image.putpixel((x,y),(count%32 *64, count%16 *18, count%64 *16))




image.save("mandel.png", "PNG")