import requests
import xlrd


url = "http://v.juhe.cn/weather/index"

para = {"cityname":"北京","dtype":"json","format":"2","key":"20948ca75703544740fe6edc0130ca5a"}

r = requests.get(url,params=para)
print(r.status_code)
print(r.json())
res = r.json()
print(res["resultcode"])
print(res["reason"])