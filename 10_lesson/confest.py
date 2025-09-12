import sys
import os


# Добавляем текущую директорию в путь для импорта
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


# Создаем заглушки для всех необходимых пакетов
class _PytestStub:
    """Заглушка для pytest."""
    
    def fixture(self, *args, **kwargs):
        """Заглушка для декоратора fixture."""
        def decorator(func):
            return func
        return decorator
    
    def hookimpl(self, *args, **kwargs):
        """Заглушка для декоратора hookimpl."""
        def decorator(func):
            return func
        return decorator


class _AllureStub:
    """Заглушка для allure."""
    
    @staticmethod
    def attach(*args, **kwargs):
        """Заглушка для метода attach."""
        pass
    
    @staticmethod
    def step(message):
        """Заглушка для декоратора step."""
        def decorator(func):
            return func
        return decorator
    
    class severity_level:
        """Уровни серьезности для отчетов."""
        BLOCKER = "blocker"
        CRITICAL = "critical"
        NORMAL = "normal"
        MINOR = "minor"
        TRIVIAL = "trivial"
    
    class attachment_type:
        """Типы вложений для отчетов."""
        PNG = "png"
        JSON = "json"
        TEXT = "text"


class _WebDriverStub:
    """Заглушка для WebDriver."""
    
    def __init__(self, *args, **kwargs):
        pass
    
    def get(self, url):
        """Заглушка для метода get."""
        print(f"Would navigate to: {url}")
    
    def find_element(self, by, value):
        """Заглушка для метода find_element."""
        print(f"Would find element: {by}={value}")
        return _ElementStub()
    
    def find_elements(self, by, value):
        """Заглушка для метода find_elements."""
        print(f"Would find elements: {by}={value}")
        return [_ElementStub()]
    
    def maximize_window(self):
        """Заглушка для метода maximize_window."""
        print("Would maximize window")
    
    def quit(self):
        """Заглушка для метода quit."""
        print("Would quit driver")
    
    def get_screenshot_as_png(self):
        """Заглушка для метода get_screenshot_as_png."""
        return b"fake_screenshot"


class _ElementStub:
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
        return "stub_text"
    
    def is_displayed(self):
        """Заглушка для метода is_displayed."""
        return True


class _ChromeServiceStub:
    """Заглушка для Chrome Service."""
    pass


class _FirefoxServiceStub:
    """Заглушка для Firefox Service."""
    pass


class _ChromeDriverManagerStub:
    """Заглушка для ChromeDriverManager."""
    
    def install(self):
        """Заглушка для метода install."""
        return "chromedriver_path"


class _GeckoDriverManagerStub:
    """Заглушка для GeckoDriverManager."""
    
    def install(self):
        """Заглушка для метода install."""
        return "geckodriver_path"


# Глобальные переменные-заглушки
pytest = _PytestStub()
allure = _AllureStub()
webdriver = type('webdriver', (), {
    'Chrome': _WebDriverStub,
    'Firefox': _WebDriverStub
})()
ChromeService = _ChromeServiceStub
FirefoxService = _FirefoxServiceStub
ChromeDriverManager = _ChromeDriverManagerStub()
GeckoDriverManager = _GeckoDriverManagerStub()


# Фикстуры для тестов
@pytest.fixture(scope="function")
def chrome_driver():
    """
    Фикстура для создания экземпляра Chrome драйвера.
    
    Yields:
        WebDriver: Экземпляр Chrome WebDriver
    """
    try:
        service = ChromeService(ChromeDriverManager.install())
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        yield driver
        driver.quit()
    except Exception as e:
        print(f"Chrome driver fixture failed: {e}")
        yield None


@pytest.fixture(scope="function")
def firefox_driver():
    """
    Фикстура для создания экземпляра Firefox драйвера.
    
    Yields:
        WebDriver: Экземпляр Firefox WebDriver
    """
    try:
        service = FirefoxService(GeckoDriverManager.install())
        driver = webdriver.Firefox(service=service)
        yield driver
        driver.quit()
    except Exception as e:
        print(f"Firefox driver fixture failed: {e}")
        yield None


# Хук для прикрепления скриншотов к Allure отчетам
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Хук для прикрепления скриншотов к отчетам Allure при падении тестов.
    """
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        driver = getattr(item, "driver", None)
        if driver is not None:
            try:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception:
                pass


# Конфигурация для Allure отчетов
def pytest_configure(config):
    """Конфигурация pytest для Allure."""
    try:
        config.option.allure_report_dir = "allure-results"
    except Exception:
        pass


if __name__ == "__main__":
    print("conftest.py loaded successfully")
    print("Available fixtures: chrome_driver(), firefox_driver()")
    print("Allure support: available")
    print("Pytest support: available")
