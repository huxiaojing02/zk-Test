#
# '''#通过函数，传入参数的测试，叫单元测试
#
# def add (a,b):
#     c=a+b*2
#     return c
# #当前脚本下执行，别的脚本调用时，不执行if代码
# if __name__=="__main__":
#     d = add(1,3)
#     print(d)
# '''
#
#
# '''import unittest
# help(unittest)
# '''
#
#
# import unittest
# '''类名用驼峰，IntegerArithmeticTestCase继承unittest.TestCase'''
# class IntegerArithmeticTestCase(unittest.TestCase):
#     def setUp(self) -> None:
#         '''每个用例前，执行一次'''
#         print('打开浏览器')
#     def tearDown(self) -> None:
#         '''每个用例后，执行一次'''
#         print('关闭浏览器')
#     @classmethod
#     def setUpClass(cls) -> None:
#         '''用例前，只执行一次'''
#         print('登录')
#     @classmethod
#     def tearDownClass(cls) -> None:
#         '''用例后，只执行一次'''
#         print('退出')
#     def test_1(self):
#         print('用例1')
#     def test_2(self):
#         print('用例2')
# if __name__ == '__main__':
#     unittest.main()
