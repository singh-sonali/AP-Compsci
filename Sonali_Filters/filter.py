# Sonali Singh
# In-class filter project
# OMH: I have neither given nor received any unauthorized aid
import PIL
from PIL import Image
from PIL import ImageFilter
import colorsys
import random as r

# this method creates a rainbow filter
# in the written code, the picture is segmented into black and white boxes as well as rainbow boxes
# Note: I also created a separate image that applied the rainbow filter for the upper right box and lower left box, to the entire image, using a modified version of this code. 
def bw_rainbow_filter():
	# open image 
	# get width and height
	# convert color scheme to HSV
	image = Image.open('grass.jpg')
	width, height = image.size
	image = image.convert('HSV')

	# upper left box to black and white
	for y in range(1, height//2):
		for x in range(1, width//2):
			h, s, v = image.getpixel((x,y))
			newcolor = h, 0, v
			image.putpixel((x,y), newcolor)

	# lower right box to black and white
	for y in range(height//2, height):
		for x in range(width//2, width):
			h, s, v = image.getpixel((x,y))
			newcolor = h,0,v
			image.putpixel((x,y), newcolor)
	
	# upper right box to rainbow
	for y in range(1, height//2):
		for x in range(width//2, width):
			h,s,v = image.getpixel((x,y))
			newcolor = (x-width//2)//3, s-20, v
			image.putpixel((x,y), newcolor)

	# lower left box to rainbow
	for y in range(height//2, height):
		for x in range(1,width//2):
			h,s,v = image.getpixel((x,y))
			newcolor = x//3,s-20,v
			image.putpixel((x,y), newcolor)

	# apply built in pillow filter
	image = image.filter(ImageFilter.SMOOTH)
	image.show()


# creates a glitchy, supernatural filter for a picture
def glitch_saturation():
	# open image
	# get width and height
	# convert color scheme to HSV
	image = Image.open('lighthouse.jpg')
	width, height = image.size
	image = image.convert('HSV')

	for y in range(height):
		for x in range(width):
			h,s,v = image.getpixel((x,y))

			# reverse h, s, and v for "glitchy" effect
			newcolor = 255-h, 255-s, 255-v
			image.putpixel((x,y), newcolor)
	image.show()

# randomizes hues at certain points, as well as changes saturation, creating random bright and dark spots
def randomness():
	# open image
	# get width and height
	# convert color scheme to HSV
	image = Image.open('grass.jpg')
	width, height = image.size
	image = image.convert('HSV')

	for y in range(height):
		for x in range(width):
			h,s,v = image.getpixel((x,y))

			# change hue and saturation to get that sort of "random" cluster of colors
			newcolor = r.randrange(0, (h**2 +1)%255), (s+30)%255, v
			image.putpixel((x,y), newcolor)
	image.show()

# blends a background of a "starry night" with the given image
def starrynight():
	# open image
	# get width and height
	# convert color scheme to HSV
	image = Image.open('lighthouse.jpg')
	width, height = image.size
	image = image.convert('HSV')

	# using top image dimensions for star background
	star = Image.new("RGB", (width, height))

	# creating background with same colors as top image, just with a darker value to imitate night
	for x in range(1, width):
		for y in range(1, height):
			h,s,v = image.getpixel((x,y))
			star.putpixel((x,y), (h,s,v-150))

	# placing stars at specified locations for the lighthouse picture
	for s in range(700):
		h = height//1.25
		star.putpixel((r.randrange(1,width//1.35),r.randrange(1,h)), (255, 0, 255))
	for s in range(200):
		star.putpixel((r.randrange(width-200, width), r.randrange(1,h)), (255, 0, 255))
	for s in range(100):
		star.putpixel((r.randrange(width//1.35, width-200), r.randrange(height//2.7)), (255,0,255))

	# using the built-in blend function to blend both images, with an alpha constant of 0.95 ensuring that the background is clearly shown
	blend = Image.blend(image, star, 0.95)
	blend.show()

bw_rainbow_filter()
glitch_saturation()
randomness()
starrynight()


