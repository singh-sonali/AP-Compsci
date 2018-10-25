import colorsys as c
from PIL import Image
imgx = 256
imgy = imgx
image = Image.new("HSV", (imgx,imgy))
h,s,v = 0.5, 0.5, 0.5
r,g,b = c.hsv_to_rgb(h,s,v)

print(r,g,b)
r = int(r*255)
g = int(g*255)
b = int(b*255)

for x in range(50,100):
	for y in range(50,100):
		image.putpixel((x,y), (r,g,b))

image.show()