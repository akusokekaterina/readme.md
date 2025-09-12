from .BasePage import BasePage, By


class CalcPage(BasePage):
    """Класс для работы с калькулятором."""
    
    # Локаторы
    DELAY_INPUT = (By.ID, "delay")
    CALC_BUTTON = (By.XPATH, "//span[text()='{button}']")
    RESULT_DISPLAY = (By.CLASS_NAME, "screen")
    
    def open(self, url="https://example.com/calculator"):
        """
        Открытие страницы калькулятора.
        
        Args:
            url: URL страницы калькулятора
            
        Returns:
            self: Экземпляр CalcPage
        """
        self.driver.get(url)
        return self
    
    def set_delay(self, delay):
        """
        Установка задержки вычислений.
        
        Args:
            delay: Задержка в секундах
        """
        self.enter_text(self.DELAY_INPUT, str(delay))
    
    def calculate(self, expression):
        """
        Выполнение вычисления.
        
        Args:
            expression: Выражение для вычисления
        """
        for char in expression:
            button_locator = (
                self.CALC_BUTTON[0],
                self.CALC_BUTTON[1].format(button=char)
            )
            self.click_element(button_locator)
    
    def get_result(self, timeout=10):
        """
        Получение результата вычисления.
        
        Args:
            timeout: Время ожидания в секундах
            
        Returns:
            Результат вычисления
        """
        result_element = self.wait_for_element_visible(
            self.RESULT_DISPLAY, timeout
        )
        return result_element.text


# Заглушки для совместимости (если allure не установлен)
def allure_step(message):
    """Заглушка для allure.step."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Step: {message}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


# Пример использования
if __name__ == "__main__":
    print("CalcPage class demonstration")
    print("Available methods:")
    methods = [method for method in dir(CalcPage) if not method.startswith('_')]
    for method in methods:
        print(f"- {method}()")
