print("hello")
print("Hello World")
print('AAAAA\nBBBBB')

print("""12345
6789
101112""")

# this is a test
print(1 + 1)
print(2 - 1)
print(2 * 3)
print(10 / 3)
print(2 ** 3)
print("A" * 10)
print(5 // 3)

# 变量定义
a = 100
print(a)

# 买苹果
price = 8.5
weight = 7.5
money = price * weight
print(money)

# 变量类型
"""
姓名：小明
年龄：18
性别：是男生
身高：1.75米
体重：75.0公斤
"""

# Python 定义变量不需要指定变量类型
# 运行时 Python 解释器会根据赋值语句等号右侧数据自动推导数据类型
name = "小明"  # str
age = 18  # int
gender = True  # bool
height = 1.75  # float
weight = 75.0  # float

print(name)
print(age)

# 格式化输出
name = input("输入姓名: ")
number = 201606060606
price = 9.00
weight = 5
money = 45.00
scale = float(input("输入小数: "))
print("我叫%s" % name)
print("学号是%6d" % number)
print("苹果单价 %.2f 元/斤，购买 %.2f 斤，需要 %.2f 元" % (price, weight, money))
print("数据比例为 %.2f%%" % (scale * 100))


import keyword
print(keyword.kwlist);