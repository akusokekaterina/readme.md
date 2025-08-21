from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.CalcPage import CalcPage


def test_slow_calculator():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    try:
        calculator = CalcPage(driver)
        calculator.open().set_delay(45)
        calculator.calculate("7+8=")
        result = calculator.get_result(46)

        assert result == "15", f"Ожидался результат 15, но получили {result}"

    finally:
        driver.quit()


if __name__ == "__main__":
    test_slow_calculator()
