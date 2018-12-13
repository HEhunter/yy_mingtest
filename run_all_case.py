# coding:utf-8
import unittest

def all_case():
    # 待执行用例的目录
    case_dir = "D:\\test\\mingtest\\case"

    testcase = unittest.TestSuite()

    discover = unittest.defaultTestLoader.discover(case_dir,
                                                   pattern="test*.py",
                                                   top_level_dir=None)
    # discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            # 添加用例到testcase
            testcase.addTests(test_case)
    # print(testcase)
        return testcase
    # testcase.addTests(discover) # 直接加载discover
    # print(testcase)
    # return testcase
if __name__ == "__main__":
    # 返回实例
    runner = unittest.TextTestRunner
    # # run所有用例
    # all_case()
    import HTMLTestRunner_cn
    report_path = "D:\\test\\mingtest\\report\\result.html"

    fp = open(report_path,"wb")
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                           title=u'这是我的自动化测试报告',
                                           description=u'用例执行情况:')
    runner.run(all_case())
    fp.close()