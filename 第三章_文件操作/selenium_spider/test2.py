#coding=utf-8
#www.testclass.cn
#Altumn

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://www.baidu.com')

#首先定位到要悬停的元素;
element = driver.find_element_by_link_text("设置")
print(element)

#对定位到的元素执行鼠标悬停操作;
ActionChains(driver).move_to_element(element).perform()

#等待两秒，为了展示鼠标悬停效果；
time.sleep(2)

#弹出的Ajax,单击'高级搜索';
driver.find_element_by_link_text('高级搜索').click()