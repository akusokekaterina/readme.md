import math
def square(a):
    return math.ceil(a * a)
num_a = int(input("Введите длину стороны: "))
print(f"Площадь квадрата: {square(num_a)}")