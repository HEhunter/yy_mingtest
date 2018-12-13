from bs4 import BeautifulSoup
import requests
import os

r = requests.get("http://699pic.com/tupian/mote.html")
model = r.content
soup = BeautifulSoup(model, 'html.parser')
# 找出所有的标签
images = soup.find_all(class_="lazy")
#print(images) 返回list对象

for i in images:
    jpg_rl = i['data-original'] # 获取url地址
    title = i["title"]          # 返回title名称
    print(title)
    print(jpg_rl)
    print("")
    with open(os.getcwd() + "\\jpg\\" + title + '.jpg', 'wb') as f:
        f.write(requests.get(jpg_rl).content)
# except:
#     pass