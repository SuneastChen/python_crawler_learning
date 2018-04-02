
from urllib.request import HTTPPasswordMgrWithDefaultRealm as mgr
from urllib.request import ProxyBasicAuthHandler,build_opener,install_opener,Request,urlopen

user = '1050521852'
passwd = 'vch6gryw'
proxyserver = '117.48.199.230:16816'

# 构建一个密码管理器,用来保存以上信息
passwdmgr = mgr()
# 添加信息参数,第一个参数是与远程服务器相关的域信息,一般写None
passwdmgr.add_password(None,proxyserver,user,passwd)
# 创建一个ProxyBasicAuthHandler处理器对象
proxy_handler = ProxyBasicAuthHandler(passwdmgr)
#替换了之前的写法: proxy_handler = ProxyHandler({"http":"1050521852:vch6gryw@117.48.199.230:16816"})
opener=build_opener(proxy_handler)
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')] 
install_opener(opener)

url='http://www.ipdizhichaxun.com/'
req=Request(url)
response=urlopen(req)  
html=response.read().decode('utf-8')
print(html)