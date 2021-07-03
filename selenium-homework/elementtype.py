# 010.md hw's solution aka Selenium with findby cases
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:9999/trickyelements.html")

first_btn = driver.find_element_by_tag_name("button")
first_btn_id = first_btn.get_attribute("id")
first_btn.click()
result = driver.find_element_by_id("result").text
if result == first_btn_id + " was clicked":
    print("Well done, " + result + "!")
else:
    print("Button not found!")

