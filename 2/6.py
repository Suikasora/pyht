import sys
f = open("out.txt", "w+")
try:
    while True:
        ranChar = input("请输入，按Q结束：")
        if (ranChar == 'Q'):
            sys.exit()
        else:
            print(ranChar, file=f)
except KeyboardInterrupt:
    print("结束输入！输入内容保存到out.txt")
finally:
    f.close()
