# 008.md hw's solution aka Selenium webdriver - Use a non existent id (try-except)

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://waitbutwhy.com/2015/01/artificial-intelligence-revolution-1.html")
non_existent_id = "nemletezik"

try:
    non_existent = driver.find_element_by_id(non_existent_id)
except:
    driver.close()
    print("An exception occurred! The " + non_existent_id + " isn't a valid ID name. Try again...")
