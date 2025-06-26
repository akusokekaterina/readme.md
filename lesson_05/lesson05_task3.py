from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/inputs")
input_box = driver.find_element(By.TAG_NAME, "input")
input_box.send_keys("Sky")
input_box.clear()
input_box.send_keys("Pro")
sleep(10)
driver.quit()