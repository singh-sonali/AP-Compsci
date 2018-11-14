import PIL
from PIL import Image
from PIL import ImageFilter
import colorsys
import random as r

def bw_rainbow_filter():
	image = Image.open('grass.jpg')
	width, height = image.size
	print(width,height)
	image = image.convert('HSV')
	#upper left box to black and white
	for y in range(1, height//2):
		for x in range(1, width//2):
			h, s, v = image.getpixel((x,y))
			newcolor = h, 0, v
			image.putpixel((x,y), newcolor)

	#lower right box to black and white
	for y in range(height//2, height):
		for x in range(width//2, width):
			h, s, v = image.getpixel((x,y))
			newcolor = h,0,v
			image.putpixel((x,y), newcolor)
	
	#upper right box to rainbow
	for y in range(1, height//2):
		for x in range(width//2, width):
			h,s,v = image.getpixel((x,y))
			newcolor = (x-width//2)//3, s-20, v
			image.putpixel((x,y), newcolor)

	#lower left box to rainbow
	for y in range(height//2, height):
		for x in range(1,width//2):
			h,s,v = image.getpixel((x,y))
			newcolor = x//3,s-20,v
			image.putpixel((x,y), newcolor)
	image = image.filter(ImageFilter.SMOOTH)
	image.show()
#bw_rainbow_filter()

def glitch_saturation():
	image = Image.open('lighthouse.jpg')
	width, height = image.size
	image = image.convert('HSV')

	for y in range(height):
		for x in range(width):
			h,s,v = image.getpixel((x,y))
			newcolor = 255-h, 255-s, 255-v
			image.putpixel((x,y), newcolor)
	image.show()

#glitch_saturation()

def switcheroo():
	image = Image.open('grass.jpg')
	width, height = image.size
	image = image.convert('HSV')

	for y in range(height):
		for x in range(width):
			h,s,v = image.getpixel((x,y))
			newcolor = r.randrange(0,h+1), s, v
			image.putpixel((x,y), newcolor)
	image.show()

switcheroo()


