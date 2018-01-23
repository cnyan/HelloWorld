# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       yan
   date：          18-1-23
-------------------------------------------------
   Change Activity:  18-1-23:
-------------------------------------------------
"""

'pillow_image'

__author__ = '闫继龙'

#图像缩放

from PIL import Image

with Image.open('../src/image/cat.jpg') as im:
    # 获得图像尺寸:
    w,h = im.size
    print('Original image size: %sx%s' % (w, h))

    # 缩放到50%:
    im.thumbnail((w // 2, h // 2))
    print('Resize image to: %sx%s' % (w // 2, h // 2))

    # 把缩放后的图像用jpeg格式保存:
    #im.save('../src/image/recat.jpg', 'jpeg')

#图片模糊
from PIL import Image,ImageFilter
with Image.open('../src/image/rain.jpg') as im:
    # 应用模糊滤镜:
    im2 = im.filter(ImageFilter.BLUR)
    im3 = im.filter(ImageFilter.MinFilter(4))
    im4 = im.filter(ImageFilter.MinFilter)

    im2.save('../src/image/rerain2.jpg', 'jpeg')
    im3.save('../src/image/rerain3.jpg', 'jpeg')
    im4.save('../src/image/rerain4.jpg', 'jpeg')