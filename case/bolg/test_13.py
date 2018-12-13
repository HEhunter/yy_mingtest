

g = 12
h = 12.5
a = None
b = False
c = "abs123"
d = [1,2,3,4,'5']  # list
e = (1,2,3,4,'5')  # tuple  只读不能更改
f = {
    "input1": "xxx",
    "input2": "baf",
    "n": True,
    "a": "",

}

# type 查看数据类型

print(type(b))

# 查询
print(f["n"])

# 增加数据
f["a"] = "bbbbbb"
f["dddd"] = "cccc"
print(f)

# 删除数据
del(f["a"])
print(f)

# 修改数据
f["dddd"] = "abcdef"
print(f)

import json
p = {
    "a": None,
    "b": False,
    "c": True,
    "d": "中文",
    "h": 123421,
    "e": ["1",12],
    "f": ("In", 90),
    "g": {"h": 1,
          "i": "11",
          "j": True
          }
}
print(type(p))
print("Python里面的:%s"%p)

p_j = json.dumps(p)  # 转换成json数据  dumps
print("json里面的数据 %s"%p_j)
print(type(p_j))

# 服务端返回json
j_dict = json.loads(p_j) # 转换字典  loads
print(j_dict)
print(type(j_dict))
print(j_dict["c"])

aaa = '{"success":true}'
d = json.loads(aaa)
print(d['success'])


