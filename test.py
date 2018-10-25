from PIL import Image
from PIL import ImageFilter
import colorsys as col
import random
# drawing area (xa < xb and ya < yb)
xa = -0.65
xb = 0.3 + xa
ya = -0.58
yb = 0.3 + ya
maxIt = 256 # iterations
# image size
imgx = 512
imgy = 512
image = Image.new("RGB", (imgx, imgy))
# Julia set to draw
c = complex(-0.6528756059172145,-0.4888112766214806)
print(c)

for y in range(imgy):
    zy = y * (yb - ya) / (imgy - 1)  + ya
    for x in range(imgx):
        zx = x * (xb - xa) / (imgx - 1) + xa
        z = complex(zx, zy)
        for i in range(maxIt):
            if abs(z) >= 2.0: 
                break 
            z = z **5 + c 
        h,s,v = i/512, (i*-ya)/256, (i*yb)/64
        r,g,b = col.hsv_to_rgb(h,s,v)

        r = int(r*255)
        g = int(g*255)
        b = int(b*255)
        image.putpixel((x,y),((r*200)%256,(g*320)%256,(b*100)%256))
image = image.filter(ImageFilter.DETAIL)
image.show()