
#我的电子邮件tom@gamil.com。
#将什么发送到jerry123@163.com或者3123432@qq.com.
#若遇特殊情况打电话给18212344567。
import re

Message='''我的电子邮件tom@gamil.com。
将什么发送到jerry123@163.com或者3123432@qq.com.
若遇特殊情况打电话给18212344567。'''

Emails = re.findall(r'[a-zA-Z0-9]+@[a-z0-9]+\.com',Message)
phonenumbers = re.findall(r'\d{11}',Message)
print(Emails)\
              
print(phonenumbers)
