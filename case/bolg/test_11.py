# coding:utf-8

import requests

s = requests.session()  #  session保持会话

login_url = "https://passport.cnblogs.com/user/signin "
head = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3371.0 Safari/537.36"}

r1 = s.get(url=login_url,headers=head,verify=False)
print(r1.cookies)

# 添加cookies到session
# 添加cookies
c = requests.cookies.RequestsCookieJar()
c.set(".CNBlogsCookie", "DB4C91DDEC93C88B73C5BD7B8C68DC72ECD366E2A1E07AEE76539E0CA020973E9B76B9B3044820C0A8327F26914942B1BD39C4E1910BE0AAB48455C0BF554AE2A5CAB7ABBAF79F6F50EA05FA823CCBAFB64D4A07F5BF9CB0C4B7DBFEF2E8BE7ECEB4E76B")
c.set(".Cnblogs.AspNetCore.Cookies", "CfDJ8KlpyPucjmhMuZTmH8oiYTOAELgqed1c6q0VlYpcg7xF5Xge5Iemp73_ol-PPEMWWZlr3Ys9PxMlJb2LHIbFj77HbHU8oSr8LKqyU4tLK45kwf_7uoAbYoZs8AMCZSfTccyIK0m2JI4AOWGmLYrhkgLy9twnxGISmPdnNUo3RhbaypQViH3iPM-w82kl3DcGIF3N0Xum-U_a9HBxStfJwHVwOOC-BoaF0PREu-ZwIq5GBxioN1MkYRHSVxbN23rLggOtocdxamVtv3cUyXZOuHG2Er6j5GL2SWLIQu_0fT9T2MPVqPn_pOWpz5UzbQN6Ow")
s.cookies.update(c)

print(r1.cookies)

# 验证是否登录成功
bianji_url = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
r2 = s.get(bianji_url,verify=False)
print(r2.text)