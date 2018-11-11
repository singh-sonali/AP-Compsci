# Anjali Mangla
# 10/25/2018
# On my honor, I have neither given nor received unauthorized aid
# This code produces 4 different images. 2 are representations of the mandelbrot set, and two are different zooms of the same input of complex number c into the julia set. As you go down the code, I will provide in-depth explanations of the ways I manipulated coloring and zooms to obtain the view of the fractal I have.
# All of the location zoom coordinates were results of hours of nitpicking by me because I didn't want to use the HTML site (I wanted to see if I could do it myself and learn how the zoom of the complex numbers worked). I would adjust values slightly and see how it changed the image to get a sense of how to make the zooms myself.
# Sources are atop the codes for images that use them.

# import pillow library, and import image and image filters.
from PIL import Image, ImageFilter
import colorsys
import math
# initialize x and y maxes and mins
xa = 0
xb = 0
ya = 0
yb = 0
# user input on image size
while True:
	try:
		imgx = int(input("What width would you like the following three images to have? "))
		imgy = int(input("What height would you like the following three images to have? "))
		break
	except ValueError:
		print("That's not a number. Try again.")

# create first image
image = Image.new("RGB", (imgx,imgy))

# My first mandelbrot set image implements the use of hsv and multiplication to create an image that has simultaneously a lot of color and noise yet a certain blending in as well. The fractal I chose to focus on was a zoomed in version of a sort of "nib" on the -2.0, 2.0 mandelbrot image. This "nib" has multiple rays coming out, so I decided to focus on one particular ray exuding from a nib. I used HSV to RGB colorsys transformation to give it the largely contrasting pink and grey colors. I used multiplication in the RGB when putting pixels in order to get the drastic color differences sort of blockish pattern in the empty space around the fractal. I really love the way the colors clash against each other yet come together and sort of soften the fractals edges in a way that it is sort of hard to tell where it is, almost like a mystery search.

def mandelbrot_1():
	xa, xb = -0.5437, -0.5412
	ya, yb = 0.6137, 0.6162

	maxIt = 256 # max iteration

	for y in range(imgy):
		cy = y*(yb-ya)/(imgy-1) + ya
		for x in range(imgx):
			cx = x * (xb - xa)/(imgx-1) + xa
			# can make a complex number in python
			c = complex(cx, cy)
			z = 0
			for i in range(maxIt):
				if abs(z) >= 2.0:
					break
				z = z**2 + c
			r = (i*-ya)/200
			g = i/128
			b = (i*yb)/100
			r,g,b = colorsys.hsv_to_rgb(r,g,b)
			# this multiplication creates that pattern going towards the fractal
			image.putpixel((x,y),(int((r*5000)%256),int(g*256),int((b*1000)%256)))
	image.save("mandelbrotsol.png", "PNG")
	image.show()

mandelbrot_1()

image2 = Image.new("RGB", (imgx, imgy))
# A Mandelbrot with a Sobel filter found from code from this website: https://medium.com/@enzoftware/how-to-build-amazing-images-filters-with-python-median-filter-sobel-filter-%EF%B8%8F-%EF%B8%8F-22aeb8e2f540
# I didn't copy the code exactly, as the original makes the outlines very grayish and dark, so I tweaked the code to make it my own and have a blue gradient by changing the number the length divided by at the end and experimenting with the r, g, b coordinates entered into the gradient color. It works by showing the edges of the fractal with blue and yellow! The original code would show a gradient of gray, and at first, for a long time I changed that to a white-ish color. I thought this black and white would be a very cool juxtaposition but I realized that I should still have a pop of color in the picture. This was the result.
# The second mandelbrot image is a zoom in on one of the sort of "stars" that accompany certain "nibs" of the mandelbrot design, and it is very zoomed in. The way the code works is that it is sort of the opposite of normal coloring of the mandelbrot set as it outlines the edges of the set in color and sets what the components of the fractal imaging are in black. I really love this fractal, it could be my favorite and its use of the filter is really fun. It is very aesthetically pleasing.
def mandelbrot_2():
	xa, xb = -0.5476, -0.5468
	ya, yb = -0.5005, -0.4997

	maxIt = 256
	for y in range(imgy):
		cy = y*(yb-ya)/(imgy-1) + ya
		for x in range(imgx):
			cx = x * (xb - xa)/(imgx-1) + xa
			# can make a complex number in python
			c = complex(cx, cy)
			z = 0
			for i in range(maxIt):
				if abs(z) >= 2.0:
					break
				z = z**2 + c
			r = 255 - i
			g = i
			b = (i*10)%256
			image2.putpixel((x,y),(r,g,b))
	image2.save("image2.png", "PNG")
