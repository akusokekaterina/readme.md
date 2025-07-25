from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

driver.maximize_window()
driver.get("http://uitestingplayground.com/classattr")

for i in range(5):
    button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()

# Ждем 25 секунд, чтобы видеть результат клика
sleep(25)