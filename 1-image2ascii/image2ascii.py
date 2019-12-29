# Author: @dourgey
# Create Time: 2019/12/27: 18:06

# 主要知识点：
# argparse的使用
# 检查文件路径是否存在
# PILLOW读取图片并处理
# 文件写入

import argparse
import os
import sys
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", help="主人要转换的图片路径喵，默认在当前路径下读取喵~")
parser.add_argument("-f", "--file", help="主人要保存的字符画文件路径喵，默认保存在当前路径下喵~")
args = parser.parse_args()

if not os.path.exists(args.image):  # 如果图片路径不存在
    print("图片路径不存在呢，粗心的主人请再次检查喵~")
    sys.exit(0)

img_path = args.image
im = Image.open(img_path)
width, height = im.size
t_height = int(height / width * 100 / 2.5)
im = im.resize((100, t_height), Image.ANTIALIAS)


def get_char(r, g, b, alpha=256):
    ascii_char = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "  # 设定映射字符
    if alpha == 0:
        return " "
    gray = (r * 38 + g * 75 + b * 15) >> 7  # RGB转灰阶参考https://www.cnblogs.com/carekee/articles/3629964.html
    return ascii_char[gray % 70]


f = open(args.file, "w")  # 新建文件写入

# 逐行逐像素转换，写入文件
for i in range(t_height):
    for j in range(100):
        r, g, b = im.getpixel((j, i))
        f.write(
            get_char(r, g, b)
        )
    f.write("\n")
f.close()

print("已经为主人处理好了喵~")



