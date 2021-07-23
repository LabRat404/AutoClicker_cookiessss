from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")



cookie = driver.find_element_by_id("bigCookie")
cookie_con = driver.find_element_by_id("cookies")
actions = ActionChains(driver)
actions.click(cookie)

while(1):
    actions.perform()