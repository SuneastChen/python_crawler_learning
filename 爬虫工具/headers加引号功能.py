import re
import easygui

# str1 = '''
# Accept:*/*
# Accept-Language:zh-CN,zh;q=0.8
# Connection:keep-alive
# Content-Type:application/x-www-form-urlencoded; charset=UTF-8
# Referer:https://www.zhihu.com/
# User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0
# '''
str1 = easygui.textbox(msg='请输入headers数据:',title='格式化headers',codebox=0)
str2 = re.sub(r'(.*):(.*)',r'"\1": "\2",',str1)
print(str2)