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
    driver = webdriver.PhantomJS()  # 也可换成Ie()，Firefox()等
    # driver = webdriver.Chrome()  # 也可换成Ie()，Firefox()等

    driver.set_page_load_timeout(10)    #设置超时停止加载
    driver.implicitly_wait(5)

    try:
        driver.get('http://www.2478.com/')
    except:
        pass
    # first_iframe = driver.find_element_by_xpath('//iframe[@class="id-focont js-iframe hidden"]')
    driver.switch_to_frame(0)    # 切换到iframe,通过索引(从0开始)或先找到,再切换过去


    driver.find_element_by_xpath('//input[@name="account"]').send_keys(user)  # 用户名
    driver.find_element_by_xpath('//input[@name="pass"]').send_keys(pswd) # 密码
    driver.find_element_by_xpath('//input[@name="code"]').click() # 验证码
    time.sleep(2)
    WebDriverWait(driver, 3).until(lambda x:x.find_element_by_xpath('//img[@class="js-codeimg hidden"]').get_attribute('src'))
    
    driver.save_screenshot(r'screen.png')  # 保存截图
    Image.open(r'screen.png').show()  #查看截图的验证码
    

    #用户输入验证码
    yanzhengma=easygui.enterbox(msg='请输入验证码:',title='验证码输入框',default='',strip=True,image=None) 
    driver.find_element_by_xpath('//input[@name="code"]').send_keys(yanzhengma) # 输入验证码


    try:
        driver.find_element_by_xpath('//input[@class="id-su"]').click()
        time.sleep(1)  # 点击之后需要小休
    except Exception:
        pass


    driver.switch_to_default_content()    # 切换到主内容

    #进入28主界面
    print(driver.find_element_by_xpath('//div[@class="htop-nav"]/a[8]').text)
    driver.find_element_by_xpath('//div[@class="htop-nav"]/a[8]').click()

    # 关闭广告
    # 用PhantomJS打开此广告不可见
    # driver.find_element_by_xpath('//div[@id="QUBA_POP_ADS_CLOSE"]').click()

    #标准赔率,list_my=标准赔率*1.01
    list_bz=[1000,333.33,166.67,100,66.66,47.61,35.71,27.77,22.22,18.18,15.87,14.49,13.69,13.33]
    percent=1.01
    list_my=list(map(lambda x :x*percent,list_bz))
    print('标准赔率', list_bz)
    print('设定赔率', list_my)




    totaltimes=0  # 投注总次数
    successtimes=0 # 投注成功次数
    kuisuntimes=0   # 初始连亏次数
    beishu=40    # 初始投注倍数


    while 1:

        while 1:        
            if time.localtime()[4]%3==2 and time.localtime()[5]==(30-lasttime):
                break
            else:
                time.sleep(0.8)
        print('开始投注...')

        # 标准投注的一个单位数
        touzhu_bz=[1,3,6,10,15,21,28,36,45,55,63,69,73,75]
        touzhu_my=list(map(lambda x: x*beishu,touzhu_bz))
        

        try:
            #进入投注界面
            driver.find_element_by_xpath('/html/body/div[5]/table[3]/tbody/tr[7]/td[8]/a/img').click()            
        except Exception:
            while 1:
                try:
                    driver.get('http://fun.2478.com/play/28/')
                    break
                except:
                    continue
            continue

        # PhantomJS不需要滚动
        # driver.execute_script("window.scrollBy(0,370)","")   #向下滚动

        try:
            for i in range(13):   #1--13号投注
                if float(driver.find_element_by_xpath('//*[@id="tr_{}"]/td[3]'.format(i)).text) > list_my[i]:
                    shurukuang=driver.find_element_by_css_selector('#text_{}'.format(i))
                    shurukuang.send_keys(touzhu_my[i])

            for i in range(13):   #27--14号投注
                if float(driver.find_element_by_css_selector('table.datatableK:nth-child(5) > tbody:nth-child(2) > tr:nth-child({}) > td:nth-child(3)'.format(1+i)).text) > list_my[i]:
                    shurukuang=driver.find_element_by_css_selector('#text_{}'.format(27-i))
                    shurukuang.send_keys(touzhu_my[i])
            shurukuang.send_keys(Keys.RETURN)      #按回车
        except:
            continue

        # 如果没来得及投注,会弹出"当前期数不可投注",点击确定
        try:
            print('投注完成,剩余时间:',driver.find_element_by_xpath('//div[@id="Gclock"]/span').text)
            driver.find_element_by_xpath('/html/body/div[11]/div[3]/div[2]/div/p[2]/a/i').click()
        except:
            pass
        


            
        time.sleep(40)    # 等她自动刷新,统计盈利亏损状况
        while 1:
            try:        
                xiazhuje=driver.find_element_by_xpath('/html/body/div[5]/table[3]/tbody/tr[8]/td[7]/div/a/span[2]').text
                shangqiyl=driver.find_element_by_xpath('/html/body/div[5]/table[3]/tbody/tr[8]/td[7]/div/a/span[1]').text
                jinriyl=driver.find_element_by_xpath('/html/body/div[5]/table[2]/tbody/tr[2]/td/strong/span').text
                zongji=driver.find_element_by_xpath('//*[@id="marqueediv"]/a[2]').text
                break
            except:
                driver.refresh()
                continue
        totaltimes+=1
        if xiazhuje!="0":
            successtimes+=1
        print('总投注数:{},成功投注数:{},上期下注额:{},上期盈利额:{},今日战绩:{},账户总趣点:{}'.format(totaltimes,successtimes,xiazhuje,shangqiyl,jinriyl,zongji))

        # print('判断前..........................')
        # print('kuisuntimes:',kuisuntimes,'beishu:',beishu)

        if shangqiyl=="0" and xiazhuje!='0':
            kuisuntimes+=1
        #判断下期投注倍数
        if kuisuntimes>=1 and beishu>36:  #连输指定次数减注,并且限制最小投注倍数
            beishu-=1
            print('************调整下期投注倍数为{}'.format(beishu))
            kuisuntimes=0
        if shangqiyl!="0":    # 盈利了加注
            beishu+=1
            print('************调整下期投注倍数为{}'.format(beishu))
            kuisuntimes=0
            
        # print('判断后..........................')
        # print('kuisuntimes:',kuisuntimes,'beishu:',beishu)


        time.sleep(80)

    
zhixing(10)    #传入剩余时间参数








