import random


def gen_pocker(n):
    random.shuffle(n)
    return n


# 产生牌的花色


def getColor(n):
    if (n >= 0 and n <= 12):
        return "梅花"
    elif (n >= 13 and n <= 25):
        return "方块"
    elif (n >= 26 and n <= 38):
        return "红桃"
    elif (n >= 39 and n <= 51):
        return "黑桃"


def getValue(n):
    if n % 13 == 0:
        return 'A'
    elif n % 13 == 12:
        return 'K'
    elif n % 13 == 11:
        return 'Q'
    elif n % 13 == 10:
        return 'J'
    else:
        return n % 13


def getPuk():
    List = [] # 代表一副牌，现在表示还没有牌，只是一个牌盒
    ListName = []
    for i in range(0, 52):
        List.append(i) # 按顺序往牌盒中放入52张牌
    List = gen_pocker(List) # 将牌盒中的牌打乱顺序
    List1 = [] # 定义4个牌手
    List2 = []
    List3 = []
    List4 = []
    for i in range(0, 52): # 实现发牌
        if i < 13: # 打乱后的前13张牌发给牌手1，实现牌手1手牌中如何含有花色和数字
            List1.append(getColor(List[i]) + str(getValue(List[i])))
        elif i < 26:
            List2.append(getColor(List[i]) + str(getValue(List[i])))
        elif i < 39:
            List3.append(getColor(List[i]) + str(getValue(List[i])))
        else:
            List4.append(getColor(List[i]) + str(getValue(List[i])))

    print(List)
    print("\n", "牌手1:", end='')
    for i in List1:
        print(i, end=' ')
    print("\n", "牌手2:", end='')
    for i in List2:
        print(i, end=' ')
    print("\n", "牌手3:", end='')
    for i in List3:
        print(i, end=' ')
    print("\n", "牌手4:", end='')
    for i in List4:
        print(i, end=' ')


getPuk()
