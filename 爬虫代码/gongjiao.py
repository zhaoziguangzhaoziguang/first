# 爬取郑州公交信息


import requests
import lxml.html
etree = lxml.html.etree
# 列表用来保存所有的线路信息
items = []
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110'
              ' Safari/537.36'
}
def parse_navigation():
    url = 'https://zhengzhou.8684.cn/'
    r = requests.get(url, headers=headers)
    # 解析内容，获取所有的导航链接
    tree = etree.HTML(r.text)
    # 查找以数字开头的所有链接
    number_href_list = tree.xpath('//div[@class="bus_kt_r1"]//a//@href')
    # 查找以字母开头的所有链接
    char_href_list = tree.xpath('//div[@class="bus_kt_r2"]//a//@href')
    # 将需要爬取的所有链接返回
    return number_href_list + char_href_list
def parse_sanji_route(content):

    tree = etree.HTML(content)
    # 获取公交线路信息
    bus_number = tree.xpath('//div[@class="bus_i_t1"]//h1//text()')
    # 获取运行时间
    run_time = tree.xpath('//div[@class="bus_i_content"]//p[@class="bus_i_t4"]//text()')[0]
    # print(run_time)
    # 获取票价信息
    ticket_info = tree.xpath('//div[@class="bus_i_content"]//p[@class="bus_i_t4"]//text()')[1]
    try:
        # 获取更新时间
        gxsj = tree.xpath('//div[@class="bus_i_content"]//p[@class="bus_i_t4"]//text()')[4]
    except Exception as e:
        gxsj = tree.xpath('//div[@class="bus_i_content"]//p[@class="bus_i_t4"]//text()')[3]
    # 获取上行总站数
    up_total = tree.xpath('//span[@class="bus_line_no"]/text()')[0]
    # 获取上行所有站名
    up_site_list = tree.xpath('//div[@class="bus_line_site "][1]/div/div/a/text()')  # 特别注意这个表达式，源码中有个空格键
    try:
        # 获取下行总站数
        down_total = tree.xpath('//span[@class="bus_line_no"]/text()')[1]
        # 获取下行所有站名
        down_site_list = tree.xpath('//div[@class="bus_line_site "][2]/div/div/a/text()')
        # 将每一条公交的线路信息存到字典中
    except Exception as e:
        down_total = ''
        down_site_list = []
    item = {
        '线路名': bus_number,
        '运行时间': run_time,
        '票价信息': ticket_info,
        '更新时间': gxsj,
        '上行站数': up_total,
        '上行站点': up_site_list,
        '下行站数': down_total,
        '下行站点': down_site_list,
    }
    items.append(item)
    # print(up_total)
    # '//div[@class="bus_site_layer"]//div[@class]//a//text()'
def parse_erji_route(content):
    tree = etree.HTML(content)
    # 写xpath，获取每一个线路
    route_list = tree.xpath('//div[@id="con_site_1"]//@href')
    # 写xpath，获取公交车的名字
    route_name = tree.xpath('//div[@id="con_site_1"]/a/text()')
    # 遍历上面这个列表
    i = 0
    for route in route_list:
        print('开始爬取%s公交信息' % route_name[i])
        route = 'https://zhengzhou.8684.cn' + route
        r = requests.get(route, headers=headers)
        # 解析内容，获取每一路公交的详细信息
        parse_sanji_route(r.text)
        print('结束爬取%s公交信息' % route_name[i])
        i = i+1





def parse_erji(navi_list):
    # 遍历上面的列表，依次发送请求，解析内容，获取每一个页面所有公交路线的url
    for first_url in navi_list:
        first_url = 'https://zhengzhou.8684.cn' + first_url
        print('开始爬取所有的公交信息%s' % first_url)
        r = requests.get(first_url, headers=headers)
        # 解析内容，获取每一路公交的详细url
        parse_erji_route(r.text)
        print('结束爬取所有的公交信息%s' % first_url)
def main():
    # 爬取第一页的所有导航链接
    navi_list = parse_navigation()
    # 爬取二级页面，需要找到以1开头的所有公交路线
    parse_erji(navi_list)
    # 爬取完毕
    fh = open('郑州公交.txt', 'w', encoding='utf-8')
    for item in items:
        fh.write(str(item) + '\n')
    fh.close()


if __name__ == '__main__':
    main()
