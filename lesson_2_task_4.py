n = int(input("Введите число:"))
def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print(f"{i} -FizzBuzz")
        elif i % 5 == 0:
            print(f"{i} -Buzz")
        elif i % 3 == 0:
            print(f"{i} -Fizz")
        else:
            print(i)
fizz_buzz(n)