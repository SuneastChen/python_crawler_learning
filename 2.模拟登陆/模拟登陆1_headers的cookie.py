
from urllib.request import Request,urlopen


headers={"Host": "www.renren.com",
"Connection": "keep-alive",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
# "Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",
"Referer": "http://www.renren.com/SysHome.do",
# "Accept-Encoding": "gzip, deflate, sdch",
"Accept-Language": "zh-CN,zh;q=0.8",
"Cookie": "anonymid=j991lsb5-55alqs; XNESSESSIONID=abcCBE82G0imm59yZZA9v; depovince=GW; _r01_=1; JSESSIONID=abc64B_GyaRrC9Eh00A9v; springskin=set; vip=1; wp=0; ick=58aad0b4-87ed-4a1e-943a-40567f4279f7; jebe_key=8e13a665-5079-4c3c-8772-b432f7956fe7%7C2183573fa959e5a988bbddad92a81ca0%7C1509057935309%7C1%7C1509061857162; jebe_key=8e13a665-5079-4c3c-8772-b432f7956fe7%7C2183573fa959e5a988bbddad92a81ca0%7C1509057935309%7C1; ch_id=10016; wp_fold=0; jebecookies=e1f8ceac-49e2-4b34-865a-eb06459b7fcc|||||; ick_login=b190808e-0d0e-43f7-b8bf-fa4e7a8675fa; _de=280B7DBFC68B1D9EF7F8541ED66B57EB; p=f2dc778da057215672fd1903ea9cc7dc3; first_login_flag=1; ln_uact=15161580934; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=335baeb2393391653a57b496a0f2b37a3; societyguester=335baeb2393391653a57b496a0f2b37a3; id=960617323; xnsid=a4e0d8be; loginfrom=syshome"}    #伪造客户端的头部信息,head在之Request对象生成之前

req = Request('http://www.renren.com/842465956/profile',headers=headers)  #Request必须用大写,构建Request对象

response = urlopen(req)
html = response.read()

print(html.decode('utf-8'))