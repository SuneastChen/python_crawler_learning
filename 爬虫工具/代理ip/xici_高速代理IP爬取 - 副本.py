
import urllib.request
import re
import requests
import threading

IP_LIST =[]

def open_url(url):
    head={}    #伪造客户端的头部信息,head在之Request对象生成之前
    head['User-Agent']='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
    req=urllib.request.Request(url,headers=head)  #Request必须用大写,得到一个Request对象
    response=urllib.request.urlopen(req)    #传入一个对象,返回一个对象
    html=response.read().decode('utf-8')     #转成utf-8可认识的信息
    return html

def get_ip(html):
    ip_port_list=[]   # 一页的ip_port_list
    p = re.compile(r'<td class="country"><img.+?秒',re.S) 
    td_list=p.findall(html)
    for td in td_list:
        ip_type = re.search(r'<td>(HTTPS?)</td>',td).group(1)
        speed = re.search(r'<div title="(\d+[.]\d+)秒',td).group(1)
        if float(speed)<1.5 and ip_type=='HTTP':
            p = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>\s+?<td>(\d{1,4})')
            ip_port = p.search(td).group(1)+':'+p.search(td).group(2)
            ip_port_list.append(ip_port)
    IP_LIST.append(ip_port_list)


def get_ips(page):
    for page_url in ['http://www.xicidaili.com/nn/{}'.format(i) for i in range(1,page)]:
        get_ip(open_url(page_url))
    print(len(IP_LIST))
    return IP_LIST


def test_ip(ip_port):
        url='http://httpbin.org/ip'
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}
        try:
            res = requests.get(url,proxies={'http': ip_port},headers=headers,timeout=5)
            print(res.status_code)
        except:
            return False
        print(ip_port)   # 有返回值的ip,但不一定是真的,再判断
        if res.text.find('"origin":') != -1:
            global IP_LIST
            IP_LIST.append(ip_port)



if __name__=='__main__':
    my_thread = []
    for ip_port in get_ips(3):
        t=threading.Thread(target=test_ip,args=[ip_port])
        while 1:    #进入判断循环
            if threading.activeCount()<=11:   
                #只有当前的激活线程小于6(包括主线程),才会开始
                t.start()
                # print('测试线程开始...')
                break
        my_thread.append(t)
    for t in my_thread:  # 也可设置为有责任心的老板
        t.join()
    print('主线程结束')
    print(IP_LIST)

