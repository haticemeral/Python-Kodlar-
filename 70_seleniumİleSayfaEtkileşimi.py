from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge()
url = "http://github.com"

# searchInput = driver.find_elements_by_name("q")
# time.sleep(1)
# searchInput.send_keys("python")
# time.sleep(2)
# searchInput.send_keys(Keys.ENTER)
# time.sleep(2)
# result = driver.page_source
# print(result)
# result = driver.find_element_by_selector(".repo-list-item h3 a")
# for element in result:
#     print(element.text)

searchInput = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div/div[2]/div/div/qbsearch-input/div[1]/button")
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)


driver.close()
