# -*- coding: utf-8 -*-
import scrapy
import chardet

class Logren1Spider(scrapy.Spider):
    name = 'logren1'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/842465956/profile',]
    cookies = {"anonymid": "j991lsb5-55alqs","_r01_": "1","springskin": "set","wp": "0","jebe_key": "8e13a665-5079-4c3c-8772-b432f7956fe7%7C2183573fa959e5a988bbddad92a81ca0%7C1509057935309%7C1%7C1509061846457","jebe_key": "8e13a665-5079-4c3c-8772-b432f7956fe7%7C2183573fa959e5a988bbddad92a81ca0%7C1509057935309%7C1%7C1509181965502","depovince": "GW","jebecookies": "dc507fb1-cc13-4260-bd11-c0a70ca5d0ce|||||","ick_login": "fcb19f23-f694-4e1d-8df7-22b5d6a6e431","_de": "280B7DBFC68B1D9EF7F8541ED66B57EB","p": "d55902f006b4d93aa2385a130163073a3","first_login_flag": "1","ln_uact": "15161580934","ln_hurl": "http://head.xiaonei.com/photos/0/0/men_main.gif","t": "a6eda102e5139a6ca0474022449304c23","societyguester": "a6eda102e5139a6ca0474022449304c23","id": "960617323","xnsid": "754fa7c9","loginfrom": "syshome","JSESSIONID": "abcX5PDQKsFhJhvLfSk_v","ch_id": "10016"}

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.FormRequest(url, cookies=self.cookies, callback=self.parse)


    def parse(self, response):
        print(response.url)
        print(response.status)
        print(response.text)

