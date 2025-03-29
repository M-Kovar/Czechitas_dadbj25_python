# 1. Součet čísel v seznamu

numbers = [23, 4, -8, 16, 15, -42]
numbers_sum = 0

for number in numbers:
    # numbers_sum = numbers_sum + number
    numbers_sum += number

print(numbers_sum)
# print(sum(numbers))


# 2. Káva

coffee_list = [
    ["Espresso", 63],
    ["Americano", 95],
    ["Latte", 75],
    ["Cold Brew", 200],
    ["Cappuccino", 80]
]

for coffee in coffee_list:
    name = coffee[0]
    caffeine_amount = coffee[1]

    if caffeine_amount < 90:
        print(f"{name} obsahuje {caffeine_amount} mg kofeinu")


# 3. Sudá čísla

numbers = [23, 4, -8, 16, 15, -42]

print("V seznamu jsou následující sudá čísla:")

for number in numbers:
    if number % 2 == 0:
        print(number)