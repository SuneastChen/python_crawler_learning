from bs4 import BeautifulSoup
import requests
import time
from PIL import Image
import ssl
import easygui

def log(*args,**kwargs):
    print(*args, **kwargs)



def zhihu_longin():
    # 构建一个Session对象,用来保存Cookie
    ssl._create_default_https_context = ssl._create_unverified_context
    sess = requests.Session()  
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"}
    
    # 自动保存cookie信息,同时要获得xsrf用于data
    html = sess.get('https://www.zhihu.com/#signin',headers=headers).text
    soup = BeautifulSoup(html,'lxml')
    # 为了防止CSRF攻击(跨站请求伪造),通常叫跨域攻击,是一种利用网站对用户的一种信任机制来做坏事
    # 故网站会通过设置一个隐藏字段来存放这个MD5字符串,通过这个字符串来校验用户身份
    xsrf = soup.find('input',attrs={'name':"_xsrf"}).get('value')
    log(xsrf)


    # 处理验证码
    with open('yzm.gif','wb') as f:
        f.write(sess.get('https://www.zhihu.com/captcha.gif?r=%d&type=login&lang=cn'% (time.time()*1000),headers=headers).content)
    Image.open('yzm.gif').show()
    # yzm = input('请输入验证码数字,用","分开:')
    yzm=easygui.enterbox(msg='请输入验证码,用","分开:',title='验证码输入框',default='',strip=True,image=None) 
    points=[]
    for i in yzm.split(','):
        i = int(i)
        points.append([15+(i-1)*26,25])
    log(points)

    # 进行post登陆请求
    data ={
    '_xsrf':xsrf,
    'phone_num':'15161580934',
    'password':'zhihu789',
    'captcha_type':'cn',
    'captcha':'{"img_size":[200,44],"input_points":%s}' % points
    }
    req = sess.post('https://www.zhihu.com/login/phone_num',headers=headers,data=data)
    # print(req.text)

    req = sess.get('https://www.zhihu.com/people/zong-you-diao-min-xiang-hai-zhen-50-42/activities',headers=headers)
    print(req.text)






if __name__ == '__main__':
    zhihu_longin()


