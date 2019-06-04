# 1.判断空白字符
str1 = " \n"
print(str1.isspace())
str2 = ""
print(str2.isspace())

# 2.判断只包含数字
str3 = "123456①\u00b2一千二百"
print(str3)
# 不能判断小数
print(str3.isdecimal())  # 全角数字
print(str3.isdigit())  # 全角数字、①、\u00b2、Unicode字符串
print(str3.isnumeric())  # 全角数字、①、\u00b2、Unicode字符串、汉字数字

# 3.查找替换
str4 = "ABCDEFG"
print(str4)

print(str4.startswith("AB"))  # 是否以字符串开始

print(str4.endswith("FG"))  # 是否以字符串结束

print(str4.find("CDE"))  # 查找子字符串的位置,成功返回索引,不存在返回-1
print(str4.find("XYZ"))  # index指定字符串不存在报错    find返回-1

print(str4.replace("EFG", "000"))  # 执行完成后返回新字符串，但不会修改原有字符串内容
print(str4)
