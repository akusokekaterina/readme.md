from smartphone import Smartphone
catalog = [
    Smartphone("Redmi", "A3x", "+79640849785"),
    Smartphone("Samsung", "L12", "+79865434556"),
    Smartphone("Nokia", "I90", "+79678656437"),
    Smartphone("Huawei", "009", "+79067458236"),
    Smartphone("aiPhone", "10", "+79456790875")
]
for smartphone in catalog:
    print(f"{smartphone.marka} - {smartphone.model}. {smartphone.num}")