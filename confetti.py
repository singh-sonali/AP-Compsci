import random as q
from PIL import Image

def confetti():
	y = 0
	x = q.randrange(512)
	r = q.randrange(256)
	g = q.randrange(256)
	b = q.randrange(256)

	while True:
		if x>=512 or x<0 or y>=512:
			break
		image.putpixel((x,y),(r,g,b))

		random = q.random()
		if random < .1:
			x+=4
		elif random < .5:
			x-=1
		else:
			y+=1
image = Image.new("RGB",(512, 512))
for a in range(100):
	confetti()

image.save("confetti.png","PNG")

