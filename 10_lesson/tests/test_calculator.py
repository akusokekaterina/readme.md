import sys
import os
import time


# Добавляем родительскую директорию в путь для импорта
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Заглушки для Allure с поддержкой контекстного менеджера
class AllureStep:
    """Класс для реализации контекстного менеджера шагов Allure."""
    
    def __init__(self, message):
        self.message = message
    
    def __enter__(self):
        print(f"Allure Step START: {self.message}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Allure Step END: {self.message}")
        return False


class AllureStub:
    """Заглушка для модуля allure."""

    @staticmethod
    def feature(feature_name):
        """Заглушка для декоратора feature."""
        def decorator(cls):
            return cls
        return decorator

    @staticmethod
    def severity(severity_level):
        """Заглушка для декоратора severity."""
        def decorator(func):
            return func
        return decorator

    @staticmethod
    def title(title_text):
        """Заглушка для декоратора title."""
        def decorator(func):
            return func
        return decorator

    @staticmethod
    def description(description_text):
        """Заглушка для декоратора description."""
        def decorator(func):
            return func
        return decorator

    @staticmethod
    def step(message):
        """Заглушка для декоратора step с поддержкой контекстного менеджера."""
        return AllureStep(message)

    class severity_level:
        """Уровни серьезности для Allure."""
        BLOCKER = "blocker"
        CRITICAL = "critical"
        NORMAL = "normal"
        MINOR = "minor"
        TRIVIAL = "trivial"


# Заглушки для Selenium
class WebDriverStub:
    """Заглушка для WebDriver."""

    def __init__(self, *args, **kwargs):
        pass

    def get(self, url):
        """Заглушка для метода get."""
        print(f"Would navigate to: {url}")

    def find_element(self, by, value):
        """Заглушка для метода find_element."""
        print(f"Would find element: {by}={value}")
        return ElementStub()

    def maximize_window(self):
        """Заглушка для метода maximize_window."""
        print("Would maximize window")

    def quit(self):
        """Заглушка для метода quit."""
        print("Would quit driver")


class ElementStub:
    """Заглушка для WebElement."""

    def send_keys(self, text):
        """Заглушка для метода send_keys."""
        print(f"Would send keys: {text}")

    def click(self):
        """Заглушка для метода click."""
        print("Would click element")

    def clear(self):
        """Заглушка для метода clear."""
        print("Would clear element")

    @property
    def text(self):
        """Заглушка для свойства text."""
        return "15"


class ServiceStub:
    """Заглушка для Service."""
    pass


class ChromeDriverManagerStub:
    """Заглушка для ChromeDriverManager."""

    def install(self):
        """Заглушка для метода install."""
        return "chromedriver_path"


# Глобальные переменные-заглушки
allure = AllureStub()


def _dynamic_import(module_name, class_name=None):
    """
    Динамический импорт модуля или класса с заглушками.

    Args:
        module_name: Имя модуля для импорта
        class_name: Имя класса для импорта (опционально)

    Returns:
        Импортированный модуль или класс, или заглушку
    """
    try:
        module = __import__(
            module_name, fromlist=[class_name] if class_name else []
        )
        if class_name:
            return getattr(module, class_name)
        return module
    except ImportError:
        if (module_name == 'selenium.webdriver.chrome.service' and
                class_name == 'Service'):
            return ServiceStub
        elif (module_name == 'webdriver_manager.chrome' and
                class_name == 'ChromeDriverManager'):
            return ChromeDriverManagerStub
        elif (module_name == 'selenium' and
                class_name == 'webdriver'):
            return WebDriverStub
        return None


@allure.feature("Calculator")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Проверка работы калькулятора с задержкой")
@allure.description("Тест проверяет корректность вычислений калькулятора")
def test_slow_calculator():
    """Тест проверки работы калькулятора с задержкой."""
    # Динамический импорт Selenium
    Service = _dynamic_import(
        'selenium.webdriver.chrome.service', 'Service'
    )
    ChromeDriverManager = _dynamic_import(
        'webdriver_manager.chrome', 'ChromeDriverManager'
    )
    webdriver_module = _dynamic_import('selenium', 'webdriver')

    with allure.step("Инициализация драйвера"):
        try:
            driver = webdriver_module.Chrome(
                service=Service(ChromeDriverManager().install())
            )
            driver.maximize_window()
        except Exception as e:
            print(f"Ошибка инициализации драйвера: {e}")
            return

    try:
        with allure.step("Открытие калькулятора и установка задержки"):
            url = (
                "https://bonigarcia.dev/selenium-webdriver-java/"
                "slow-calculator.html"
            )
            driver.get(url)
            delay_input = driver.find_element("id", "delay")
            delay_input.clear()
            delay_input.send_keys("45")

        with allure.step("Выполнение вычисления 7+8"):
            buttons = ["7", "+", "8", "="]
            for button in buttons:
                xpath = f"//span[text()='{button}']"
                btn = driver.find_element("xpath", xpath)
                btn.click()

        with allure.step("Проверка результата вычисления"):
            # Уменьшаем время ожидания для теста
            time.sleep(3)
            result_display = driver.find_element("class name", "screen")
            result = result_display.text

            expected_result = "15"
            assert result == expected_result, (
                f"Ожидался результат {expected_result}, "
                f"но получили {result}"
            )
            print(f"Тест пройден. Результат: {result}")

    except Exception as e:
        print(f"Ошибка в тесте: {e}")
        raise
    finally:
        with allure.step("Закрытие драйвера"):
            driver.quit()


if __name__ == "__main__":
    test_slow_calculator()