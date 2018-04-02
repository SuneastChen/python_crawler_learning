import random
from urllib.request import ProxyHandler,build_opener,install_opener,urlopen,Request


# 1.参数是一个字典
proxy_handler = ProxyHandler({"http":"1050521852:vch6gryw@117.48.199.230:16816"})
# 2.定制,创建一个opener
opener=build_opener(proxy_handler)
# 加入头信息,需要用元组的列表
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')] 


# 3.调用opener.open()方法打开url,从局部打开
#opener.open(req)
# 3.安装一个全局的opener,安装后,urlopen()方法默认会用此opener打开网页
install_opener(opener)


url='http://www.ipdizhichaxun.com/'
req=Request(url)
response=urlopen(req)  
html=response.read().decode('utf-8')
print(html)