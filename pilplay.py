from PIL import Image
import random as r

imgx = 512
imgy = 512

image = Image.new("RGB",(imgx, imgy))
image.putpixel((0,0),(255,0,0)) #colors left upper corner pixel as red

#changes entire picture to red
# for x in range (imgx):
# 	for y in range (imgy):
# 		image.putpixel((x,y),(255,0,0))

# some cool blue and red gradients
# for x in range (1, imgx):
# 	for y in range (1, imgy):
# 		image.putpixel((x,y),(300 * 100//x,0, 300 * 100//y))

# i = 1
# while i<imgx-15:
# 	for x in range (i, i+15):
# 		for y in range (1,imgy):
# 		# for x in range(1, imgx//x):
# 		# 	for y in range(1, imgy//y):
# 			image.putpixel((x,y),(15*(x//255),0, 0))
# 	i+=15
bands = 12
bandwidth = imgx//bands
for b in range (0,bands):
	for col in range(0,bandwidth):
		for y in range (0, imgy):
			image.putpixel((col+b*bandwidth,y),(0,int(255-(col/(bandwidth-1))*255), 0)) 

			


		
		 

image.save("demo_image.png", "PNG")