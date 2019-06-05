card_list = []


def show_menu():
    """显示菜单"""
    welc_str = "欢迎使用【名片管理系统】"
    new_str = "１、新增名片"
    all_str = "２、显示全部"
    sea_str = "３、搜索名片"
    exit_str = "０、退出系统"
    print("－" * 51)
    print("|%s|" % welc_str.center(50, "　"))
    print("|%s|" % new_str.center(50, "　"))
    print("|%s|" % all_str.center(50, "　"))
    print("|%s|" % sea_str.center(50, "　"))
    print("|%s|" % exit_str.center(50, "　"))
    print("－" * 51)


def new_card():
    """新增名片"""
    print("新增名片")
    # 1.提示输入信息
    name = input("请输入姓名: ")
    phone = input("请输入电话: ")
    qq = input("请输入QQ: ")
    email = input("请输入邮箱: ")
    # 2.使用用户的信息建立名片字典
    card_dict = {"姓名: ": name,
                 "电话: ": phone,
                 "QQ: ": qq,
                 "邮箱: ": email}
    # 3.将名片字典添加到列表
    card_list.append(card_dict)
    # 4.提示用户添加成功
    print("添加 %s 的名片成功" % card_dict["姓名: "])


def show_all():
    """显示所有名片"""
    print("－" * 51)

    # 检验空表
    if 0 == len(card_list):
        print("当前没有任何名片记录，请使用【新增名片】功能添加名片")
        return

    # 打印表头
    for tag in ["姓名", "电话", "QQ", "邮箱"]:
        print(tag, end="\t\t\t\t")

    print()

    # 遍历名片输出字典
    for card_dict in card_list:
        print("%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t" %
              (card_dict["姓名: "],
               card_dict["电话: "],
               card_dict["QQ: "],
               card_dict["邮箱: "]))


def search_card():
    """搜索名片"""
    print("－" * 51)

    # 1.提示用户输入搜索姓名
    find_name = input("请输入要搜索的姓名: ")
    # 2.遍历查找
    for card_dict in card_list:
        if card_dict["姓名: "] == find_name:
            for tag in ["姓名", "电话", "QQ", "邮箱"]:
                print(tag, end="\t\t\t\t")

            print()
            print("%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t%s\t\t\t\t" %
                  (card_dict["姓名: "],
                   card_dict["电话: "],
                   card_dict["QQ: "],
                   card_dict["邮箱: "]))

            # 对找到的名片记录修改和删除
            deal_card(card_dict)

            break
    else:
        print("抱歉，没有找到 %s 的记录" % find_name)


def deal_card(find_dict):
    """处理查找到的名片

    :param find_dict:查找到的名片
    """
    print("－" * 51)
    while True:
        action_str = input("请选择要执行的操作: "
                           "1.修改 2.删除 0.返回上级\n")
        if action_str == "1":
            print("修改名片")
            input_card_info(find_dict["姓名: "], "请输入姓名: ")
            input_card_info(find_dict["电话: "], "请输入电话: ")
            input_card_info(find_dict["QQ: "], "请输入QQ: ")
            input_card_info(find_dict["邮箱: "], "请输入邮箱: ")
            print("成功修改名片")
            return
        elif action_str == "2":
            print("%s 已被删除" % find_dict["姓名: "])
            card_list.remove(find_dict)
        elif action_str == "0":
            return
        else:
            print("输入错误, 请重新输入")


def input_card_info(dict_value, tip_message):
    """输入名片信息

    :param dict_value: 字典中原有的值
    :param tip_message: 输入的提示文字
    :return: 输入内容, 返回内容, 否则返回原有值
    """
    # 1.提示用户输入
    result_str = input(tip_message)
    # 2.对输入进行判断, 输入内容返回内容
    if len(result_str) > 0:
        return result_str
    else:
        # 3.输入为空返回结果
        return dict_value
