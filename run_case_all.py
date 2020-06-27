import unittest
'''from 导模块时，必须从根寄出发'''
from zk_product.commont.HTMLTestRunner_cn import HTMLTestRunner
'''在路径前面加r，即保持字符原始值的意思。'''
casePath = r"D:\python-product\zk_product\case"
rule = "test*.py"
discover = unittest.defaultTestLoader.discover(start_dir=casePath, pattern=rule)
# print(discover)
reportPath="D:\\python-product\\zk_product\\report\\"+"login_report2.html"
'''读取reportPath，以二进制写入'''
fg = open(reportPath,"wb")
'''retry=1表示失败的用例重新跑一次'''
runner = HTMLTestRunner(stream=fg,
                        title="正凯系统登录测试报告",
                        description="测试登录功能",
                        retry=1)
runner.run(discover)
fg.close()