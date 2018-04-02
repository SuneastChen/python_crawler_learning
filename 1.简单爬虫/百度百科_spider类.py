#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: xinlan time:2017/09/23
import requests
import re
# 定义一个爬虫类

class Spider:
    def __init__(self):
        # 已爬取url集合，去从
        self.crawled_urls = set([])
        # 待爬取url
        self.not_crawl_urls = set([])
        # 下载器
        headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E) '}
        self.session = requests.Session()
        self.session.headers.update(headers)

    # 下载方法
    def download(self, url):
        try:
            return self.session.get(url)
        except Exception as e:
            print(e)
            return None

    # 解析
    def parse(self, html):
        # 获取所有词条的url
        urls = re.findall(r'(/item/.*?)"', html)
        # url补全
        return ["https://baike.baidu.com%s" % x for x in urls]

    # 输出
    def out(self, html, path):
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)

    # 执行
    def run(self, start_url):
        # 将start_url 放入待爬取url集合
        self.not_crawl_urls.add(start_url)
        i = 1
        while len(self.not_crawl_urls) > 0:
            # 没有检测是否已爬取
            # 作业
            # 获取一条待爬取url
            crawling_url = self.not_crawl_urls.pop()
            # 下载
            response = self.download(crawling_url)
            if response:
                response.encoding = 'utf-8'
                # 分析获取字条urls
                new_urls = self.parse(response.text)
                self.not_crawl_urls.update(new_urls)
                self.out(response.text, "%d.html" % i)
                # 将爬完的url放入已爬取
                self.crawled_urls.add(crawling_url)
                print('download %d page' % i)
                i += 1
                if i > 100:
                    break


if __name__ == '__main__':
    spider = Spider()
    start_url = "https://baike.baidu.com/item/Python/407313"
    spider.run(start_url)