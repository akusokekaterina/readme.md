from address import Address
from mailing import Mailing

# Создаем адреса
address_from = Address("123456", "Москва", "Ленина", 10, 5)
address_to = Address("654321", "Санкт-Петербург", "Пушкина", 20, 15)

# Создаем почтовое отправление
mail = Mailing(address_to, address_from, cost = 250, track = "ABC123456")

# Печатаем информацию об отправлении
print(mail)