# Необходимо написать программу, которая обрабатывает результаты экзамена.


def calculate_marks(num):
    fives = 0
    fours = 0
    triplets = 0
    deuces = 0
    units = 0
    zeros = 0

    for i in num:

        if i < 0 or i > 5:
            return -1

        if i == 0:
            zeros += 1

        elif i == 1:
            units += 1

        elif i == 2:
            deuces += 1

        elif i == 3:
            triplets += 1

        elif i == 4:
            fours += 1

        else:
            fives += 1

    return zeros, units, deuces, triplets, fours, fives


def calculate_percent(num, zeros, units, deuces, triplets, fours, fives):
    percent_fives = fives * 100 / len(num)
    percent_fours = fours * 100 / len(num)
    percent_triplets = triplets * 100 / len(num)
    percent_deuces = deuces * 100 / len(num)
    percent_units = units * 100 / len(num)
    percent_zeros = zeros * 100 / len(num)

    return (f"Exam Result:\nfives - {round(percent_fives, 2)}%({fives})\nfours - {round(percent_fours, 2)}%({fours})"
            f"\ntriplets - {round(percent_triplets, 2)}%({triplets})\ndeuces - {round(percent_deuces, 2)}%({deuces})"
            f"\nunits - {round(percent_units, 2)}%({units})\nzeros - {round(percent_zeros, 2)}%({zeros}) ")


def main():
    numbers = int(input("Input amount of numbers : "))
    num = []
    for i in range(numbers):
        number = int(input("Input your number: "))
        num.append(number)

    zeros, units, deuces, triplets, fours, fives = calculate_marks(num)

    msg = (f"Exam Result Handling\nMarks: {str(num).strip('[]')}"
           f"\n{calculate_percent(num, zeros, units, deuces, triplets, fours, fives)}")

    print(msg)


main()
