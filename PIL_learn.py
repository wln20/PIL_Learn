# Author: wln
# Date: 2022/8/8
from PIL import Image
import os

# 创建Image对象

# 通过打开图片文件创建
im = Image.open('Test_img.jpeg') 
im2 = Image.open('Test_img2.jpeg')
# 直接创建，指定模式、大小、颜色（缺省为黑色） 
im3 = Image.new(mode='RGB',size=(200,100),color='red')

im3.show()   # 显示图片对象
os.system("pause")

# Image对象的基本属性

# 图片长/宽/大小（以像素计）
print("width=%s\nheight=%s\nsize=%s"%(im.width,im.height,im.size))  

# format（图片格式，如.jpg）、readonly（是否只读，0为只读）、info（图片相关信息：dpi和截图软件等）、图片模式（mode）
print("format:%s\nreadonly:%s\ninfo:%s\nmode:%s"%(im.format,im.readonly,im.info,im.mode))


# 图片模式转换、格式转换/保存

# 图片模式转换，只需关心转化成的mode
im_png = im.convert(mode='RGBA')
im2_png = im2.convert(mode='RGBA')
# 保存图片
im_png.save('Test_img_PNG.png')
im2_png.save('Test_img2_PNG.png')

# 图像缩放操作
im_resize = im.resize(size=(800,100),box=(10,10,666,333))
im_resize.show()
os.system("pause")

# 创建缩略图（thumbnail image）'
im_png.thumbnail((150,50))  #改变原图
im_png.show()
im_png = im.convert(mode='RGBA')    #改回原来的
os.system("pause")

# 图像（颜色的）分离与合并

# 颜色通道分离，以三通道RGB为例，产生三个Image对象（都是灰度图，各像素灰度为该像素处此颜色通道的值大小）
im_r,im_g,im_b = im.split()
im_r.show()
os.system("pause")
im_g.show()
os.system("pause")
im_b.show()
os.system("pause")

# 图像合并，也即把同一张图/多张图分离出来的各个颜色通道，重新输入到一张图的RGB通道中
# merge方法（一般用于RGB）
im2 = im2.resize(im.size)   #两图片的大小、格式必须完全一致
im_r,im_g,im_b = im.split() #分离两张图的各颜色通道
im2_r,im2_g,im2_b = im2.split()
im12_merge = Image.merge(mode='RGB',bands=[im2_r,im_g,im2_b])
im12_merge.show()
os.system("pause")
# blend方法（用于RGBA，PNG格式）
im2_png = im2_png.resize(im_png.size)
im12_blend = Image.blend(im_png,im2_png,alpha=0.5)
im12_blend.show()
os.system("pause")

# 图像裁剪、复制、粘贴

# 剪裁
im_crop = im.crop((10,10,666,333))
im_crop.show()
os.system("pause")
# 复制、粘贴
im_copy = im.copy()
im_mask = Image.new('L',(666-10,333-10),200) #200为灰度值,越大则粘贴图越明显
im_copy.paste(im_crop,box=(10+100,10+100,666+100,333+100),mask=im_mask)
im_copy.show()
os.system("pause")

# 图像的几何变换

# 翻转
im_transpose = im.transpose(method=Image.FLIP_LEFT_RIGHT)
im_transpose.show()
os.system("pause")

# 旋转
im_rotate = im.rotate(angle=45,expand=True,fillcolor='blue')
im_rotate.show()
os.system("pause")

# 图像变换
im_transform = im.transform(size=(500,500),method=Image.EXTENT,data=[0,0,30 + im.width//4,im.height//3])
im_transform.show()
os.system("pause")

# 图像降噪
from PIL import ImageFilter

# 模糊处理
im_blur = im.filter(ImageFilter.BLUR)
im_blur.show()
os.system("pause")

# 轮廓图
im_contour = im.filter(ImageFilter.CONTOUR)
im_contour.show()
os.system("pause")

# 边缘检测
im_edge = im.filter(ImageFilter.FIND_EDGES)
im_edge.show()
os.system("pause")

# 浮雕图
im_emboss = im.filter(ImageFilter.EMBOSS)
im_emboss.show()
os.system("pause")

# 平滑图
im_smooth = im.filter(ImageFilter.SMOOTH)
im_smooth.show()
os.system("pause")


