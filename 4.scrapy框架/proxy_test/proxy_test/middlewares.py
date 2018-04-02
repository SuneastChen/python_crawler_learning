# -*- coding: utf-8 -*-

from proxy_test.settings import PROXY
import base64

class ProxyMyIP(object):
    def process_request(self,request,spider):
        #1.先对账户密码进行base64编码
        userpasswd_base64 = base64.b64encode('1050521852:vch6gryw'.encode('utf-8'))
        #2.再把编码后的账户密码数据加入到headers中,'Basic '后面有个空格,userpasswd_base64是个字节,要转成字符串
        request.headers['Proxy-Authorization'] = 'Basic ' + str(userpasswd_base64)[2:-1]
        #3.把代理ip加入到meta属性中
        request.meta['proxy'] = PROXY['ip_port']
