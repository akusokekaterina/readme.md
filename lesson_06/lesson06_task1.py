from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

green_label = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
    )

print(green_label.text)

# Закрываем браузер
driver.quit()