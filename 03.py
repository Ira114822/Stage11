# Необходимо разработать программу, которая проверяет, что все элементы
# вектора расположены в зеркальном виде относительно его середины.


def find_middle(num):
    middle = len(num) // 2

    if len(num) % 2 == 0:
        ls1 = num[:middle]
        ls2 = num[middle:]

    else:
        ls1 = num[:middle]
        ls2 = num[middle + 1:]

    return True if ls1 == ls2[::-1] else False


def main():
    numbers = int(input("Input amount of numbers : "))
    num = []
    for i in range(numbers):
        number = int(input("Input your number: "))
        num.append(number)
    msg = f"{find_middle(num)}"

    print(msg)


main()
