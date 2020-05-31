import requests
import re

url2 = "参数传递接口"
s = requests.session() # 为了保持和下一个接口建立相同的连接通道
res = s.get(url2)
para1 = re.findall(r'xxxxxxxxx(.+?)xxxxx',res.text) # 正则表达式获取参数值

url = "参数传递到的接口"
para = {"传递参数name":para1[0],"参数name":"参数value","参数1name":"参数1value"}
r = s.post(url,data=para) #这里直接写通道s调用即可
# 也可以requests调用
# r = requests.post(url,data=para)

