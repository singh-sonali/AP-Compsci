from PIL import Image
from PIL import ImageFilter
import math
import random 

#This method draws an image created by a zoom on a specific area of the Julia set.
def Julia():
    #Image Area Space. xa and ya were found as zoom coordinates by experimentation. xb and yb are defined in terms of xa and xb respectively to ensure equal distances between x and y coordinates. 
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

    #Begin modified Julia set code. First lines are simply the scaling of the drawing area to the image size.
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

            #Simple mod for colors. More complex use of variables is then implemented when coloring pixels.
            greenr = i * 5 % 256
            greeng = i * 15 % 256
            greenbb = i * 16 % 256
            print(r,g,b)

            greenimage.putpixel((x, y), greenr*1027 + greeng%332 * greenb+ i)

            #Rotated green image 90 degrees for effect. Both green and red images are immediately shown upon running code instead of saved.
    greenimage.rotate(90).show()
    #Experimenting with more complex ways to input RGB values. Discovered that avoiding a RGB tuple, and instead modifying r,g,b values in one expression produced exciting colors. Presume that PIL accepts a single value as a monochrome color. Both a green image, and red image of the same design and zoom are produced using algorithms.
            #greenimage.putpixel((x, y), r*1027 + g%332 * b+ i)
            redimage.putpixel((x, y), r*10 + g%10 * b+ i)

    #Rotated green image 90 degrees for effect. Both green and red images are immediately shown upon running code instead of saved.
    greenimage.rotate(90).show()
    redimage.show()

Julia()
