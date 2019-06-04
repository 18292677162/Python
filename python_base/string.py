str = "0123456789"
# 1. 截取从 2 ~ 5 位置 的字符串
print(str[2:6])
# 2. 截取从 2 ~ 末尾 的字符串
print(str[2:])
# 3. 截取从 开始 ~ 5 位置 的字符串
print(str[:6])
# 4. 截取完整的字符串
print(str[:])
# 5. 从开始位置，每隔一个字符截取字符串
print(str[::2])
# 6. 从索引 1 开始，每隔一个取一个
print(str[1::2])
# 7. 截取从 2 ~ 末尾 - 1 的字符串
print(str[2::-1])
# 8. 截取字符串末尾两个字符S
print(str[-2:])
# 9. 字符串的逆序（面试题）
print(str[::-1])

str1 = '我是"闪电侠"'
for char in str1:
    print(char, end="")
print()

str2 = "hello world"
# 1.统计字符串长度
print(len(str2))

# 2.统计子字符串出现次数
print(str2.count("ll"))
# 注意: 不存在不会报错!!!
print(str2.count("bye"))

# 3.某一个子字符串首次出现的位置
print(str2.index("lo"))
# 注意: 不存在会报错
# print(str2.index("bye"))
