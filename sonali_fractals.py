#Sonali Singh
#10/24/18
#Sources: Python PIL Documentation Website
#https://pillow.readthedocs.io/en/3.1.x/reference/Image.html

#CODE STARTS NOW!
import PIL

#Importing the modules from PIL that allow the creation of a picture, as well as some pre-specified image filters.
from PIL import Image
from PIL import ImageFilter

#The colorsys module enables conversions between types of color sets.
import colorsys as col
import random
import math

#Code for first Image.
#This method draws a swirly, bright picture.
def psychedelic_image():

	#These are the drawing area dimensions. (xa, xb) is the bottom left corner, and (ya,yb) is top right corner. xb and yb are defined in terms of xa and ya to ensure that the distance between x coordinates and y coordinate can remain the same without doing math. 
    xa = -0.65
    xb = 0.3 + xa
    ya = -0.58
    yb = 0.3 + ya
	
	#Max iterations allowed 
    maxIt = 256
	
	#Image dimensions
    imgx = 512
    imgy = 512
	
	#Creating image named "psychedelic"
    psychedelic = Image.new("RGB", (imgx, imgy))

	#I randomized the Julia set until I found a c value that produced a cool picture. I printed out c and copied the exact values so that c could be fixed to create that picture every time.
    c = complex(-0.6528756059172145,-0.4888112766214806)

    #Begin modified Julia set code. First lines for zx and zy are algorithms that scale the drawing area to the image size.
    for y in range(imgy):
        zy = y * (yb - ya) / (imgy - 1)  + ya
        for x in range(imgx):
            zx = x * (xb - xa) / (imgx - 1) + xa
            z = complex(zx, zy)

            #Point "escapes" if it's values exceeds the specified range within the max number of iterations. 
            for i in range(maxIt):
                if abs(z) >= 2.0: 
                    break 
                    
            #Modification here: increased the power of z to get more interesting shapes. Both z and c are of course complex numbers; they form the Julia set. 
                z = z **5 + c 

            #Using colorsys to define color using HSV. This will allow for brighter, more fun colors. I used i here so the colors vary for each pixel. I chose to include the values 0.58 and -0.28 randomly, as they are my ya and yb values.
            h,s,v = i/512, (i*0.58)/256, (i*-0.28)/64
            r,g,b = col.hsv_to_rgb(h,s,v)

            #RGB values must be integers in the range of 0-255.
            r = int(r*255)
            g = int(g*255)
            b = int(b*255)

            #Generating random multiples of the HSV values stored in R,G, and B to then mod by 256, for a proper (R,G,B) tuple.
            psychedelic.putpixel((x,y),((r*200)%256,(g*320)%256,(b*100)%256))

    #Applying one of the pre-made PIL image filters to get more detail. Then, picture is simply shown automatically instead of saved.
    psychedelic = psychedelic.filter(ImageFilter.DETAIL)
    psychedelic.show()




#This method draws an image created by a zoom on a specific area of the Julia set.
def zoom_julia_image():

    #Image Area Space. (xa, xb) is the bottom left corner, and (ya,yb) is top right corner. xa and ya were found as zoomed-in coordinates by experimentation. xb and yb are defined in terms of xa and xb respectively to ensure equal distances between x and y coordinates. 
    xa = -.54
    xb = 1.5 + xa
    ya = -.74
    yb = 1.5 + ya

    #Max iterations allowed
    maxIt = 256
    #Image dimensions
    imgx = 512
    imgy = 512

    #C value was found by randomizing Julia set and selecting, then copying, random c value that produced nice picture.
    c = complex(-0.5831868776269598,-0.4827115744172533)

    #Two images of the same design, but with different main colors are created.
    greenimage = Image.new("RGB", (imgx, imgy))
    redimage = Image.new("RGB", (imgx, imgy))

    #Begin modified Julia set code. First lines – defining zx,zy, and z – are simply algorithms to scale drawing area to the image size.
    for y in range(imgy):
        zy = y * (yb - ya) / (imgy - 1) + ya
        for x in range(imgx):
            zx = x * (xb - xa) / (imgx - 1) + xa
            z = complex(zx, zy)

            #Point "escapes" if it's values exceeds the specified range within the max number of iterations. 
            for i in range(maxIt):
                if abs(z) > 2.0: 
                    break 
                z = z * z + c

            #Tried using log for colors. Added simple mod to ensure that rgb values are in correct range. Even more complex use of variables is then implemented when coloring pixels.
            r = int(math.log(i*50) % 256)
            g = int(math.log(i*150) % 256)
            b = int(math.log(i*160) % 256)

    		#Experimenting with more complex ways to input RGB values. Discovered that avoiding a RGB tuple, and instead modifying r,g,b values in one expression produced exciting colors. Presume that PIL accepts a single value as a monochrome color. Red, zoomed-in Julia fractal is produced here using log colors.
            
            redimage.putpixel((x, y), r*10 + g%100 * b+ i)

            #Created another green image with not as complex assignment of colors, but the output was cool, so I'm putting the code for that here.

            #Simple mod for colors. More complex use of variables is then implemented when coloring pixels.
            greenr = i * 5 % 256
            greeng = i * 15 % 256
            greenb = i * 16 % 256

            #Creation of green image, with cool algorithm.
            greenimage.putpixel((x, y), greenr*1027 + greeng%332 * greenb+ i)


    redimage.show()
    greenimage.rotate(90).show()

