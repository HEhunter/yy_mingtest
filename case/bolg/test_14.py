
import requests

# url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-1202247993797-yunda.html"
url = "http://www.kuaidi100.com/query?type=zhongtong&postid=75108286196439&id=19&valicode=&temp=0.7226150759410155 "

res = requests.post(url)
print(res.text)
d = res.json() # json解析成python里面的字典
print(type(d))
print(d)
print(d['data'])
print(d["data"][0])
print(d["data"][0]["context"])
result = d["data"][0]["context"]
if "派件" in result:
    print("已经签收成功了")
else:
    print("还没签收成功")