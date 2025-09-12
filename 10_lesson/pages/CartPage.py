from .BasePage import BasePage, By


class CartPage(BasePage):
    """Класс для работы со страницей корзины Saucedemo."""
    
    # Локаторы
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    
    def proceed_to_checkout(self):
        """Переход на страницу оформления заказа."""
        self.click_element(self.CHECKOUT_BUTTON)
    
    def get_cart_items_count(self):
        """
        Получение количества товаров в корзине.
        
        Returns:
            int: Количество товаров в корзине
        """
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)
    
    def continue_shopping(self):
        """Продолжение покупок (возврат к товарам)."""
        self.click_element(self.CONTINUE_SHOPPING)
    
    def remove_item_from_cart(self, item_name):
        """
        Удаление товара из корзины по названию.
        
        Args:
            item_name: Название товара для удаления
        """
        xpath = f"//div[text()='{item_name}']/ancestor::div[@class='cart_item']//button"
        remove_button = self.driver.find_element(By.XPATH, xpath)
        remove_button.click()


# Заглушка для allure.step
def step(message):
    """Заглушка для декоратора allure.step."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Step: {message}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


# Пример использования
if __name__ == "__main__":
    print("CartPage class demonstration")
    print("Available methods:")
    methods = [method for method in dir(CartPage) if not method.startswith('_')]
    for method in methods:
        print(f"- {method}()")
