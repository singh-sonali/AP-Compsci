from PIL import Image

xa, xb = -2.0, 2.0
ya, yb = -2.0, 2.0

imgx, imgy = 512, 512

maxIt = 256

image = Image.new("RGB", (imgx, imgy))

for y in range(imgy):
	cy = y * (yb-ya)/(imgy-1) + ya
	for x in range(imgx):
		cx = x * (xb-xa)/(imgx-1) + xa
		c = complex(cx,cy)
		z = 0
		for i in range(maxIt):
			if abs(z)>= 2:
				break
			z = z**2 + c

		r = i
		g = 0
		b = 0
		image.putpixel((x,y),(r,g,b))

image.show()

	