from urllib.request import Request,urlopen
import time
import math
import json


class NeiHan():
    def __init__(self,page):
        self.baseurl = 'http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time='
        self.page = page
        self.text =[]
    
    # 根据html_dict取段子内容加入到text列表
    def get_text(self,html_dict):
        for data_dict in html_dict['data']['data']:
            self.text.append(data_dict['group']['content'])

    # 根据html_dict取max_time,供下一次url用
    def get_max_time(self,html_dict):
        return html_dict['data']['max_time']

    # 打开url,获取html_dict,调用另外两个方法,最终返回text列表
    def get_content(self):
        headers = headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"}
        max_time = math.floor(time.time())
        for i in range(1,self.page):
            req = Request(self.baseurl+str(max_time),headers=headers)
            html_dict = json.loads(urlopen(req).read().decode('gbk'))
            max_time = self.get_max_time(html_dict)
            print(max_time)
            self.get_text(html_dict)
        return self.text

if __name__ == '__main__':
    
    neihan = NeiHan(6)
    print(neihan.get_content())

