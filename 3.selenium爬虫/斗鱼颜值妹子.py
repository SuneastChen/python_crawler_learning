from selenium import webdriver
import os
import requests
from lxml import etree
import time
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.PhantomJS()
driver.get('https://www.douyu.com/directory/game/yz')


try:
    os.mkdir('./斗鱼美女imgs')
except FileExistsError:
    pass

for i in range(3):
    
    # 等待的两种方式
    # driver.implicitly_wait(10)
    # WebDriverWait(driver, 10).until(lambda x : 1)


    # 不同的定位方式
    # print(etree.HTML(html).xpath('//*[@class="shark-pager-item current"]'))
    # print(driver.find_element_by_xpath('//*[@class="shark-pager-item current"]'))
    # print(driver.find_element_by_class_name("current"))   # 有点特殊

    # 显式等待方式,注意传参的方式
    WebDriverWait(driver, 10).until(lambda driver : int(driver.find_element_by_xpath('//*[@class="shark-pager-item current"]').text)==i+1)
    # WebDriverWait(driver.page_source, 10).until(lambda html : int(etree.HTML(html).xpath('//*[@class="shark-pager-item current"]/text()')[0])==i+1)
    
    html = driver.page_source

    name_list = etree.HTML(html).xpath('//*[@id="live-list-contentbox"]/li/a/div/p/span[1]/text()')
    imgurl_list = etree.HTML(html).xpath('//*[@id="live-list-contentbox"]/li/a/span/img[@height]/@data-original')
    roomname_list = etree.HTML(html).xpath('//*[@id="live-list-contentbox"]/li/a/@title')
    for n,r in zip(name_list,roomname_list):
        print(n,'---->',r)
    # print('name_list',name_list)
    for i in range(len(imgurl_list)):
        with open('./斗鱼美女imgs/'+name_list[i]+'.jpg','wb') as f:
            f.write(requests.get(imgurl_list[i]).content)
        print(name_list[i],'保存成功!')

    print('*'*50)
    driver.find_element_by_xpath('//a[@class="shark-pager-next"]').click()
    

driver.quit()