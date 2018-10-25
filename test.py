#Importing the modules from PIL that allow the creation of a picture, as well as some pre-specified image filters.
from PIL import Image
from PIL import ImageFilter
#The colorsys module enables conversions between types of color sets.
import colorsys as col
import random

#This method draws a swirly, bright picture.
def psychedelic_image():
#These are the drawing area dimensions. xb and yb are defined in terms of xa and ya to ensure that the distance between x coordinates and y coordinate can remain the same without doing math. 
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

    #Begin modified Julia set code. First lines are simply the scaling of the drawing area to the image size.
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

psychedelic_image()