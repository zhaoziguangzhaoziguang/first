#  爬取糗事百科上面的糗图

import urllib.request
import re
import os
# 判断文件夹是否存在，如果不存在就创建一个文件夹，如果存在则不需重复创建
if not os.path.exists('D:/qiushi'):
    os.mkdir('D:/qiushi')
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
n = int(input('请输入你想爬的页数:'))
# 循环爬取每一页的图片
for i in range(1, n+1):
    url = 'https://www.qiushibaike.com/pic/page/' + str(i) + '/'
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req).read().decode()
    pat = r'<div class="thumb">.*?<img src="(.*?)".*?>.*?</div>'
    # 加上re.S可以让.*?匹配上换行符，无论有几个换行符都能匹配得上
    # 其中re.S:单行匹配，re.M:多行匹配，re.I:忽略大小写
    list_link = re.compile(pat, re.S).findall(response)
    for x in range(len(list_link)):
        filepath = 'D:/qiushi/' + str(i) + str(x) + '.jpg'
        pic_url = 'https:' + list_link[x]
        urllib.request.urlretrieve(pic_url, filename=filepath)