import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50'}
proxies = {"http": "http://1050521852:vch6gryw@10.10.1.10:3128"}
sess = requests.Session()
req = requests.get(url='http://www.ipdizhichaxun.com/',proxies=proxies,headers=headers)
print(req.text)

