#  这个爬取的网站是http://sc.chinaz.com/tupian/，爬取其中的性感美女图片
# 同样要注意爬取的思路，还有创建文件的方法也是值得注意的

import urllib.request
import urllib.parse
import lxml.html
import os
etree = lxml.html.etree


def handle_request(url, page):
    # 由于第一页和后面的页码规律不一样，所以要进行判断
    if page == 1:
        url = url.format('')
    else:
        url = url.format('_' + str(page))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/70.0.3538.110 Safari/537.36'
    }
    request = urllib.request.Request(url, headers=headers)
    return request


def parse_content(content):
    tree = etree.HTML(content)
    image_list = tree.xpath('//div[@id="container"]/div/div/a/img/@src2')
    # 遍历列表，依次加载
    for image_src in image_list:
        download_image(image_src)


def download_image(image_src):
    dirpath = 'xinggan'
    # 创建一个文件夹
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    # 搞个文件名
    filename = os.path.basename(image_src)  # 要注意这种写法
    # 搞图片路径
    filepath = os.path.join(dirpath, filename)  # 要注意这种写法
    # 发送请求保存图片
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.'
                      '3538.110 Safari/537.36'
    }
    request = urllib.request.Request(image_src, headers=headers)
    response = urllib.request.urlopen(request).read()
    fh = open(filepath, 'wb')
    fh.write(response)
    fh.close()


def main():
    url = 'http://sc.chinaz.com/tupian/xingganmeinvtupian{}.html'
    start_page = int(input('请输入起始页码:'))
    end_page = int(input('请输入结束页码:'))
    for page in range(start_page, end_page+1):
        request = handle_request(url, page)
        content = urllib.request.urlopen(request).read().decode()
        parse_content(content)


if __name__ == '__main__':
    main()
