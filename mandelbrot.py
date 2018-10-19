"""
Notes:
Mandelbrot equation: z = z^2 + c

Sources;
http://0pointer.de/blog/projects/mandelbrot.html
https://introcs.cs.princeton.edu/python/32class/mandelbrot.py.html
"""
from PIL import Image
import cmath

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

maxCalc = 300 #how many times value should be calculated to see if it escapes

image = Image.new("RGB",(imgx, imgy))

for y in range(imgy):
	#zy: y component of complex number z
	#have to scale the grid values (-2 to 2) to fit in (0 to 255)
	zy = y *(y2-y1)/(imgy-1) +y1
	# print(y)
	# print(zy)
	for x in range(imgx):
		#zx: x component of complex number z
		#used same scaling method as above for zx
		zx = x * (x2-x1)/(imgx-1) + x1
		#calculate z using formula given on demo
		z = cmath.sqrt(zx**2 + zy**2)
		#store first value of z into c value so it can be added after each check to see if that point has "escaped"
		c = z

		#loop only checks first -maxCalc- z values to see if point has escaped
		for count in range(maxCalc):
			#if the point escapes (higher than 2), the loop is exited
			if abs(z) >= 2:
				break
			#if on the first iteration, the point hasn't escaped, the next value of z is calculated and loops through again
			z = z*z + c
		image.putpixel((x,y),(count%10 *100, count%100 *10, count%1 *100))




image.save("demo_image.png", "PNG")