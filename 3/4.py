import math


class MyMath(object):
    def __init__(self, r):
        self.r = r

    # 圆的周长
    def perimeter(self):
        c = 2 * math.pi * self.r
        return c

    # 圆的面积
    def area(self):
        a = math.pi * r * r
        return a

    # 球的表面积
    def surfaceArea(self):
        s = 4 * math.pi * r * r
        return s

    # 球的体积
    def volume(self):
        v = (4 / 3) * math.pi * r * r * r
        return v


r = int(input("请输入圆的半径："))
p = MyMath(r)
print("圆的周长={:.2f}".format(p.perimeter()))
print("圆的面积={:.2f}".format(p.area()))
print("球的表面积={:.2f}".format(p.surfaceArea()))
print("球的体积={:.2f}".format(p.volume()))
