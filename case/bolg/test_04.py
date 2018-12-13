# from bs4 import BeautifulSoup
#
# jinri = open('zhang_wei.html')
# soup = BeautifulSoup(jinri)
#
# print(soup.prettify())

from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.qiushibaike.com/")
qiubai = r.content
soup = BeautifulSoup(qiubai, "html.parser")
duanzi = soup.find_all(class_="content")

for i in duanzi:
    # tag 的.contents 属性可以将tag的子节点以列表的方式输出
    duan = i.span.contents[0]  # 取第一个
    print(duan)