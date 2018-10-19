import random
from PIL import Image

def draw_snake():
	y = 0
	x = random.randrange(512)

	r = random.randrange(256)
	g = random.randrange(256)
	b = random.randrange(256)

	while True:
		if x < 0 or x >= 512 or y >= 512: 
			break
		image.putpixel((x,y),(r,g,b))

		# rr = random.random();

		# if rr < .2:
		# 	x+=1
		# elif rr < .4:
		# 	x-=1
		# else:
		# 	y+=1;

imgx = 512
imgy = 512

image = Image.new("RGB",(imgx, imgy))

for i in range(100):
	draw_snake()

image.save("snakes_image.png", "PNG")
