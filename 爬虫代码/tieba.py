# 爬取中原工学院贴吧的每一页


import urllib.request
import urllib.parse
import os
i = int(input('请输入你要爬取的页数：'))
url = 'http://tieba.baidu.com/f?'
# 判断文件是否存在，防止出现文件已经存在的情况
if not os.path.exists('D:/good'):
    os.mkdir('D:/good')
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
}
# 构造for循环，抓取贴吧的每一页
for a in range(1, i+1):
    data = {
        'kw': '中原工学院',
        'ie': 'utf-8',
        'pn': str(50 * (a - 1))
    }
    data = urllib.parse.urlencode(data)
    url_1 = url + data
    filepath = 'D:/good/' + str(a) + '.html'
    urllib.request.urlretrieve(url_1, filepath)