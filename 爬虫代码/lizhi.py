# 这个是爬取励志签名一点点的内容，爬取的思路很有参考性，还有很多知识点值得注意


import urllib.request
import re
# 这个page参数设置的非常好，这个函数有两个参数，url是必须要传的，page默认为空，可传可不传
# 在这个函数中，传与不传将执行不同的代码，所以可根据需要来进行传参


def handle_request(url, page=None):
    # 拼接出指定的url
    if page is not None:
        url = url + str(page) + '.html'
    headers = {
        'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/7'
                        '0.0.3538.110 Safari/537.36'
    }
    request = urllib.request.Request(url, headers=headers)
    return request


def get_text(a_href):
    # 调用函数构建对象
    request = handle_request(a_href)
    # 发送请求获得响应
    content = urllib.request.urlopen(request).read().decode()
    # 解析内容
    pat = r'<div class="neirong">(.*?)</div>'
    lt = re.compile(pat, re.S).findall(content)
    text = lt[0]
    # 写个正则将每篇文章里的图片去掉
    pat1 = r'<img .*?>'
    pat11 = re.compile(pat1)
    text = pat11.sub('', text)  # ''这个空字符在文档中表示的就是没有任何东西,注意这个用法，挺不错的
    return text


def parse_content(content):
    # 写正则
    pat = r'<h3>.*?<a href="(.*?)">.*?<b>(.*?)</b>.*?</a>.*?</h3>'
    # lt是一个列表，列表中的元素都是元组，元组中第一个元素就是正则中第一个小括号匹配到的内容，
    # 元组中第二个元素就是正则中第二个小括号匹配到的内容
    lt = re.compile(pat).findall(content)
    # 遍历列表
    for href_title in lt:
        # 获取内容的链接
        a_href = 'http://www.yikexun.cn' + href_title[0]
        # 获取标题
        title = href_title[1]
        # 向a_href发送请求获取响应内容
        text = get_text(a_href)
        # print(text)
        # 写入到html文件中
        string = '<h1>%s</h1>%s' % (title, text)  # 这样就能把文章和标题连在一起，以追加的方式去写文件即可
        fh = open('lizhi.html', 'a', encoding='utf8')  # 这个a表示的是以追加的方式去写到文件中
        fh.write(string)
        fh.close()


def main():
    url = 'http://www.yikexun.cn/lizhi/qianming/list_50_'
    start_page = int(input('请输入起始页码:'))
    end_page = int(input('请输入结束页码:'))
    for page in range(start_page, end_pag+1):

        # 根据url和page去生成指定的request
        request = handle_request(url, page)
        # 发送请求
        content = urllib.request.urlopen(request).read().decode()
        # 解析内容
        parse_content(content)


if __name__ == '__main__':
    main()
