import random  # 随机数工具包

while (1):
    player = int(input("请输入---石头(1) 剪刀(2) 布(3) 退出(0):"))

    # randint(a, b) 随机数 a <= n <= b
    computer = int(random.randint(1, 3))

    if ((player == 1 and computer == 2) or
            (player == 2 and computer == 3) or
            (player == 3 and computer == 1)):
        print("恭喜你，你赢了")
    elif player == computer:
        print("难分胜负")
    elif player == 0:
        exit()
    else:
        print("你输了")
