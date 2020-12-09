import random


def gen_pocker(n):
    random.shuffle(n)
    return n


class Card:
    FaceNum = 0
    Suit = ""

    def __init__(self, num):
        self.FaceNum = num
        self.Suit = self.getColor(num) + str(self.getValue(num))

    @staticmethod
    def getColor(num):
        if (num >= 0 and num <= 12):
            return "梅"
        elif (num >= 13 and num <= 25):
            return "方"
        elif (num >= 26 and num <= 38):
            return "红"
        elif (num >= 39 and num <= 51):
            return "黑"

    @staticmethod
    def getValue(num):
        if num % 13 == 0:
            return 'A'
        elif num % 13 == 12:
            return 'K'
        elif num % 13 == 11:
            return 'Q'
        elif num % 13 == 10:
            return 'J'
        else:
            return num % 13


class Hand:
    List = []

    def addCard(self, C):
        self.List.append(C)

    def clearCards(self):
        self.List.clear()

    def giveCard(self, H, C):
        self.List.remove(C)
        H.addCard(C)


class Poke(Hand):
    def __init__(self):
        for i in range(0, 52):
            self.List.append(Card(i))
        # self.List = gen_pocker(self.List)
        random.shuffle(self.List)

    def getCard(self):
        return self.List.pop()


L1 = Hand()
L2 = Hand()
L3 = Hand()
L4 = Hand()
L = Poke()
for i in range(0, 13):
    L.giveCard(L1, L.getCard())
