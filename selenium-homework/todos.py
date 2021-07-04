# 015.md hw's solution aka Selenium find elements (list)
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:9999/todo.html")

web_elements = driver.find_elements_by_class_name("done-false")

for web_element in web_elements:
    print(web_element.text)

driver.close()