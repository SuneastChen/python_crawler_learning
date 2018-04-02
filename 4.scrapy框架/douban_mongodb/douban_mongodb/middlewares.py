# -*- coding: utf-8 -*-
import random
from douban_mongodb.settings import USER_AGENTS,PROXY
import base64

class RandomUserAgent(object):
    def process_request(self,request,spider):
        useragent = random.choice(USER_AGENTS)
        request.headers.setdefault('User-Agent', useragent)


class Proxy(object):
    def process_request(self,request,spider):
        #先对账户密码进行base64编码
        userpasswd_base64 = base64.b64encode(PROXY['user_passwd'].encode('utf-8'))
        #再把编码后的账户密码数据加入到headers中
        request.headers['Proxy-Authorization'] = 'Basic ' + str(userpasswd_base64)[2:-1]
        #把代理ip加入到meta属性中
        request.meta['proxy'] = PROXY['ip_port']


