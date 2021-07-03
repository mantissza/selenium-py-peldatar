# 006.md hw's solution aka Selenium webdriver - Open a webpage

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://waitbutwhy.com/2015/01/artificial-intelligence-revolution-1.html")
s = driver.find_element_by_name("s")
s.send_keys("neuralink")
submit = driver.find_element_by_class_name("search-submit")
submit.click()
driver.close()