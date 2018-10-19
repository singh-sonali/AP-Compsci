from PIL import Image
import random as r

dimension = 32
image = Image.new("RGB",(dimension, dimension))

color = True
for w in range (0, 8):
	for h in range(0, 8):
		for x in range(7, dimension):
			for y in range(7, dimension):
				image.putpixel((x-w,y-h),(255,0,0))
			

image.save("demo_image.png", "PNG")