# encoding=utf8

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


# 前台开启浏览器模式
def openChrome():
    # 加启动配置
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    # 打开chrome浏览器
    driver = webdriver.Chrome(chrome_options=option)
    return driver


# 授权操作
def operationAuth(driver):
    url = "http://www.dd.com:8080/visittest"
    driver.get(url)
    # 找到账号密码并登录
    elem = driver.find_element_by_id("log-cacct")
    elem.send_keys("11599")
    elem = driver.find_element_by_id("log-pwd")
    elem.send_keys("a1234567")
    # 提交表单
    driver.find_element_by_id("login-button").click()

    print('登录成功！')
    return driver


# 方法主入口
if __name__ == '__main__':
    # 加启动配置
    driver = openChrome()
    # 打开并登录系统
    driver = operationAuth(driver)
    # 打开义教填报数据
    elem = driver.find_element_by_xpath("//*[@id=\"main_msg\"]/div[3]/div/div[1]/div/div[1]")
    elem.click()
    driver.switch_to.frame("windowBox")
    while True:
        try:
            elem2 = driver.find_element_by_link_text("填报")
            elem2.click()
            break
        except Exception:
            continue
