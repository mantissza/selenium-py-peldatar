from selenium import webdriver

driver = webdriver.Chrome()
''' Multiline comment
driver.get("https://python.org")
q = driver.find_element_by_name("q")
q.send_keys("input")
submit = driver.find_element_by_name("submit")
submit.click()
driver.close() # Bezárja az ablakot
'''
driver.get("http://localhost:9999/filltablewithsum.html")


def add(p, q, pr):
    product = driver.find_element_by_id("product")
    quantity = driver.find_element_by_id("quantity")
    price = driver.find_element_by_id("price")
    add_button = driver.find_element_by_id("add")

    product.clear()
    quantity.clear()
    price.clear()

    product.send_keys(p)
    quantity.send_keys(q)
    price.send_keys(pr)
    add_button.click()


add("Ford", 1, 120000)
add("Tesla", 3, 12000000)
