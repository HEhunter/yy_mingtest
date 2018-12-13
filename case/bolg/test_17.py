# coding:utf-8

import requests
# 先打开登录首页，获取部分cookie
url = "https://passport.cnblogs.com/user/signin"
headres = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3371.0 Safari/537.36",
    "Upgrade-Insecure-Requests": "1",
}

s = requests.session()
r = s.get(url=url,headers=headres,verify=False)
print(s.cookies)

# 添加登录需要的两个cookies
c = requests.cookies.RequestsCookieJar()

c.set(".CNBlogsCookie", "85813487C66634CDA42943D1502B326E7DB71962CFF0680927F012A6CE7804AB14C1B0A064290546BB39A3FF2F7897149798A5ECB526BB160948ED64CF381815A9306F97F865811B0B3DCEC1873D2A14C614A4C7B58A17891BF973A66717D2CC333B34E0") # 抓取的cookies
c.set(".Cnblogs.AspNetCore.Cookies", "CfDJ8KlpyPucjmhMuZTmH8oiYTP9q_XqE4qnmWhXEYdKZex1iHSxUAtFajs36Ff_4kf-GSq69zM8RljIoJEKN0ggS-dFWs_DdKE2oB-BX2b2S0_MGLQ3k3z77okmBHMgx6JYS-pQB8YOANxcqYEasNLn3t8xFVwXm8P4EDjhgCGR5LDuBRdeF5CwPv3VvtNzY1BqHKZzQC5D-QWBi_rr7GZeI1nUbf-B4tiBMgQavbn66Hho513AEy8R7H95GxMPeZuQxFOrUmv0w8057TCeoYTrr_YT0qupeDvrkiKF1OgHjPk_PdD9Fm2JnKNpbf10Ena22w")
s.cookies.update(c)
print(s.cookies)

# 保存草稿
url_2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"

body = {
    "__VIEWSTATE": "",
    "__VIEWSTATEGENERATOR": "FE27D343",
    "Editor$Edit$Advanced$chkComments": "on",
    "Editor$Edit$Advanced$chkDisplayHomePage": "on",
    "Editor$Edit$Advanced$chkMainSyndication": "on",
    "Editor$Edit$Advanced$ckbPublished": "on",
    "Editor$Edit$Advanced$tbEnryPassword": "",
    "Editor$Edit$Advanced$txbEntryName": "",
    "Editor$Edit$Advanced$txbExcerpt": "",
    "Editor$Edit$Advanced$txbTag": "",
    "Editor$Edit$EditorBody": "<p>没错。111李志强的确是大帅哥</p>",
    "Editor$Edit$lkbDraft": "存为草稿",
    "Editor$Edit$txbTitle": "李志强111"
}

r_2 = s.post(url_2,data=body,verify=False)
# 获取当前url地址
print(r_2.url)

# 正则提取需要的参数值
import re
postid = re.findall(r"postid=(.+?)&",r_2.url)
print(postid)# list
# print(postid[0])# 提取字符串

# 删除草稿箱
url_3= "https://i.cnblogs.com/post/delete"
json3 = {"postid": postid[0]}
r3 = s.post(url_3,json=json3,verify=False)
#print(r3.json())