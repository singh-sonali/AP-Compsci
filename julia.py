from PIL import Image
from PIL import ImageFilter
import random 
import colorsys
#Image 1 Area Space
xa = -.5432423423
xb = 1.5 + xa
ya = -.74324232342
yb = 1.5 + ya
#Max Iterations of Image 1
maxIt = 256
#Dimensions of images
imgx = 512
imgy = 512

def Julia():
    c = complex(-0.5831868776269598,-0.4827115744172533)
    colorgreen = Image.new("RGB", (imgx, imgy))
    colorred = Image.new("RGB", (imgx, imgy))
    for y in range(imgy):
        zy = y * (yb - ya) / (imgy - 1) + ya
        for x in range(imgx):
            zx = x * (xb - xa) / (imgx - 1) + xa
            z = complex(zx, zy)
            for i in range(maxIt):
                if abs(z) > 2.0: 
                    break 
                z = z * z + c
            r = i * 5 % 256
            g = i * 15 % 256
            b = i * 16 % 256
#Tried seeing what would happen if I didn't put three arguments in for color, and the result was extremely cool.
            colorgreen.putpixel((x, y), r*1027 + g%332 * b+ i)
            colorred.putpixel((x, y), r*10 + g%10 * b+ i)
    colorgreen.rotate(90).show()
    colorred.show()
#pasting images in their locations (based on name)

def Hello():
    print("hello")

Julia()
