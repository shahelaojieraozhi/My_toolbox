import os
import numpy as np
from PIL import Image

im = Image.open('./p_1.png')
im.show()
width = im.size[0]  # 获取宽度
height = im.size[1]  # 获取长度

for x in range(width):
    for y in range(height):
        r, g, b, a = im.getpixel((x, y))
        rgb = (r, g, b)
        if (r == 0 and g == 102 and b == 204):
            r = g = b = 0

im.show()
im.save('P_2.png')

