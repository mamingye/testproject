"""#Urllib是python内置的HTTP请求库
 包括以下模块
urllib.request 请求模块
urllib.error 异常处理模块
urllib.parse url解析模块  parse和paste的区别
urllib.robotparser robots.txt解析模块"""


import urllib.request #Urllib是python内置的HTTP请求库
resp=urllib.request.urlopen('http://www.weibo.com')
print(resp.read().decode('utf-8'))







python main.py --startdate 2019-03-11 --enddate 2019-03-14