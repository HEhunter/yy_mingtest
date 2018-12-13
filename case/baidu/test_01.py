import unittest
import time
class Test(unittest.TestCase):
    def setUp(self):
        print("start!")
    def tearDown(self):
        time.sleep(1)
        print("end!")
    def test01(self):
        u'''测试登录用例，账号：xx 密码 xx'''
        print("执行测试用例01")
    def test03(self):
        u'''测试登搜索用例，关键词：xxx'''
        print("执行测试用例 03")
print("李志强")