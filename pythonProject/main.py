# 先导入要用的一堆工具
from urllib import request
import json
from urllib import parse
import os, win32gui, win32con, win32api
import datetime

a = 0;
b = input("你想下载几天前的壁纸？")
a = int(b)

os.chdir('BingPictures')
datetoday = datetime.date.today()

date = str(int(datetoday.strftime('20%y%m%d')) - a);

print(datetoday.strftime("今天是20%y年%m月%d日"))
if a != 0:
    print('正在下载' + str(a) + '天前的壁纸')
# 运行时间有点久就让操作者等待
print('壁纸下载中，请稍候。。。。。')

# 先找到必应每日一图对应的js文件的网址
sourceWebsite = request.urlopen('https://www.bing.com/HPImageArchive.aspx?format=js&idx=' + str(a) + '&n=1')
obj = json.load(sourceWebsite)

# 在文件信息里打印出'copyright',即版权信息中包含的图片名字
if a == 0:
    print('今天的图片是：')
    print(obj['images'][0]['copyright'])
else:
    print(str(a) + '天前的图片是：')
    print(obj['images'][0]['copyright'])

# (obj['images'][0]['urlbase'])提取每日的照片的网址部分使用
photoURL = 'http://www.bing.com' + (obj['images'][0]['urlbase']) + '_1920x1080.jpg'
f = open('./wallpaper.jpg', 'wb')
picture = request.urlopen(photoURL)
f.write(picture.read())
f.close()

# 提取js中的'copyrightlink'项(地名)
nameurl = obj['images'][0]['copyrightlink']

# 去头去尾，只剩下汉字搜索对应的url的字码
photoname = nameurl.replace('https://www.bing.com/search?q=', '')
photoname = photoname.replace('&form=hpcapt&mkt=zh-cn', '')
# 把url字码解码，转回原来汉字
photoname = parse.unquote(photoname)
print(photoname)
os.rename('wallpaper.jpg',date + photoname + '.jpg')