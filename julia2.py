from PIL import Image
from PIL import ImageFilter
import colorsys as col
import random
# drawing area (xa < xb and ya < yb)
Txa = -0.95
Txb = 2 + Txa
Tya = -1
Tyb = 2 + Tya
TmaxIt = 256 # iterations
# image size
imgx = 512
imgy = 512
topimage = Image.new("RGB", (imgx, imgy))
# Julia set to draw
Tc = complex(-0.780987977374866,-0.18958326731498987)

print(Tc)

for y in range(imgy):
    Tzy = y * (Tyb - Tya) / (imgy - 1)  + Tya
    for x in range(imgx):
        Tzx = x * (Txb - Txa) / (imgx - 1) + Txa
        Tz = complex(Tzx, Tzy)
        for i in range(TmaxIt):
            if abs(Tz) >= 2.0: 
                break 
            Tz = Tz **5 + Tc 
        hT,sT,vT = i/512, (i*2)/256, (i*2)/64
        rT,gT,bT = col.hsv_to_rgb(hT,sT,vT)

        rT = int(rT*255)
        gT = int(gT*255)
        bT = int(bT*255)
        print(rT,gT,2)
        topimage.putpixel((x,y),((rT*200)%256,(gT*320)%256,(bT*100)%256))
        # r = i % 5 * 51
        # g = i % 15 * 17
        # b = i % 16 * 16
        # image.putpixel((x, y), (r,g,b))

topimage.show()