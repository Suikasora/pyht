tarList = []
print("输入数值(当输入-1时停止输入)：")
while True:
    i = float(input())
    if i == -1:
        break
    tarList.append(i)


def sum(list):
    """对列表的数值求和
    """
    s = 0
    for j in list:
        s += j
    return s


def average(list):
    """对列表的数值求平均值
    """
    aver = 0
    aver = sum(list) / (len(list) * 1.0)
    return aver


print("输入的数据个数为%d" % len(tarList))
print("sum={:.2f}".format(sum(tarList)))
print("average={:.2f}".format(average(tarList)))
