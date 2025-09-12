class ProductsPage:
    """Класс для работы со страницей товаров Saucedemo."""

    def __init__(self, driver):
        """
        Инициализация страницы товаров.
        Args:
            driver: WebDriver instance
        """
        self.driver = driver

    def add_product_to_cart(self, product_name):
        """
        Добавление товара в корзину по названию.
        Args:
            product_name (str): Название товара для добавления в корзину
        """
        # Простая реализация без сложных локаторов
        xpath = f"//div[text()='{product_name}']/ancestor::div[contains(@class, 'inventory_item')]//button"
        add_button = self.driver.find_element("xpath", xpath)
        add_button.click()

    def go_to_cart(self):
        """Переход на страницу корзины."""
        cart_link = self.driver.find_element("class name", "shopping_cart_link")
        cart_link.click()

    def get_cart_count(self):
        """
        Получение количества товаров в корзине.  
        Returns:
            int: Количество товаров в корзине  """
        try:
            cart_badge = self.driver.find_element(
                "class name", "shopping_cart_badge")
            return int(cart_badge.text)
        except:
            return 0
