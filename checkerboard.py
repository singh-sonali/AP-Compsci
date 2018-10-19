import random as r
from PIL import Image

imgx = 256
imgy = 256
image = Image.new("RGB",(imgx, imgy))
def draw_square(x,y,size,color):
	"""
	This method draws a square with the top left coordinate of x,y. 
	Arguments:
	x: x coordinate of top left corner
	y: y coordinate of top left corner
	size: dimension of square (height and width)
	color: color of square (red or black)
	"""
	for xcoor in range(x,x+size):
		for ycoor in range(y, y+size):
			image.putpixel((xcoor,ycoor),color)

def draw_checkerboard(size):
	"""
	Arguments:
	size: dimension of square (height and width)
	"""
	maincolor = (r.randrange(255),r.randrange(255),r.randrange(255))
	black = (0,0,0)
	currentcolor = black
	for xsquare in range(0, imgx, size):
		if currentcolor == maincolor:
			currentcolor = black
		else:
			currentcolor = maincolor
		for ysquare in range(0, imgy, size):
			if currentcolor == maincolor:
				currentcolor = black
			else:
				currentcolor = maincolor
			draw_square(xsquare,ysquare,size,currentcolor)

draw_checkerboard(64)

image.save("checkerboard.png", "PNG")