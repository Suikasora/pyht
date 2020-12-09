def fib_recur(n):
    assert n >= 0, "n > 0"
    if n <= 1:
        return n
    return fib_recur(n - 1) + fib_recur(n - 2)


for i in range(1, 20):
    print(fib_recur(i), end=' ')

#Method2============================================
print()


class Fibonacci(object):
    """迭代器"""
    def __init__(self, n):
        # 保存初始值
        self.n = n
        # 指向位置
        self.current = 0
        self.a = 0
        self.b = 1

    def __next__(self):
        if self.current < self.n:
            self.a, self.b = self.b, self.a + self.b
            self.current += 1
            return self.a
        else:
            raise StopIteration

    def __iter__(self):
        return self


fib = Fibonacci(19)
for num in fib:
    print(num, end=' ')
