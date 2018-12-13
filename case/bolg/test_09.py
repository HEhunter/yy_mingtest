
import requests

#  请求综合管廊登录页面
url = "http://192.168.0.80:18005/oauth/token"

nes = {"clientId": "ut.usscity.com",
        "password": "123456",
        "userName": "chenwh",
        "VerificationCode": "",
        "VerificationCodeKey": "d5bd96bb-7eda-44e7-a0ef-46f906653547"
        }

head = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3371.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive"

}

r = requests.post(url=url,json=nes,headers=head)
print(r.content)