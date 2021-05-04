import matplotlib.pyplot as plt



class NumberWithProbability():
    def __init__(self, number, count, probability) -> None:
        super().__init__()
        self.number = number
        self.count = count
        self.probability = probability

    def __str__(self):
        return f"{self.number} | {self.count} | {self.probability}"


def printTable(l: list):
    length = 150
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

    # for i in nums:
    #     if flag:
    #
    #         if tmp == '-':
    #             print(f"{toFixed(__probability)}, x ≤ {i.number}")
    #         else:
    #             print(f"{toFixed(__probability)}, {tmp} < x ≤ {i.number}".center(15, " "))
    #         tmp = i.number
    #
    #     __probability = __probability + i.probability
    #     point_list.append([i.number, i.probability])
    #
    # if flag:
    #     print(f"   {1}, x > {nums[len(nums) - 1].number}")

    return point_list

def getPointForStaticGraphic(nums: list) -> list:
    point_list = []

    for i in nums:
        point_list.append([i.number, i.probability])

    return point_list


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

def drawBarGraph(nums: list):
    # data = pd.DataFrame(data=np.c_[iris['data'], iris['target']], columns=iris['feature_names'] + ['target'])
    pass

def toFixed(numObj, digits=2):
    try:
        return f"{numObj:.{digits}f}"
    except Exception:
        return numObj
