import requests

url = "http://127.0.0.1:8080/j_acegi_security_check"

body = {"j_username": "hemingwei",
        "j_password": "123456",
        "remember_me": "on",
        "from": "/",
        "Jenkins-Crumb": "f27f3a6fa69b114ca89738fea45defd9",
        "json": '{"j_username": "hemingwei", "j_password": "123456", "remember_me": true, "from": "", "Jenkins-Crumb": "f27f3a6fa69b114ca89738fea45defd9"}',
        "Submit": "登录"
        }

head = {"Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3371.0 Safari/537.36",
        "Cookie": "JSESSIONID.74d1314f=node01oz8t77cc80dwspaj9e3l2t221.node0",
        "Upgrade-Insecure-Requests": "1"
}

r = requests.post(url=url,data=body,headers=head)
print(r.content)