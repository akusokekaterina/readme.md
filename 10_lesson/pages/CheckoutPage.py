from .BasePage import BasePage, By


class CheckoutPage(BasePage):
    """Класс для работы со страницей оформления заказа Saucedemo."""
    
    # Локаторы
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON = (By.ID, "finish")
    CANCEL_BUTTON = (By.ID, "cancel")
    
    def fill_customer_info(self, first_name, last_name, postal_code):
        """
        Заполнение информации о покупателе.
        
        Args:
            first_name: Имя покупателя
            last_name: Фамилия покупателя
            postal_code: Почтовый индекс
        """
        self.enter_text(self.FIRST_NAME_FIELD, first_name)
        self.enter_text(self.LAST_NAME_FIELD, last_name)
        self.enter_text(self.POSTAL_CODE_FIELD, postal_code)
    
    def continue_checkout(self):
        """Переход к итоговой информации о заказе."""
        self.click_element(self.CONTINUE_BUTTON)
    
    def get_total_amount(self):
        """
        Получение итоговой суммы заказа.
        
        Returns:
            Итоговая сумма заказа в формате строки
        """
        total_text = self.get_element_text(self.TOTAL_LABEL)
        return total_text.split("$")[1]
    
    def finish_checkout(self):
        """Завершение оформления заказа."""
        self.click_element(self.FINISH_BUTTON)
    
    def cancel_checkout(self):
        """Отмена оформления заказа."""
        self.click_element(self.CANCEL_BUTTON)
    
    def is_order_complete(self):
        """
        Проверка завершения заказа.
        
        Returns:
            bool: True если заказ завершен, иначе False
        """
        try:
            complete_element = self.driver.find_element(
                By.CLASS_NAME, "complete-header"
            )
            return complete_element.is_displayed()
        except Exception:
            return False


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
    print("CheckoutPage class demonstration")
    print("Available methods:")
    methods = [
        method for method in dir(CheckoutPage) 
        if not method.startswith('_')
    ]
    for method in methods:
        print(f"- {method}()")
    
    print("\nAvailable severity levels:")
    for level in dir(SeverityLevel):
        if not level.startswith('_'):
            print(f"- {level}")
