"""
(Chrome Browser)https://chromedriver.storage.googleapis.com/index.html

first_method:

    可 elements 查找多个!
    find_element_by_xpath()
    find_element_by_class_name()	
    find_element_by_css_selector()	
    find_element_by_id()
    find_element_by_link_text()
    find_element_by_name()  ---name 属性
    find_element_by_partial_link_text() ---链接文本的部分匹配查找
    find_element_by_tag_name()  ---标签名

second_method:

    find_element(By.XPATH, "XXX")

    from selenium.webdriver.common.by import By
    find_element('xpath', "XXX")

    ID = "id" 
    LINK_TEXT = "link text" 
    PARTIAL_LINK_TEXT = "partial link text" 
    NAME = "name" 
    TAG_NAME = "tag name" 
    CLASS_NAME = "class name" 
    CSS_SELECTOR = "css selector" 
"""


from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get('https://github.com/CHINA-gcc/CHINA-gcc.github.io')
driver.find_element_by_xpath("//summary[@class='btn css-truncate btn-sm']/span[@class='css-truncate-target']").click()