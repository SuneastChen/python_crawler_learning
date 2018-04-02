from urllib.request import Request,urlopen,HTTPCookieProcessor,build_opener
from urllib.parse import urlencode
from http.cookiejar import CookieJar

# 第一步:构建opener(浏览器)
cookie = CookieJar()  # 创建cookie对象,用来保存cookie的值
cookie_handler = HTTPCookieProcessor(cookie) # 构建一个cookie_handler
opener = build_opener(cookie_handler)  # 创建一个自定义的opener
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')] 

# 第二步:构建req(浏览器要打开的对象)
url = 'http://www.renren.com/PLogin.do'
data = {'email':'15161580934','password':'renren789.'}
data = urlencode(data).encode('utf-8')
req = Request(url,data=data)

# 第三步:用opener打开req对象,post登陆,保存了登陆的cookie
response = opener.open(req)  
# print(response.read().decode('utf-8'))

# 第四步:opener的get请求url
response = opener.open('http://www.renren.com/842465956/profile')
print(response.read().decode('utf-8'))