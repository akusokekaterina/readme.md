from adress import Adress
from mailing import Mailing
adress_from = Adress("123456", "Москва", "Ленина", 10, 5)
adress_to = Adress("654321", "Санкт-Петербург", "Пушкина", 20, 15)

# Создаем почтовое отправление
mailing = Mailing(adress_to, adress_from, cost=250, track="ABC123456")

# Печатаем информацию об отправлении
print(mailing)