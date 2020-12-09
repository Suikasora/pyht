import random


def gcd(x, y):
    if y > x:
        x, y = y, x
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)


x = random.randint(0, 100)
y = random.randint(0, 100)
print(f"整数1={x},整数2={y}")
a1 = gcd(x, y)
a2 = x * y / a1
print(f"最大公约数是={a1},最小公倍数是={a2:.0f}")
