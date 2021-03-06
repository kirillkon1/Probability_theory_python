import matplotlib.pyplot as plt

'''Класс, в котором хранятся число (из ряда),
 кол-во в ряде и его вероятность в выборке'''


class NumberWithProbability():
    def __init__(self, number, count, probability) -> None:
        super().__init__()
        self.number = number
        self.count = count
        self.probability = probability

    def __str__(self):
        return f"{self.number} | {self.count} | {self.probability}"


# Вывод таблицы со стат. рядом
def printTable(l: list):
    length = len(l) * 8
    print("\n", "".center(length, '='), '\n', " Таблица распределения ".center(length, '='), '\n',
          "".center(length, '='), '\n')
    print(*[f"-------" for x in l])
    print("|", end='')
    print(*[f"{x.number:>5} |" for x in l])
    print(*[f"-------" for x in l])
    print("|", end='')
    print(*[f"{x.probability:>5} |" for x in l])
    print(*[f"-------" for x in l])
    print('\n')


# Массив точек для постройки графика эмпирической функции распределения
# flag = True - отображение эмп. фун-ции в консоль
def getEmpiricalFunction(nums: list, flag=False):
    __probability = 0
    point_list = []
    tmp = '-'
    tmp1 = 0

    point_list.append([nums[0].number - 0.5, 0])

    for i in nums:
        if flag:

            if tmp == '-':
                print(f"{toFixed(__probability)}, x ≤ {i.number}")
            else:
                print(f"{toFixed(__probability)}, {tmp} < x ≤ {i.number}".center(15, " "))
            tmp = i.number

        point_list.append([i.number, tmp1])
        __probability = __probability + i.probability
        point_list.append([i.number, __probability])
        tmp1 = __probability

    if flag:
        print(f"   {1}, x > {nums[len(nums) - 1].number}")

    point_list.append([nums[len(nums) - 1].number + 0.5, tmp1])

    return point_list


# Массив точек для постройки графика статического распределения
def getPointForStaticGraphic(border_list: list, result_list: list, h) -> list:
    point_list = []

    for i in range(len(border_list) - 1):
        point_list.append([border_list[i] + h/2, result_list[i]])

    # print("тттт",point_list)
    return point_list


# рисует график по точкам
def drawFunction(points: list, tittle=None):
    x_axis = []
    y_axis = []

    for i in points:
        x_axis.append(i[0])
        y_axis.append(i[1])

    plt.title(tittle)
    plt.grid()
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    plt.plot(x_axis, y_axis)
    plt.show()


# Нарисовать гистограмму
def drawBarGraph(graph_list_index: list, graph_list_result: list) -> None:
    # plt.hist(graph_list, border, density=True)

    plt.bar(graph_list_index, graph_list_result)
    plt.ylabel('Probability p(x)')
    plt.xlabel('x')
    plt.rcParams['font.size'] = '5'
    plt.show()


# Границы для гистограммы
def preGraphFunction(nums: list, border: list):
    graph_list = []
    count = []

    for i in range(len(border) - 1):
        counter = 0
        for num in nums:
            if border[i] <= num < border[i + 1]:
                graph_list.append(border[i])

    return graph_list


def toFixed(numObj, digits=2):
    try:
        return f"{numObj:.{digits}f}"
    except Exception:
        return numObj
