
import unittest

# 用例执行顺序  setUpClass>setUp>test01>setDown>setUp>...

def login():
    print("先登录")

class LoginCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(" 前置，只执行一次")
        login()

    @classmethod
    def tearDownClass(cls):
        print("所有的用例执行完之后，最后执行这个")

    def setUp(self):  #  前置，每个用例都会先执行这个
        print(" 前置，每个用例都会先执行这个")

    def tearDown(self):
        print("后置：每次用例执行完都会执行这个")

    def test01(self):  # test method names begin with 'test'
        print("测试发帖啦！")
        a = 1
        b = 2
        c = a + b  #  测试结果
        self.assertEqual(c, 3)   # 断言是测试结果与期望结果对比，生成测试结果pass/fail

    def test02(self):
        a = 1
        b = 2
        result = a+b #  实际结果
        ex = 3  #  期望结果
        self.assertEqual(result, ex)  # 断言(检查点) pass or fail


if __name__ == '__main__':
    unittest.main()