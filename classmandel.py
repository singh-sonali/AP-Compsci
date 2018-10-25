import PIL
from PIL import Image
from PIL import ImageFilter
import colorsys as col

def stack_images():
	xa = -1.5
	xb = 2+ xa
	ya = -1
	yb = 2+ ya

	imgx, imgy = 512, 512

	maxIt = 256
	image = Image.new("RGB", (imgx, imgy))
	for y in range(imgy):
		cy = y * (yb-ya)/(imgy-1) +ya 
		for x in range(imgx):
			cx = x * (xb-xa)/(imgx-1) +xa
			c = complex(cx,cy)
			z = -0.5
			for i in range(maxIt):
				if abs(z)>= 2.0:
					break
				z = (z**2) + c 
			h,s,v = i/512, (i*2)/256, (i*2)/256
			r,g,b = col.hsv_to_rgb(h,s,v)
			r = int(r*255)
			g = int(g*255)
			b = int(b*255)
			image.putpixel((x,y),((r*200)%256,(g*320)%256,(b*100)%256))
			# h,s,v = (i*-yb)/256, (i*yb)/512, i/128
			# r,g,b = col.hsv_to_rgb(h,s,v)

			# r = int(r*255)
			# g = int(g*255)
			# b = int(b*255)
			# print(r,g,b)
			# image.putpixel((x,y),((r*200)%256,(g*320)%256,(b*100)%256))
	image = image.filter(ImageFilter.SHARPEN)
#image.show()
	image = image.rotate(90)

#CODE FOR OP IMAGE STARTS HERE
#New Picture
#These variables have "T" in front of them to signify they belong to the code of the top image
	Txa = -0.95
	Txb = 2 + Txa
	Tya = -1
	Tyb = 2 + Tya
	TmaxIt = 256 # iterations
	# image size
	Timgx = 210
	Timgy = 210
	topimage = Image.new("RGB", (Timgx, Timgy))
	# Julia set to draw
	Tc = complex(-0.780987977374866,-0.18958326731498987)

	print(Tc)

	for y in range(Timgy):
	    Tzy = y * (Tyb - Tya) / (Timgy - 1)  + Tya
	    for x in range(Timgx):
	        Tzx = x * (Txb - Txa) / (Timgx - 1) + Txa
	        Tz = complex(Tzx, Tzy)
	        for i in range(TmaxIt):
	            if abs(Tz) >= 2.0: 
	                break 
	            Tz = Tz **5 + Tc 
	        hT,sT,vT = i/512, (i*2)/256, (i*2)/256
	        rT,gT,bT = col.hsv_to_rgb(hT,sT,vT)

	        rT = int(rT*255)
	        gT = int(gT*255)
	        bT = int(bT*255)
	        print(rT,gT,2)
	        topimage.putpixel((x,y),((rT*200)%256,(gT*320)%256,(bT*100)%256))
	image.paste(topimage,box=(151,70,361,280),mask=None)
	image.show()

stack_images()
#image2.show()
#PIL.Image.blend(image,image2, 0.5).show()



	