#This method stacks two different images on top of each other to create another cool image. The base image uses the mandelbrot set, while the top decorative image was constructed using the julia set.
def stacked_images():
#Code for base image is first.

#These are the drawing area dimensions. (xa, xb) is the bottom left corner, and (ya,yb) is top right corner. xb and yb are defined in terms of xa and ya to ensure that the distance between x coordinates and y coordinate can remain the same without doing math. 
	xa = -1.5
	xb = 2+ xa
	ya = -1
	yb = 2+ ya

	#Image dimensions
	imgx, imgy = 512, 512

	#Max iterations allowed
	maxIt = 256
	baseimage = Image.new("RGB", (imgx, imgy))

	#This code uses the simple mandelbrot set detailed in class.
	for y in range(imgy):
		cy = y * (yb-ya)/(imgy-1) +ya 
		for x in range(imgx):
			cx = x * (xb-xa)/(imgx-1) +xa
			c = complex(cx,cy)

			#Value of z was modifed from 0 to -0.5 to change basic shape of mandelbrot fractal. Edges are made pointier.
			z = -0.5

			#Point "escapes" if it's values exceeds the specified range within the max number of iterations. 
			for i in range(maxIt):
				if abs(z)>= 2.0:
					break
				z = (z**2) + c 

			#Using colorsys to define color using HSV. This will allow for brighter, more fun colors. I used i here so the colors vary for each pixel. The mod values were chosen at random until I was satisfied with the color palette.
			h,s,v = i/512, (i*2)/256, (i*2)/64
			r,g,b = col.hsv_to_rgb(h,s,v)

			#RGB values must be integers in the range of 0-255.
			r = int(r*255)
			g = int(g*255)
			b = int(b*255)

			#Generating random multiples of the HSV values stored in R,G, and B to then mod by 256, for a proper (R,G,B) tuple.
			baseimage.putpixel((x,y),((r*200)%256,(g*320)%256,(b*100)%256))
	
	#Applied pillow image filter "SHARPEN" to increase clarity of base picture.
	baseimage = baseimage.filter(ImageFilter.SHARPEN)
	#Rotated base image by 90 degrees for horizontal symmetry.
	baseimage = baseimage.rotate(90)

#CODE FOR TOP (SUPERIMPOSED) IMAGE STARTS HERE
#These variables have "T" in front of them to signify they belong to the code of the top image

	#Drawing area dimensions. See comments above.
	Txa = -0.95
	Txb = 2 + Txa
	Tya = -1
	Tyb = 2 + Tya

	#Max iterations
	TmaxIt = 256 
	
	#Image dimensions need to match dimensions of the area on base picture where the top picture is being pasted.
	Timgx = 210
	Timgy = 210

	#Creating top image
	topimage = Image.new("RGB", (Timgx, Timgy))

	#Selected c value based on random value that produced cool design.
	Tc = complex(-0.780987977374866,-0.18958326731498987)

	#Code uses the Julia set as detailed in previous methods.
	for y in range(Timgy):
	    Tzy = y * (Tyb - Tya) / (Timgy - 1)  + Tya
	    for x in range(Timgx):
	        Tzx = x * (Txb - Txa) / (Timgx - 1) + Txa
	        Tz = complex(Tzx, Tzy)

	        #Modification from traditional Julia set. Changed value of escape to higher, for greater color variation.
	        for i in range(TmaxIt):
	            if abs(Tz) >= 10.0: 
	                break 
	        #Modification here: increased the power of z to get star shape. 
	            Tz = Tz **5 + Tc 

	        #Using colorsys to define color using HSV. This will allow for brighter, more fun colors. I used i here so the colors vary for each pixel. Mod values are same as for base picture, for color consistency.
	        hT,sT,vT = i/512, (i*2)/256, (i*2)/64
	        rT,gT,bT = col.hsv_to_rgb(hT,sT,vT)

	        #RGB values must be integers in the range of 0-255.
	        rT = int(rT*255)
	        gT = int(gT*255)
	        bT = int(bT*255)
	  		
	  		#Same color code as base image, for consistency.
	        topimage.putpixel((x,y),((rT*200)%256,(gT*320)%256,(bT*100)%256))

	#Filtered top image using pre-made PIL filter. Takes away the fill of the image and only shows vibrant edges. This created a cool effect, as the top image is the focal point in the stacked images.
	topimage = topimage.filter(ImageFilter.FIND_EDGES)

	#This pastes a rotated version of the top image, onto the base image. The area where the top image is being pasted is given in the "box=" tuple, with coordinates for top left and bottom right corners. Box size must equal top image size.
	baseimage.paste(topimage.rotate(45),box=(151,70,361,280),mask=None)

	#Showing final product - stacked images, or in other words, top image pasted on bottom image.
	baseimage.show()


#calling each method in order that they're written
psychedelic_image()
zoom_julia_image()
stacked_images()




	