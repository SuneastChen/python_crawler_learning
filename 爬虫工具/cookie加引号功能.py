import re
import easygui

str1 = easygui.textbox(msg='请输入cookies数据:\n(以"分号"结尾)',title='格式化cookie',codebox=0)
# str1 = 'anonymid=j9lb4g45-9bvguo; depovince=GW; _r01_=1; jebecookies=8430f330-8f10-43de-a2f6-832f110fc767|||||; ick_login=8db9ffd0-74a9-4cff-a8a1-32dee10e2763; _de=280B7DBFC68B1D9EF7F8541ED66B57EB; p=e558a1fed7a994bcb21fa5f3a10527d43; first_login_flag=1; ln_uact=15161580934; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=a039ac62de73d87fe1e7759a14adb9103; societyguester=a039ac62de73d87fe1e7759a14adb9103; id=960617323; xnsid=78ee621e; loginfrom=syshome; ch_id=10016; wpsid=14774186144651; jebe_key=23873db9-1f26-4756-b77f-9696ebfe5778%7C2183573fa959e5a988bbddad92a81ca0%7C1509799902784%7C1%7C1509799901478; wp_fold=0'
str2 = re.sub(r'\s?(.*?)=(.*?);',r'"\1": "\2",',str1)
print(str2)