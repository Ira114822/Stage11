# Написать программу, которая подсчитывает количество только чётных/нечёт-
# ных элементов вектора.


def calculate_even_numbers(num):
    count = 0
    for i in num:
        if i % 2 == 0:
            count += 1
    return count


def main():
    numbers = int(input("Input amount of numbers : "))
    num = []
    for i in range(numbers):
        number = float(input("Input your number: "))
        num.append(number)

    msg = f"You have {calculate_even_numbers(num)} even numbers"

    print(msg)


main()
