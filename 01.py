# Дана некоторая последовательность вещественных чисел. Необходимо напи-
# сать приложение, которое эффективным способом:
#  находит экстремальные элементы заданной последовательности (наиболь-
# ший и наименьший элементы последовательности, а также среднеарифме-
# тическое);
#  подсчитывает количество положительных, отрицательных и равных нулю
# элементов последовательности;
#  меняет местами экстремальные элементы (если их несколько, то пер-
# вые/последние из найденных элементов последовательности).


def find_max_number(num):
    return max(num)


def find_min_number(num):
    return min(num)


def find_arithmetical_mean(num):
    return round(sum(num) / len(num), 2)


def calculate_positive_negative_zero_number(num):
    p = 0  # p - positive
    n = 0  # n - negative
    z = 0  # z - zero
    for i in num:
        if i > 0:
            p += 1
        elif i < 0:
            n += 1
        else:
            z += 1
    return f"In your list {p} positive, {n} negative and {z} zero numbers."

def replacing_max_min_elements(num):
    max_num = max(num)
    min_num = min(num)

    for i in range(len(num)):
        if num[i] == max_num:
            num[i] = min_num
        elif num[i] == min_num:
            num[i] = max_num

    return num


def main():
    numbers = int(input("Input amount of numbers : "))
    num = []
    for i in range(numbers):
        number = float(input("Input your number: "))
        num.append(number)

    max_num = find_max_number(num)
    min_num = find_min_number(num)
    arith_mean = find_arithmetical_mean(num)
    calculate_numbers = calculate_positive_negative_zero_number(num)

    msg = (f"You max number is {max_num}.\nYour min number is {min_num}."
           f"\nArithmetic mean of your numbers is {arith_mean}."
           f"\n{calculate_numbers}"
           f"\nModified list: {replacing_max_min_elements(num)}")

    print(msg)

main()
