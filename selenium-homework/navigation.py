# 017.md hw's solution aka Selenium webdriver - Navigation

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://localhost:9999/general.html")
list_of_links = driver.find_elements_by_xpath("//a")
print("Sum of links: " + str(len(list_of_links)))

i = 0
try:
    for link in list_of_links:
        print(i)
        driver.execute_script("document.getElementsByTagName('a')[" + str(i) + "].removeAttribute('target');")
        i += 1
        time.sleep(0.2)
        #link.click()
        driver.get(link.get_attribute("href"))
        time.sleep(1)
        # A _blank-ot ugyan eltávolítja a hack, de a külsős url navigálással nem tud mit kezdeni, később visszatérek rá.
        ''' '''
        if driver.current_url == link.get_attribute("href"):
            print("OK")
            print(driver.current_url)
            print(link.get_attribute("href"))
        else:
            print("Different URLs!")
            break

        driver.back()
#except:
#    print("Error!")
finally:
    driver.close()
