def print_info(x):
    i = max(x)
    j = min(x)
    l = len(x)
    print("最大值是%s" % i, end=',')
    print("最小值是%s" % j, end=',')
    print("元素个数是{0}".format(l))
    return i, j, l


s1 = [9, 8, 7, 3, 2, 1, 55, 6]
s2 = ['apple', 'pear', 'melon', 'kiwi']
s3 = 'TheQuickBrownFox'
print("List =", s1)
q = print_info(s1)
print("List =", s2)
w = print_info(s2)
print("List =", s3)
e = print_info(s3)
