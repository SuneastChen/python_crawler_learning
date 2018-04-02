# _*_ coding:utf-8 _*_
#!/usr/bin/python34

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import requests
from PIL import Image
import easygui






def zhixing(lasttime=17,user='15161580934',pswd='24quba'):
    driver = webdriver.Chrome()  # 也可换成Ie()，Firefox()等
    try:
        driver.set_page_load_timeout(10)    #设置超时停止加载
        driver.get('http://www.2478.com/')       
    except Exception: 
        pass
    # driver.maximize_window()
    driver.implicitly_wait(10)    #此方法较实用,发现元素立即返回,没有则一直等,直到10秒时间到,超时
    # def get_ele_times(driver,times,func):    #传入(driver,超时时间,函数)
    #     return WebDriverWait(driver,times).until(func)
    driver.find_element_by_xpath('//*[@id="cscHelp2"]/div[6]/a/img').click()     #关闭隐藏按钮
    driver.find_element_by_id('LoginName').send_keys(user)
    driver.find_element_by_id('LoginPwd').send_keys(pswd)


    driver.find_element_by_id('LoginCode').click()


    # img_ele=driver.find_element_by_xpath('//*[@id="form1"]/ul/li[3]/a/img')
    # img_src=img_ele.get_attribute('src')
    # print(img_src)    
    # yanzhengma_img=driver.get_screenshot_as_file('screen.png')
    # yanzhengma_img=Image.open('screen.png')
    # yanzhengma_img.show()
    

    #用户输入验证码
    yanzhengma=easygui.enterbox(msg='请输入验证码:',title='验证码输入框',default='',strip=True,image=None) 
    driver.find_element_by_id('LoginCode').send_keys(yanzhengma)

    try:
        driver.find_element_by_id('log_but').click()
    except Exception:
        pass

    #进入28界面
    driver.find_element_by_xpath('//*[@id="Banner"]/ul/li[9]/a').click()
    #关闭广告
    driver.find_element_by_xpath('//*[@id="QUBA_POP_ADS_CLOSE"]').click()

    #lasttime=17

    #标准赔率,list_my=标准赔率*1.01
    list_bz=[1000,333.33,166.67,100,66.66,47.61,35.71,27.77,22.22,18.18,15.87,14.49,13.69,13.33]
    percent=1.01
    list_my=list(map(lambda x :x*percent,list_bz))
    print(list_bz)
    print(list_my)




    totaltimes=0
    successtimes=0
    kuisuntimes=0   #初始连亏次数
    beishu=10    #初始倍数



    while 1:



        while 1:        
            if time.localtime()[4]%3==2 and time.localtime()[5]==(30-lasttime):
                break
        

        totaltimes+=1

        #标准投注数
        touzhu_bz=[1,3,6,10,15,21,28,36,45,55,63,69,73,75]
        #beishu=2


        touzhu_my=list(map(lambda x: x*beishu,touzhu_bz))
        



        try:
            #进入投注界面
            driver.find_element_by_xpath('/html/body/div[5]/table[3]/tbody/tr[7]/td[8]/a/img').click()
            driver.refresh()
              
        except Exception:
            driver.get('http://fun.2478.com/play/28/index.asp')
            time.sleep(6)
            continue


        driver.execute_script("window.scrollBy(0,370)","")   #向下滚动


        
        try:

            for i in range(13):   #1--13投注
                if float(driver.find_element_by_xpath('//*[@id="tr_{}"]/td[3]'.format(i)).text) > list_my[i]:
                    #driver.find_element_by_xpath('//*[@id="chk_{}"]'.format(i)).click()   #勾选
                    #driver.find_element_by_xpath('//*[@id="tr_{}"]/td[7]/input[2]'.format(i)).click()  #点10倍
                    shurukuang=driver.find_element_by_css_selector('#text_{}'.format(i))
                    #shurukuang.clear()
                    shurukuang.send_keys(touzhu_my[i])

            for i in range(13):   #27--14投注
                if float(driver.find_element_by_css_selector('table.datatableK:nth-child(5) > tbody:nth-child(2) > tr:nth-child({}) > td:nth-child(3)'.format(1+i)).text) > list_my[i]:
                    #driver.find_element_by_xpath('//*[@id="chk_{}"]'.format(27-i)).click()   #勾选
                    # driver.find_element_by_css_selector('table.datatableK:nth-child(5) > tbody:nth-child(2) > tr:nth-child({}) > td:nth-child(7) > input:nth-child(2)'.format(1+i)).click()  #点10倍
                    shurukuang=driver.find_element_by_css_selector('#text_{}'.format(27-i))
                    #shurukuang.clear()
                    shurukuang.send_keys(touzhu_my[i])
            shurukuang.send_keys(Keys.RETURN)      #按回车
            if driver.switch_to_alert():
                driver.switch_to_alert().accept()
                driver.get('http://fun.2478.com/play/28/index.asp')
                time.sleep(6)

        except Exception:     #此处容易产生异常
            driver.get('http://fun.2478.com/play/28/index.asp')
            time.sleep(6)

        finally:
            time.sleep(5)
            xiazhuje=driver.find_element_by_xpath('/html/body/div[5]/table[3]/tbody/tr[7]/td[7]/div/a/span[2]').text
            if xiazhuje!="0":

                successtimes+=1
                
            time.sleep(35)

            shangqiyl=driver.find_element_by_xpath('/html/body/div[5]/table[3]/tbody/tr[8]/td[7]/div/a/span[1]').text
            jinriyl=driver.find_element_by_xpath('/html/body/div[5]/table[2]/tbody/tr[2]/td/strong/span').text
            zongji=driver.find_element_by_xpath('//*[@id="marqueediv"]/a[2]').text
            print('总投注数:{},成功投注数:{},上期下注额:{},上期盈利额:{},今日战绩:{},账户总趣点:{}'.format(totaltimes,successtimes,xiazhuje,shangqiyl,jinriyl,zongji))


            #判断投注倍数


            if shangqiyl=="0" and xiazhuje!='0':
                kuisuntimes+=1


            # if kuisuntimes>=5:
            #     beishu+=1
            #     print('投注倍数变更为{}'.format(beishu))
            #     kuisuntimes=0
            # if shangqiyl!="0" and beishu>6:    #此处为最小倍数
            #     beishu-=1
            #     print('投注倍数变更为{}'.format(beishu))
            #     kuisuntimes=0



            if kuisuntimes>=3 and beishu>8:
                beishu-=1
                print('投注倍数变更为{}'.format(beishu))
                kuisuntimes=0
            if shangqiyl!="0":    #此处为最小倍数
                beishu+=1
                print('投注倍数变更为{}'.format(beishu))
                kuisuntimes=0



            time.sleep(80)

    
zhixing(18)    #传入剩余时间参数








