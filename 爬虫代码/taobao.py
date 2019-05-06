# 抓取淘宝图片

import urllib.request
import os
import re
import ssl
dir = 'D:/taobao'
# 判断该文件夹是否存在，避免每次运行出现文件夹已经存在的情况
if not os.path.exists(dir):
    os.mkdir(dir)
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
'cookie': 'miid=1069298250227251534; t=1b4cc69994c7a376ba8fd039619d7012; cna=qdp/FPgj6FoCAXWIJJxDDHre; tg=0; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; enc=5XrpK063n5EyZe7eC6qUc5zlWfUGkY%2BF57CDPMMkhMpUwLRnN3ZUeAI1e8k6QaMyjWzVmEAtm6jBbuaeAniUhA%3D%3D; _uab_collina=154996502001303451151106; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; _cc_=VFC%2FuZ9ajQ%3D%3D; mt=ci=-1_0; _m_h5_tk=45eda662bfe2ca09f3d4eff269f7c861_1551160907236; _m_h5_tk_enc=3871946a07343c70e8575b705d7f155b; v=0; cookie2=1cba80d734d934d599bc20790d7e98f6; _tb_token_=554f3b38e1434; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; JSESSIONID=4197EE73CD6704E4C43193B4E69547FC; l=bBIZJ9acvS5riKKLBOfgZuI8ax7TaCRf1sPzw4_G5IB1TjfaydrZbHwKXogwL3Q_E_5pmetrCFDR9REe8rzLRO1..; isg=BPPzoSqMq-7dL2fCZesA1aSvgvfdgIeQJV7IdaWUlJcspBRGLfrpOuH-XpTvBN_i'
}
i = int(input('请输入你要爬取的页数：'))
url = 'https://s.taobao.com/search?q=Python&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.inde' \
      'x&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=7&ntoffset=' \
      '7&p4ppushleft=1%2C48&'
# 构建for循环，爬取每一页的图片
for a in range(1, i+1):
    data = {
        's': str(44*(a-1))
    }
    data = urllib.parse.urlencode(data)
    url_1 = url + data
    req = urllib.request.Request(url_1, headers=headers)
    response = urllib.request.urlopen(req, context=ssl._create_unverified_context()).read().decode('utf-8', 'ignore')
    pat = '"pic_url":"(.*?)"' # 提取每一页源码的图片链接
    pic_url = re.compile(pat).findall(response)
    # print(len(pic_url))
    for x in range(len(pic_url)):
        url_1 = 'http:' + pic_url[x]
        pic_file = 'D:/taobao/' + str(a) + str(x) + '.jpg'
        urllib.request.urlretrieve(url_1, pic_file)