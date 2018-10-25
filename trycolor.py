import colorsys as c
from PIL import Image
imgx = 256
imgy = imgx
image = Image.new("HSV", (imgx,imgy))
h,s,v = 0.5, 0.5, 0.5
r,g,b = c.hsv_to_rgb(h,s,v)


r = int(r*255)
g = int(g*255)
b = int(b*255)
print(r,g,b)
for x in range(1,imgx):
	for y in range(1,imgy):
		image.putpixel((x,y), r%x*g*b)

image.show()