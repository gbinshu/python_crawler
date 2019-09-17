import json
import time

import redis
from selenium import webdriver

client = redis.StrictRedis()

driver = webdriver.Chrome()
url = ""
driver.get(url)

user = driver.find_element_by_xpath('//input[@name="username"]')
user.clear()
user.send_keys("username")

user = driver.find_element_by_xpath('//input[@name="password"]')
user.clear()
user.send_keys("password")

remember = driver.find_element_by_xpath('//input[@name="remember"]')
remember.click()

time.sleep(2)
cookies = driver.get_cookies()
client.lpush('cookies', json.dumps(cookies))
driver.quit()