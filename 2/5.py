import sys
n = int(sys.argv[1])
#0~n
list1 = []
#0~n的2倍值
list2 = []
#2的0~n次幂
list3 = []
for i in range(0, n):
    list1.append(i)
    list2.append(2 * i)
    list3.append(2 ** i)

f = open('out.txt', 'w+')
print(list1, file=f)
print(list2, file=f)
print(list3, file=f)
f.close()
