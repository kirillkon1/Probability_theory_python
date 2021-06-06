import math
from prettytable import PrettyTable
from collections import Counter

from Number_class import *

digits_list = [-0.76, -0.55, -0.62, 0.21, -1.31, 0.64, -0.21, -1.07, 0.21, 1.16,
               -1.14, 1.07, -0.14, -1.45, 1.45, 0.24, 1.46, 1.04, -0.31, -1.12]


digits_set = set(digits_list)

if __name__ == '__main__':

    print(f"Выборка: {digits_list}")
    # ------ вариационный ряд -------
    digits_list.sort()
    variation_range = digits_list
    print(f"\nВариационный ряд : {variation_range}")

    # ----- экстремальные значения -----
    # -----  (максимум и минимум)  -----
    minimum = min(digits_list)
    maximum = max(digits_list)
    print(f"min = {minimum}, max = {maximum}")

    # --- Размах выборки ----

    R = maximum - minimum

    print(f"Размах = {R}")

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

    dispersion = math_sqr_expectation - math_expectation ** 2  # M(x^2) - M(x)^2
    standard_deviation = math.sqrt(dispersion)

    print(f"Математическое ожидание = {toFixed(math_expectation)}\n"
          f"Дисперсия = {toFixed(dispersion)}\n"
          f"СКО = {toFixed(standard_deviation)}\n")

    drawFunction(getEmpiricalFunction(number_list, True), "график эмпирической функции распределения")

    # --- Гистограмма ---

    # Формула Стерджеса
    h = float(toFixed((maximum - minimum) / (1 + math.log(len(number_list), 2))))

    x = minimum - h / 2
    border_list = []

    while x <= maximum:
        border_list.append(float(toFixed(x)))
        x += h
    else:
        border_list.append(float(toFixed(x)))
    preGraphList = preGraphFunction(digits_list, border_list)
    counter = Counter(preGraphList)

    border_list_index = []
    border_list_result = []

    table = PrettyTable()
    for i in range(len(border_list) - 1):
        border_list_index.append(f"[{border_list[i]};{border_list[i + 1]})")
        border_list_result.append(counter[border_list[i]])


    table = PrettyTable()

    table.field_names = border_list_index
    table.add_row(border_list_result)

    print(f'Интервальный ряд с шагом {h}')
    print(table)
    for i in range(len(border_list_result)):
        border_list_result[i] = border_list_result[i] / len(digits_list)

    drawBarGraph(border_list_index, border_list_result)



    drawFunction(getPointForStaticGraphic(border_list, border_list_result, h), "полигон приведенных частот")
