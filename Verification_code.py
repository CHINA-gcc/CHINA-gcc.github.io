"""
>> 通道
- 每张图片都是由一个或多个数据通道构成.
- RGB图像 --每张图片都是由三个数据通道叠加构成(R、G、B)
- PNG图像 --RGBA 四个通道(A 代表透明度)
- 灰度图像只有一个通道(RGB色彩分量全部相等)
- 灰度指黑白图像中点的颜色深度,范围一般是 0-255(白色为255, 黑色为0)

>> 灰度化
- 像素点是最小的图片单元, 一个像素点的颜色由RGB三个值来表现. 一个像素点对应三个颜色向量矩阵.
- 图片的灰度化是让像素点矩阵中每一个像素点满足 R=G=B, 此时的值叫做灰度值.
- 灰度转化公式：R=G=B=处理前的 Rx0.3 + Gx0.59 + Bx0.11.

>> 二值化
- 图像的二值化是将图像的像素点矩阵中的每个像素点的灰度值设置为0或255.
- 二值化原理是利用设定的一个阈值来判断图像像素(一般小于阈值的像素点变为0, 大于的变成255.)
- 临界灰度值被称为阈值, 选择原则为既要尽可能保存图片信息, 又要尽可能减少背景和噪声的干扰.
- 阈值选择的方法:灰度平均值法: 取127(0-255的中数)
- 平均值法: 计算像素点矩阵中的所有像素点的灰度值的平均值avg.
- 迭代法: 选择一个近似阈值作为估计值的初始值, 然后进行分割图像, 根据产生的子图像的特征来选取新的阈值. 再利用新的阈值分割图像, 经过多次循环, 使得错误分割的图像像素点降到最小.

>> 降噪
- 二值化处理使整个图片像素被分为了两个值 0 和 255.
- 一个点是黑色并且相邻的点为白色的点的个数大于一个固定的值, 这个点就是噪点.
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from pwd import bili_user, bili_pwd
from PIL import Image


# from common_utils import UtilsFunction


class VerifyCode(UtilsFunction):

    def usage_contents(self):
        if self.str_choice == "字符验证码":
            self.usage_infos = """
>> 灰度化

from PIL import Image
# picture = Image.new('RGB', (200, 100), 'red')
# pic = picture.crop((100, 100, 100, 100))
picture = Image.open('...')
# print(picture.getbands())
picture.convert('L')
picture.show()

>> 二值化

def sharp(image):
    w, h = image.size
    tem = 0
    for i in range(w):
        for j in range(h):
            tem += image.getpixel((i, j))

    pixel_ave = tem/(w*h)
    for i in range(w):
        for j in range(h):
            p = image.getpixel((i, j))
            if p > pixel_ave:
                # 填充
                im.putpixel((i, j), 255)
            else:
                im.putpixel((i, j), 0)

    return image

>> 降噪
def genPointIndex(coreTuple, Range=1):
    # coreTuple(中心点坐标)
    for i in range(-Range, Range+1):
        for j in range(-Range, Range+1):
             if i ==0 and j == 0:
                continue
            x = coreTuple[0] + i
            y = coreTuple[1] + j
            yield x, y

def reduceNoise(image):
    w, h = image.size
    array = image.load()    --将图片转换为一个读写对象.
    # 去掉边缘干扰信息
    per = 0.5
    for i in range(w):
        for j in range(int(h*per)):
            array[i, j] = 255
        for j in range(int(h*(1-per)), h):
            array[i, j] = 255

    for i in range(h):
        for j in range(int(w*per)):
            array[j, i] = 255

        for j in range(int(w*(1-per)), w):
            array[j, i] = 255

    # 去掉中间噪点
    for i in range(w):
        for j in range(h):
            if image.getpixel((i, j)) < 100:    --黑点才有可能是噪点.
                count = 0
                Range = 2   # 检测范围
                for x, y in genPointIndex((i, j), Range):
                    if array[x, y] > 100:
                        count += 1

                if 
    return image
"""

class BiliLogin():
    def __init__(self):
        self.username = username
        self.password = password
        self.chrome = webdriver.Chrome()

    def username_password(self):
        self.chrome.find_element_by_id('login-username').send_keys(bili_user)
        self.chrome.find_element_by_id('login-passwd').send_keys(bili_pwd)
        self.chrome.find_element_by_css_selector('.btn-login').click()

    def get_captcha(self):
        # 隐藏滑块
        js = "document.getElementByClassName('geetest_canvas_slice')[0].style.display='None'"
        self.chrome.execute_script(js)
        # 截取缺口图
        slice_path = './slice.png'
        self.chrome.find_element_by_class_name('')[0]
        # 显示完整图


        
    def get_distance(self, slice_path, full_path):
        slice_im = Image.open(slice_path)
        full_im = Image.open(full_path)
        # slice_im = slice_im.convert('L')
        # full_im = full_im.convert('L')
        w, h = slice_im.size
        for i in range(w):
            for j in range(h):
                r = slice_im.getpixel(i, j)[0] - full_im.getpixel(i,j)[0]
                g = slice_im.getpixel(i, j)[1] - full_im.getpixel(i,j)[1]
                b = slice_im.getpixel(i, j)[2] - full_im.getpixel(i,j)[2]

    def run(self):
        self.chrome.get('https://passport.bilibili.com/login')
        self.username_password()
        self.get_captcha()