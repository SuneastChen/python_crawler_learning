# encoding=utf-8
import requests
from bs4 import BeautifulSoup
import time
import json

#这是首页加载的内容
# req = requests.get('http://news.sina.com.cn/china/')
# # print(req.content.decode('utf-8'))
# req.encoding = 'utf-8'
# soup = BeautifulSoup(req.text,'lxml')
# divs_list = soup.find('div', id='subShowContent1').find_all('div',class_='news-item')
# # print(divs_list)
# contents_list = []

# for div in divs_list:
#     if len(div.find_all('h2'))>0:
#         h2 = div.find('h2').text
#         time = div.find(class_='time').text
#         a = div.find('a')['href']
#         new_dict = {}
#         new_dict['title'] = h2
#         new_dict['url'] = a
#         new_dict['time'] = time
#         contents_list.append(new_dict)

# print(contents_list)



# ajax加载的内容,同时首页的第一页也可以构造url来获取
def get_news_dict(pages):
    now_time = str(time.time()*1000)[:-5]
    contents_list = []
    for p in range(1,pages):
        url = 'http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page={}&callback=newsloadercallback&_={}'.format(p, now_time) 
        response_dict = json.loads(requests.get(url).text[21:-2])
        for new in response_dict['result']['data']:          
            new_dict = {}
            new_dict['title'] = new['title']
            new_dict['url'] = new['url']
            new_dict['time'] = time.strftime("%m-%d  %X",time.localtime(int(new['createtime'])/1000))
            new_dict['原标题'] = new['ext5']
            contents_list.append(new_dict)
    return contents_list




if __name__ == '__main__':
    contents_list = get_news_dict(4)
    for new in contents_list:
        print(new['原标题'])