# 017.md hw's solution aka Selenium webdriver - Navigation

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://localhost:9999/general.html")
list_of_links = driver.find_elements_by_xpath("//a")
print("Sum of links: " + str(len(list_of_links)))


def navigate_to_general():
    driver.get("http://localhost:9999/general.html")


print(list_of_links[9].get_attribute("href"))


i = 0
try:
    for link in list_of_links:
        print(i)
        if link.get_attribute('target'):
            print("x")
            driver.execute_script("document.getElementsByTagName('a')[" + str(i) + "].removeAttribute('target');")
        i += 1
        time.sleep(0.2)
        print(link.text)
        attr = link.get_attribute("href")  # Before navigate
        link.click()
        curr = driver.current_url  # After navigate
        #driver.get(link.get_attribute("href"))
        time.sleep(0.2)
        # A _blank-ot ugyan eltávolítja a hack, de a külsős url navigálással nem tud mit kezdeni, később visszatérek rá.
        ''' '''
        if curr == attr:
            print("OK")
            print(curr)
            print(attr)

        else:
            print("Different URLs!")
            print(curr)
            print(attr)

        driver.back()

        #driver.get("http://localhost:9999/general.html")
except:
    print("Error!")
finally:
    driver.close()
