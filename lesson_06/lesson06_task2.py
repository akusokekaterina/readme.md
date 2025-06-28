from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("http://uitestingplayground.com/textinput")

element = driver.find_element(By.CSS_SELECTOR,"#newButtonName") #нашли элемент
element.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR,"button.btn.btn-primary").click()

WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#updatingButton"), "SkyPro"))

button = driver.find_element(By.CSS_SELECTOR,"#updatingButton")
print(button.text)

driver.quit()