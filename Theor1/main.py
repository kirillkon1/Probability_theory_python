import math
from collections import Counter

from Number_class import NumberWithProbability, printTable, toFixed, drawFunction, getPointForStaticGraphic, \
    getEmpiricalFunction, preGraphFunction, drawBarGraph

digits_list = [-0.76, -0.55, -0.62, 0.21, -1.31, 0.64, -0.21, -1.07, 0.21, 1.16,
               -1.14, 1.07, -0.14, -1.45, 1.45, 0.24, 1.46, 1.04, -0.31, -1.12]

# digits_list = [-0.76, -0.55, -0.62, 0.21, -1.31, 0.64, -0.21, -1.07, 0.21, 1.16,
#                -1.14, 1.07, -0.14, -1.45, 1.45, 0.24, 1.46, 1.04, -0.31, -1.12,
#                1.13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

digits_set = set(digits_list)


def print_mas(l: list):
    for i in l:
        print(i)


if __name__ == '__main__':
    # ------ вариационный ряд -------
    digits_list.sort()
    variation_range = digits_list
    print(f"\nВариационный рад : {variation_range}")

    # ----- экстремальные значения -----
    # -----  (максимум и минимум)  -----
    minimum = min(digits_list)
    maximum = max(digits_list)
    print(f"min = {minimum}, max = {maximum}")

    # --- Размах выборки ----

    R = maximum - minimum

    # --- Эмпирическая фун-ция распределения ---
    counter = Counter(digits_list)
    number_list = []
    for digit in digits_set:
        number_list.append(
            NumberWithProbability(digit, counter[digit], float(toFixed(counter[digit] / len(digits_list)))))
    number_list = sorted(number_list, key=lambda x: x.number)

    printTable(number_list)

    math_expectation = 0  # M(x)
    math_sqr_expectation = 0  # M(x^2)
    for NUMBER in number_list:
        math_expectation = math_expectation + NUMBER.number * NUMBER.probability
        math_sqr_expectation = math_sqr_expectation + NUMBER.number ** 2 * NUMBER.probability

    dispersion = math_sqr_expectation - math_expectation ** 2  # M(x^2) - M(x)
    standard_deviation = math.sqrt(dispersion)

    drawFunction(getPointForStaticGraphic(number_list), "полигон приведенных частот")
    drawFunction(getEmpiricalFunction(number_list, False), "график эмпирической фукнции распределения")

    # --- Гистограмма ---
    h = float(toFixed((maximum - minimum) / (1 + math.log(len(number_list), 2))))

    x = minimum - h / 2
    bbb = []
    print(h)
    while x <= maximum:
        bbb.append(x)
        x += h
    else:
        bbb.append(x)
    preGraphList = preGraphFunction(digits_list, bbb)

    drawBarGraph(digits_list, bbb)
