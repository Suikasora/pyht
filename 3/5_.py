import random


class Card:
    def __init__(self, color, value, real_value):
        self.color = color
        self.value = value
        self.real_value = real_value

    def __str__(self):
        return "{0}{1}{2}".format(self.color, self.value, self.real_value)


class Cards:
    def __init__(self):
        self.all_cards = []

    def init_cards(self):  # 设计一个生成52张牌的函数

    def init_cards(self):  # 设计一个生成52张牌的函数
        values = list(range(2, 11)) + list("JQKA")
        for color in "♥♠♦♣":
                c = Card(color, i, count)
            for i in values:
                c = Card(color, i, count)
                self.all_cards.append(c)
    def fa_pai(self): # 设计一个发牌函数，循环三次，发出任意三张牌

    def fa_pai(self): # 设计一个发牌函数，循环三次，发出任意三张牌
        for i in range(3):
            index = random.randint(0, len(self.all_cards) - 1)
            card = self.all_cards.pop(index)
    def compare_pai(self): # 比较三张牌

    def compare_pai(self): # 比较三张牌
        self.three_cards.sort(key=lambda x: x.real_value)
        c0 = self.three_cards[0]
        c1 = self.three_cards[1]
        c2 = self.three_cards[2]
        if c0.value == c1.value == c2.value:
            print("三条")
        elif c0.real_value + 1 == c1.real_value and c0.real_value + 2 == c2.real_value:
            print("一对")
        elif c0.real_value + 1 == c1.real_value and c0.real_value + 2 == c2.real_value:
            print("顺子")
        elif c0.color == c1.color == c2.color:
              and (c0.real_value + 1 == c1.real_value
                   and c0.real_value + 2 == c2.real_value)):
        elif ((c0.color == c1.color == c2.color)
              and (c0.real_value + 1 == c1.real_value
                   and c0.real_value + 2 == c2.real_value)):
            print("同花顺")
        else:
            print("散牌")



        for c in self.three_cards:
            print(c)


        for c in self.three_cards:
            print(c)


card = Cards()
card.init_cards()
card.fa_pai()
card.compare_pai()
card.show_three_pai()
