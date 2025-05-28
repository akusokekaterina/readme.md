from adress import Adress
class Mailing:
    def __init__(self, to_adress, from_adress, cost, track):
        self.to_adress = to_adress
        self.from_adress = from_adress
        self.cost = cost
        self.track = track
    def __str__(self):
        return (f"Отправление {self.track} из {self.to_adress} "
                f"в {self.from_adress}. Стоимость {self.cost} рублей.")