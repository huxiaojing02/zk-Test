def login_location(driver,userName,paw):
    driver.get("http://121.36.203.32:8082/#/login")
    driver.find_element_by_xpath(".//*[@placeholder='请输入用户名']").send_keys(userName)
    driver.find_element_by_xpath(".//*[@placeholder='请输入密码']").send_keys(paw)
    driver.find_element_by_class_name("ivu-btn").click()
