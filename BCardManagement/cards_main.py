#!
# Shebang

import cards_tools

while True:
    # 选择操作

    # TODO(Pinna) 功能菜单
    cards_tools.show_menu()

    # input 默认字符串
    action_str = input("请选择操作功能: ")
    print("您选择的操作是:【%s】" % action_str)

    # 1,2,3 对名片操作
    if action_str in ["1", "2", "3"]:
        # 新增名片
        if "1" == action_str:
            cards_tools.new_card()
        # 显示全部
        elif "2" == action_str:
            cards_tools.show_all()
        # 查询全部
        elif "3" == action_str:
            cards_tools.search_card()
    # 0 退出系统
    elif "0" == action_str:
        # pass 表示一个占位符, 可以保证程序正常运行, pass不进行任何操作
        print("欢迎再次使用【名片管理系统】", end=" ")
        break
    # 其他 输入错误
    else:
        print("输入有误, 请重新选择")
