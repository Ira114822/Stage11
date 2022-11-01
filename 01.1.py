# предыдущий таск, только используя цикл for


def find_max_number(num):
    max_num = num[0]
    for i in num:
        if i > max_num:
            max_num = i
    return max_num


def find_min_number(num):
    min_num = num[0]
    for i in num:
        if i < min_num:
            min_num = i
    return min_num


def find_arithmetical_mean(num):
    s = 0
    for element in num:
        s += element
    return round(s / len(num), 2)


def main():
    numbers = int(input("Input amount of numbers : "))
    num = []
    for i in range(numbers):
        number = float(input("Input your number: "))
        num.append(number)

    max_num = find_max_number(num)
    min_num = find_min_number(num)
    arith_mean = find_arithmetical_mean(num)

    msg = (f"You max number is {max_num}."
           f"\nYour min number is {min_num}."
           f"\nArithmetic mean of your numbers is {arith_mean}")

    print(msg)


main()
