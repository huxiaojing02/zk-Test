from selenium import webdriver
from time import sleep
'''绝对路径'''
import unittest
from zk_product.commont.login_position import login_location
'''相对路径'''
'''from ..commont.login_position import login_location'''

class LoginTest(unittest.TestCase):
    '''
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver= webdriver.Chrome()
        cls.driver.get("http://localhost:8080/#/login")'''
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/#/login")
        sleep(3)
        self.is_alert_exsit()
        '''清除cookies'''
        self.driver.delete_all_cookies()
        '''刷新页面'''
        self.driver.refresh()

    def get_login_user_name(self):
        '''是否登录成功'''
        try:
            user_name = self.driver.find_element_by_class_name("main-user-name").text
            return  user_name
        except:
            return ""

    def is_alert_exsit(self):
        '''是否有弹框'''
        try:
            sleep(3)
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept() #关闭alert弹框
            return  alert_text
        except:
            return ''
    def test_01(self):
        login_location(self.driver,'xiaohu','123456')
        sleep(3)
        user_name = self.get_login_user_name()
        print('测试结果1：%s'%user_name)
        self.assertTrue(user_name=='胡晓静')
    def test_02(self):
        '''登录失败'''
        login_location(self.driver,'wangyixuan','123456')
        sleep(3)
        user_name = self.get_login_user_name()
        print('测试结果2：%s'%user_name)
        self.assertTrue(user_name == '1111')
    # def tearDown(self) -> None:
    #     self.driver.quit()
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.driver.quit()

#使用框架运行
if __name__ == "__main__":
    unittest.main()