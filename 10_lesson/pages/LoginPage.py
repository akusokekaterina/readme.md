from .BasePage import BasePage, By


class LoginPage(BasePage):
    """Класс для работы со страницей авторизации Saucedemo."""
    
    # Локаторы
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    
    def open(self, url="https://www.saucedemo.com/"):
        """
        Открытие страницы авторизации.
        
        Args:
            url: URL страницы авторизации
            
        Returns:
            self: Экземпляр LoginPage
        """
        self.driver.get(url)
        return self
    
    def login(self, username, password):
        """
        Выполнение авторизации.
        
        Args:
            username: Логин пользователя
            password: Пароль пользователя
        """
        self.enter_text(self.USERNAME_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click_element(self.LOGIN_BUTTON)
    
    def get_error_message(self):
        """
        Получение текста сообщения об ошибке.
        
        Returns:
            Текст сообщения об ошибке
        """
        return self.get_element_text(self.ERROR_MESSAGE)
    
    def is_login_successful(self):
        """
        Проверка успешности авторизации.
        
        Returns:
            bool: True если авторизация успешна, иначе False
        """
        try:
            # Проверяем, что мы на странице продуктов после логина
            products_title = self.driver.find_element(
                By.CLASS_NAME, "title"
            )
            return "Products" in products_title.text
        except Exception:
            return False
    
    def clear_login_fields(self):
        """Очистка полей логина и пароля."""
        self.enter_text(self.USERNAME_FIELD, "")
        self.enter_text(self.PASSWORD_FIELD, "")


# Заглушки для Allure
def allure_step(message):
    """Заглушка для декоратора allure.step."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Allure Step: {message}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


def allure_feature(feature_name):
    """Заглушка для декоратора allure.feature."""
    def decorator(cls):
        print(f"Allure Feature: {feature_name}")
        return cls
    return decorator


def allure_severity(severity_level):
    """Заглушка для декоратора allure.severity."""
    def decorator(func):
        print(f"Allure Severity: {severity_level}")
        return func
    return decorator


# Константы для уровней серьезности Allure
class SeverityLevel:
    """Уровни серьезности для Allure отчетов."""
    BLOCKER = "blocker"
    CRITICAL = "critical"
    NORMAL = "normal"
    MINOR = "minor"
    TRIVIAL = "trivial"


# Пример использования
if __name__ == "__main__":
    print("LoginPage class demonstration")
    print("Available methods:")
    methods = [
        method for method in dir(LoginPage) 
        if not method.startswith('_')
    ]
    for method in methods:
        print(f"- {method}()")
    
    print("\nAvailable locators:")
    locators = [
        attr for attr in dir(LoginPage) 
        if attr.isupper() and not attr.startswith('_')
    ]
    for locator in locators:
        print(f"- {locator}")