########################### SOBEL FILTER CODE STARTS HERE #################################
	path = "image2.png"
	img = Image.open(path)
	for x in range(1, imgx-1):  # ignore the edge pixels for simplicity (1 to width-1)
		for y in range(1, imgy-1): # ignore edge pixels for simplicity (1 to height-1)

		    # initialise Gx to 0 and Gy to 0 for every pixel
		    Gx = 0
		    Gy = 0

		    # top left pixel
		    p = img.getpixel((x-1, y-1))
		    r = p[0]
		    g = p[1]
		    b = p[2]

		    # intensity ranges from 0 to 765 (255 * 3)
		    intensity = int(r/2) + g + b

		    # accumulate the value into Gx, and Gy
		    Gx += -intensity
		    Gy += -intensity

		    # remaining left column
		    p = img.getpixel((x-1, y))
		    r = p[0]
		    g = p[1]
		    b = p[2]

		    Gx += -2 * (r + g + b)

		    p = img.getpixel((x-1, y+1))
		    r = p[0]
		    g = p[1]
		    b = p[2]

		    Gx += -(r + g + b)
		    Gy += (r + g + b)

		    # middle pixels
		    p = img.getpixel((x, y-1))
		    r = p[0]
		    g = p[1]
		    b = p[2]

		    Gy += -2 * (r + g + b)

		    p = img.getpixel((x, y+1))
		    r = p[0]
		    g = p[1]
		    b = p[2]

		    Gy += 2 * (r + g + b)

		    # right column
		    p = img.getpixel((x+1, y-1))
		    r = p[0]
		    g = p[1]
		    b = p[2]

		    Gx += (r + g + b)
		    Gy += -(r + g + b)

		    p = img.getpixel((x+1, y))
		    r = p[0]
		    g = p[1]
		    b = p[2]

		    Gx += 2 * (r + g + b)

		    p = img.getpixel((x+1, y+1))
		    r = p[0]
		    g = p[1]
		    b = p[2]

		    Gx += (r + g + b)
		    Gy += (r + g + b)

		    # calculate the length of the gradient (Pythagorean theorem)
		    length = math.sqrt((Gx * Gx) + (Gy * Gy))

		    # normalise the length of gradient to the range 0 to 255
		    length = length / 1000 * 255

		    length = int(length)

		    # draw the length in the edge image
		    #newpixel = img.putpixel((length,length,length))
		    image2.putpixel((x,y),(length,length,(length*10)%256))
	image2.show()
	image2.save("image2.png", "PNG")

mandelbrot_2()
image3 = Image.new("RGB", (imgx, imgy))

# https://en.wikipedia.org/wiki/Julia_set
# Wikipedia was used to get some good complex c coordinates to generate a nice image.
# My Julia set image looks at a small cluster of "pixels" outside of the main two clusters in the full screen version of the set. I used HSV and a filter, both, to create this image. First, I used HSV and multiplication to garner the color scheme I wanted as well as use the SMOOTH filter to smooth out the edges. It reminds me of watercolor paint, which is very soothing. Instead of the sharp contrast between edges with multiplication like in image 1 mandelbrot, I used smooth to create an opposition to that image. That is why I think all the images I created really go together.

def julia_1():
	xa, xb = -0.062, -0.042
	ya, yb = -0.18, -0.16

	maxIt = 256 # max iteration
	c = complex(-0.4, 0.6)
	for y in range(imgy):
		zy = y*(yb-ya)/(imgy-1) + ya
		for x in range(imgx):
			zx = x * (xb - xa)/(imgx-1) + xa
			# can make a complex number in python
			z = complex(zx,zy)
			for i in range(maxIt):
				if abs(z) >= 2.0:
					break
				z = z**2 + c
			r = (i/512)**2
			g = (i*zy)/128
			b = i/500
			r,g,b = colorsys.hsv_to_rgb(r,g,b)
			image3.putpixel((x,y),(int((r*1000)%256),int(g*256),int((b*2000)%256)))
	image3.filter(ImageFilter.SMOOTH).save("image3.png", "PNG")
	image3.filter(ImageFilter.SMOOTH).show()

julia_1()

image4 = Image.new("RGB", (imgx, imgy))

# I had created this earlier but did not think the zoom was enough, even though I loved the look of two galaxies colliding together. In this, I just used HSV to try to make the "stars" or hearts of the galaxies bright and different colors, depending on where in the image they were (depending on zx or zy). I really love this image and wanted to include it in the end even if the zoom was a little far because it reminds me of the starry night.

def julia_2():
	xa, xb = -0.5, 0.5
	ya, yb = -0.5, 0.5

	maxIt = 256
	c = complex(-0.4, 0.6)
	for y in range(imgy):
		zy = y*(yb-ya)/(imgy-1) + ya
		for x in range(imgx):
			zx = x * (xb - xa)/(imgx-1) + xa
			# can make a complex number in python
			z = complex(zx,zy)
			for i in range(maxIt):
				if abs(z) >= 2.0:
					break
				z = z**2 + c
			r = ((i*zx)/512) ** 0.5
			g = (i*zy)/300
			b = i/300
			r,g,b = colorsys.hsv_to_rgb(r,g,b)
			image4.putpixel((x,y),(int(r*256),int(g*256),int(b*256)))
	image4.save("image4.png", "PNG")
	image4.show()

julia_2()