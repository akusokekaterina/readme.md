import time


class By:
    """Константы для типов локаторов (аналог selenium.webdriver.common.by.By)."""
    
    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"


class BasePage:
    """Базовый класс для всех страниц, содержащий общие методы."""
    
    def __init__(self, driver):
        """
        Инициализация базовой страницы.
        
        Args:
            driver: Экземпляр веб-драйвера
        """
        self.driver = driver
        self.wait_timeout = 10
    
    def _simple_wait(self, condition, timeout=None):
        """
        Простая реализация ожидания условия.
        
        Args:
            condition: Функция-условие, которая возвращает элемент или None
            timeout: Время ожидания в секундах
            
        Returns:
            Найденный элемент
            
        Raises:
            TimeoutError: Если элемент не найден в течение timeout
        """
        if timeout is None:
            timeout = self.wait_timeout
        
        end_time = time.time() + timeout
        while time.time() < end_time:
            try:
                result = condition()
                if result:
                    return result
            except Exception:
                pass
            time.sleep(0.1)
        raise TimeoutError(f"Element not found within {timeout} seconds")
    
    def find_element(self, locator):
        """
        Поиск элемента на странице.
        
        Args:
            locator: Кортеж (By, значение) для поиска элемента
            
        Returns:
            Найденный элемент WebElement
        """
        def condition():
            try:
                element = self.driver.find_element(*locator)
                return element if element.is_displayed() else None
            except Exception:
                return None
        
        return self._simple_wait(condition)
    
    def click_element(self, locator):
        """
        Клик по элементу на странице.
        
        Args:
            locator: Кортеж (By, значение) для поиска элемента
        """
        element = self.find_element(locator)
        element.click()
    
    def enter_text(self, locator, text):
        """
        Ввод текста в поле.
        
        Args:
            locator: Кортеж (By, значение) для поиска элемента
            text: Текст для ввода
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_element_text(self, locator):
        """
        Получение текста элемента.
        
        Args:
            locator: Кортеж (By, значение) для поиска элемента
            
        Returns:
            Текст элемента
        """
        element = self.find_element(locator)
        return element.text
    
    def wait_for_element_visible(self, locator, timeout=10):
        """
        Ожидание видимости элемента.
        
        Args:
            locator: Кортеж (By, значение) для поиска элемента
            timeout: Время ожидания в секундах
            
        Returns:
            Видимый элемент WebElement
        """
        return self.find_element(locator)
    
    def wait_seconds(self, seconds):
        """
        Ожидание указанного количества секунд.
        
        Args:
            seconds: Количество секунд для ожидания
        """
        time.sleep(seconds)

    # Заглушки для совместимости (если allure не установлен)
    @staticmethod
    def step(message):
        """Заглушка для allure.step."""
        def decorator(func):
            def wrapper(*args, **kwargs):
                print(f"Step: {message}")
                return func(*args, **kwargs)
            return wrapper
        return decorator


# Пример использования класса By для удобства
if __name__ == "__main__":
    # Демонстрация использования констант By
    print("Available locator types:")
    for attr in dir(By):
        if not attr.startswith('_'):
            print(f"By.{attr} = {getattr(By, attr)}")
