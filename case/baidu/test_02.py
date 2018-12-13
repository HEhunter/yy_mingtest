import requests

def login(s, url, payload):
    '''登录'''
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0)Gecko/20100101 Firefox/44.0",
               "Accept": "application/json, text/javascript, */*; q=0.01",
               "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
               "Accept-Encoding": "gzip, deflate, br",
               "Content-Type": "application/json; charset=utf-8",
               "X-Requested-With": "XMLHttpRequest",
               "Content-Length": "385",
               "Cookie": "xxx 已省略",
               "Connection": "keep-alive"
               }
    r = s.post(url, json= payload, headers=headers, verify=False)
    result = r.json
    print(result)
    return result['seccess']  # 返回True或False

def save_box(s, url2, title, body_data):
    '''# 获取保存之后URL地址'''
    body = {
        "__VIEWSTATE": "",
        "__VIEWSTATEGENERATOR": "FE27D343",
        "Editor$Edit$txbTitle": title,
        "Editor$Edit$EditorBody": "<p>" + body_data + "</p>",
        "Editor$Edit$Advanced$ckbPublished": "on",
        "Editor$Edit$Advanced$chkDisplayHomePage": "on",
        "Editor$Edit$Advanced$chkComments": "on",
        "Editor$Edit$Advanced$chkMainSyndication": "on",
        "Editor$Edit$lkbDraft": "存为草稿",
    }
    r2 = s.post(url2, data=body, verify=False)
    print(r2.url)
    return r2.url

def get_postid(u):
    '''正则提取postid'''
    import re
    postid = re.fondall(r"postid=(.+?)&", u)
    print(postid)  # 这里是list
    if len(postid) < 1:
        return ''
    else:
        return postid[0]
def delete_box(s, url3, postid):
    '''删除草稿箱'''
    json3 = {"postId": postid}
    r3 = s.post(url3, json=json3, verify= False)
    print(r3.json())

if __name__ == "__main__":
    url = "https://passport.cnblogs.com/user/signin"
    payload = {
        "input1": "xxx",
        "input2": "xxx",
        "remember": True
    }
    s = requests.session()
    login(s, url, payload)
    url2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
    u = save_box(s, url2, "标题", "正文内容")
    postid = get_postid(u)
    url3 = "https://i.cnblogs.com/post/delete"
    delete_box(s, url3, postid)