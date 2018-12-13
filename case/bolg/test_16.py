# coding utf-8

import urllib.parse
import re

url = "http://zzk.cnblogs.com/s/blogpost?Keywords=%E4%B8%AD%E6%96%87"
postid = re.findall(r"Keywords=(.+?)$", url)
print(postid) # 这里是list
print(postid[0])#  提取为字符串
#postid = re.findall(r"postid=(.+?)&", r2.url)

ur2 = "https://i.cnblogs.com/PostDone.aspx?postid=7900629"
postid = re.findall(r"postid=(.+?)$", ur2)
print(postid)
print(postid[0])