# *_* coding : UTF-8 *_*
# 开发团队 ： 无
# 开发人员 ： 归零叔
# 开发时间 ： 2020/9/8 18:29
# 文件名称 : yuanjisong2.py
# 开发工具 : PyCharm
"""
猿急送爬虫单子数据
"""
import random

import requests
from lxml import etree
import redis
import re
from hashlib import md5
import sys
from fake_useragent import UserAgent
from threading import Thread,Lock
from queue import Queue
import time

class MzbSpider:
    def __init__(self):
        self.url = 'https://www.yuanjisong.com/job/allcity/page{}'
        self.headers = {
            'Cookie':'HMACCOUNT_BFESS=0A354F2E1B912620; BDUSS_BFESS=TdERTNlUU1mU2wzdH5NSVdMc0t2SjVmY0FYN1BpaWVhdE54OE9HSjhLMzBWSHRmRUFBQUFBJCQAAAAAAAAAAAEAAACwBAwGMTUxNTgxNwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPTHU1~0x1Nfe'
            ,'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
        # self.r = redis.Redis(host='127.0.0.1', port=6379, db=0)
        self.item_list=[]
        #2个队列、2把锁
        self.one_q = Queue()
        self.two_q = Queue()
        self.lock1 = Lock()
        self.lock2 = Lock()
        # 计数
        self.count = 0

    def get_html(self, url):
        """功能函数1 - 请求"""
        headers = {'User-Agent': UserAgent().random}
        html = requests.get(url=url, headers=self.headers).text
        return html

    def url_in(self):
        for index in range(1, 306):
            one_url = self.url.format(index)
            # URL地址入一级队列
            self.one_q.put(one_url)

    def md5_url(self, url):
        """功能函数：生成请求指纹"""
        s = md5()
        s.update(url.encode())

        return s.hexdigest()




    def xpath_func(self, html, xpath_bds):
        """功能函数2 - xpath解析"""
        p = etree.HTML(html)
        r_list = p.xpath(xpath_bds)

        return r_list


    def parse_one_html(self):
        while True:
            # 加锁
            self.lock1.acquire()
            if not self.one_q.empty():
                one_url = self.one_q.get()
                # 释放锁
                self.lock1.release()
                one_html = self.get_html(url=one_url)
                one_xpath='//*[@id="db_adapt_id"]'
                href_list = self.xpath_func(html=one_html, xpath_bds=one_xpath)
                for item in href_list:
                    href_list=item.xpath('.//div[@class="weui_panel weui_panel_access weui_panel_access_adapt db_adapt margin-top-2 "]/a/@href')
                for item in href_list:
                    # 拼接每个职位详情页链接,交给二级队列
                    two_url=item
                    self.two_q.put(two_url)
            else:
                self.lock1.release()
                break




    def parse_two_page(self):
        """二级页面线程事件函数: 获取每个职位的具体信息"""
        while True:
            try:
                two_url = self.two_q.get(block=True, timeout=2)
                # 生成指纹,来判断是否需要继续抓取此职位
                finger = self.md5_url(url=two_url)
                # if self.r.sadd('tencent:spider', finger) == 1:
                two_html = self.get_html(url=two_url)
                two_xpath = '/html/body/div[2]/div[@class="left_main detail_main"]'
                # tr_list: [<element tr at xxx>, <element tr at xxx>, <element tr at xxx>, ...]
                tr_list = self.xpath_func(html=two_html, xpath_bds=two_xpath)
                item={}
                for div in tr_list:
                    item['链接']=two_url
                    item['title']=div.xpath('.//div[@class="cv-title"]/h2/text()')[0].strip()
                    item['合作方式']=div.xpath('.//div/ul/li[2]/text()')[0].strip()
                    item['预估日薪']=div.xpath('.//div/ul/li[2]/text()')[1].strip()
                    item['预估总价']=div.xpath('.//div/ul/li[2]/text()')[2].strip()
                    item['预估工时']=div.xpath('.//div/ul/li[2]/text()')[3].strip()
                    item['所在区域']=div.xpath('.//div/ul/li[2]/text()')[4].strip()
                    item['需求描述']=div.xpath('.//div[@class="mobmid"]/div/p/text()')[0].strip()
                    item['状态']=div.xpath(".//div[@class='mainleft ']/div[@class='weui_panel_bd appoint_div margin_top_7']/a/text()")

                    self.item_list.append(item)
                    print(item)







                # 加锁、释放锁
                self.lock2.acquire()
                self.count += 1
                self.lock2.release()
                random.uniform(0,1)

            except Exception as e:
                print(e)
                break

    def save_data(self,list_item):
        lst_item = []
        lst2_item = []
        for i in range(len(list_item)):
            lst = list(list_item[i])
            lst2 = list(list_item[i].values())
            lst_item.append(lst)
            lst2_item.append(lst2)
        import xlwt
        work_book = xlwt.Workbook(encoding='utf-8')
        sheet = work_book.add_sheet('爬虫表')
        for i in range(len(lst_item[0])):
            sheet.write(0, i, lst_item[0][i])

        for i in range(len(lst2_item)):
            for j in range(len(lst2_item[0])):
                sheet.write(i + 1, j, lst2_item[i][j])

        work_book.save('Excel爬虫最终测试.xls')
    def run(self):
        """程序入口函数"""
        self.url_in()
        t1_list = []
        t2_list = []
        for i in range(3):
            t1 = Thread(target=self.parse_one_html)
            t1_list.append(t1)
            t1.start()

        for j in range(3):
            t2 = Thread(target=self.parse_two_page)
            t2_list.append(t2)
            t2.start()

        for t in t1_list:
            t.join()

        for t in t2_list:
            t.join()
        self.save_data(self.item_list)


        print('job number:', self.count)

if __name__ == '__main__':
    start_time = time.time()
    spider = MzbSpider()
    spider.run()
    end_time = time.time()
    print('time:%.2f' % (end_time-start_time))















