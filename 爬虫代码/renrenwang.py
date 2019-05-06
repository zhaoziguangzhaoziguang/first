# 爬取人人网登陆后的首页

import urllib.request
import http.cookiejar
import urllib.parse
# 创建一个cookiejar对象
cj = http.cookiejar.CookieJar()
# 创建一个handler对象
handler = urllib.request.HTTPCookieProcessor(cj)
# 创建一个opener
opener = urllib.request.build_opener(handler)

post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019132111193 '
post_data = {
'email': '15713826124',
'icode': '',
'origURL': 'http://www.renren.com/home',
'domain': 'renren.com',
'key_id': '1',
'captcha_type':	'web_login',
'password':	'316d70b9799b8d6991dcf986d98b036cde2a646f928d39fb6b380086d45c9e19',
'rkey':	'f9473288c1c8270976ba6cb8b6297196',
'f': 'https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dxrck62vqvHPG4Sh8r-ZAUXyASA7i4WpvdFvPkRw37dm%26wd%3D%26eqid%3D9c41f5c4000d1e80000000025c76924f'
}
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'

}
post_data = urllib.parse.urlencode(post_data).encode()
req = urllib.request.Request(post_url, headers=headers)
# 在创建好opener后，所有的请求都要用opener的方式去请求
response = opener.open(req, post_data)
url = 'http://www.renren.com/969882792'
req = urllib.request.Request(url, headers=headers)
# 此时的opener中已经携带了有关的cookie信息
response = opener.open(req)
print(response.read().decode())