# Необходимо разработать программу, которая проверяет, что все элементы
# вектора различны/одинаковы.


def search_unique_elements(num):
    for i in range(len(num) - 1):
        for j in range(i + 1, len(num)):
            if num[i] == num[j]:
                break

        return False if num[i] == num[j] else True


def main():
    numbers = int(input("Input amount of numbers : "))
    num = []
    for i in range(numbers):
        number = float(input("Input your number: "))
        num.append(number)

    msg = search_unique_elements(num)

    print(msg)


main()
