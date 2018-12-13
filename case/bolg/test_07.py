
import requests
import urllib3
# 禁用安全警告
urllib3.disable_warnings()

# # 博客园
# r = requests.get("http://www.cnblogs.com/yoyoketang/")
# print(r.status_code)    # 状态码
# print(r.headers)
# print(r.text)

url = "http://zzk.cnblogs.com/s/blogpost"
par = {"Keywords": "yoyoketang"}  # 参数存在字典里面
header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3371.0 Safari/537.36",
          "Cookie": "_ga=GA1.2.758003995.1542870548; __gads=ID=b7e9d93fab6d14af:T=1542870550:S=ALNI_MZ0bqVWrjwpvl1wMvGuV1NI-RrT-A; .CNBlogsCookie=3EF7814D4D89A4A4AF5230A270F269E282F3ADBFC7E173154A894ED80515F28121EF70E699D8AA816FC1412091431802A0FAEF3C5E38BC9677D3BBE18BFFA6D8880CA756B901FFFA47CA01547C1400A880E0BFA288C05D6F7B06495EAE46AB5AC012E632; .Cnblogs.AspNetCore.Cookies=CfDJ8KlpyPucjmhMuZTmH8oiYTPj_sPY_1U9C3hpu6s8TdVgHbBwVeQm9lbVI9G8lrK1duXcBxp1rp1pJwI6Ot-B16-nVePzF3yDO5lu55EPoPDRBZCx0DYYQ9fdMsAwRSCdk5nGwgHI_ybufD_AeaM0g9jE0MCjuBhvABPKG7B6kdnF3R1MsZMX9rU5GU_iPdt-lJ-Dzo2jj3tR1KcP72xiv4T3mlqW3LDXn73P5LVOKF_TljMbcsXMvUVGaodb6Cua9qlfDtkgA4uxDsuwrbiwIFW8oRcnCAK_4jlIG75ZMw11fc4qvLHTV2X_-r283eLvMw",
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
          "Accept-Encoding": "gzip, deflate, br",
          "Accept-Language": "zh-CN,zh;q=0.9",
          }

res1 = requests.get(url=url, params=par, headers=header,verify=False)
print(res1.status_code) # 状态码
print(res1.encoding)  # 编码格式
print(res1.cookies)
print(res1.text) # 返回文本信息
print(res1.url)  # 返回URL地址