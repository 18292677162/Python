import random  # 随机数工具包

while 1:
    player: int = input("请输入---石头(1) 剪刀(2) 布(3) 退出(0):")
    while not (0 == player or 1 == player or 2 == player or 3 == player):
        player = int(input("输入错误, 请重新输入: "))

    # randint(a, b) 随机数 a <= n <= b
    computer: int = random.randint(1, 3)

    if ((1 == player and 2 == computer) or
            (2 == player and 3 == computer) or
            (3 == player and 1 == computer)):
        print("恭喜你，你赢了")
    elif player == computer:
        print("难分胜负")
    elif player == 0:
        exit()
    else:
        print("你输了")
