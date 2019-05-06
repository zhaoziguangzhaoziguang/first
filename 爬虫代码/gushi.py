# 这个是爬取古诗文网页的代码


import requests
from bs4 import BeautifulSoup
# 创建一个会话，下面所有的请求都要用s去请求
s = requests.Session()
headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'

}

# 下载验证码


def download_code():
    url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
    r = s.get(url, headers=headers)
    # print(r.text)
    soup = BeautifulSoup(r.text, 'lxml')
    # 得到图片的链接
    image_url = 'https://so.gushiwen.org' + soup.find('img', id="imgCode")['src']
    r = s.get(image_url)
    fh = open('code.png', 'wb')
    fh.write(r.content)
    fh.close()


def login():

    post_url = 'https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fus' \
               'er%2fcollect.aspx'
    homepage_url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
    r = s.get(homepage_url)
    soup = BeautifulSoup(r.text, 'lxml')
    # 这一步是为了得到V，因为这个参数是不停在变的，所以必须对其进行捕获
    V = soup.find('input', id="__VIEWSTATE")['value']
    code = input('帅哥，请输入验证码:')
    # 在写formdata时，有时要注意，不要一味地复制黏贴，其中的一些参数有时并不是固定的
    formdata = {
        '__VIEWSTATE': V,
        '__VIEWSTATEGENERATOR': 'C93BE1AE',
        'code': code,
        'denglu': '登录',
        'email': '975836442@qq.com',
        'from': 'http://so.gushiwen.org/user/collect.aspx',
        'pwd': 'zzg123456789'

    }
    r = s.post(post_url, headers=headers, data=formdata)
    fh = open('gushi.txt', 'w', encoding='utf=8')
    fh.write(r.text)
    fh.close()


def main():
    # 下载验证码到本地
    download_code()
    # 发送post请求
    login()


if __name__ == '__main__':
    main()
