import random
#随机单词表
WORDS = (
    "python",
    "jumble",
    "hello",
    "world",
    "java",
)
print("欢迎参加猜单词游戏 \n\
把字母组合成一个正确的单词")

flag = "y"
while flag == "y" or flag == "Y":
    word = random.choice(WORDS)
    jumble = ""
    answer = word

    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]
    print("乱序后单词：", jumble)

    guess = input("\n请你猜:")
    while guess != answer and guess != "":
        print("对不起不正确")
        guess = input("继续猜：")
    if guess == answer:
        print("真棒，你猜对了")

    flag = input("\n是否继续(Y/N):")
