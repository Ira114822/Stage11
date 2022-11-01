# разработать программу, которая проверяет, что все элементы
# вектора находятся в упорядоченном виде, т.е. отсортированы по возрастанию


def sequence_search(num):
     num2 = sorted(num)
     return True if num == num2 else False


def main():
    numbers = int(input("Input amount of numbers : "))
    num = []
    for i in range(numbers):
        number = float(input("Input your number: "))
        num.append(number)

    print(num) #debug

    msg = f"Result: {sequence_search(num)}"

    print(msg)


main()
