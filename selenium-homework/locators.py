# 013.md hw's solution aka Selenium with locators (XPath)
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:9999/kitchensink.html")

find_ID = driver.find_element_by_id("opentab")
find_NAME = driver.find_element_by_name("cars")
find_XPath = driver.find_element_by_xpath('//*[@id="product"]/tbody/tr[2]/td[2]')
print(find_ID.text)
print(find_NAME.get_attribute("value"))
print(find_XPath.text)
