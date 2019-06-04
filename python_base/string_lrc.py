list1 = ["\n   丑八怪能否别把灯打开",
         "\n我要的爱出没在漆黑一片的舞台\t\n",
         "丑八怪在这暧昧的时代\t",
         "我的存在不意外", ]
# 去除空白字符
for list1_str in list1:
    print("|%s|" % list1_str.lstrip().rstrip())

# 文本对齐
# 中
for list1_str in list1:
    print("|%s|" % list1_str.strip().center(20, "　"))  # 英文空格半角" "  中文空格全角"　"
# 左
for list1_str in list1:
    print("|%s|" % list1_str.strip().ljust(20, "　"))
# 右
for list1_str in list1:
    print("|%s|" % list1_str.strip().rjust(20, "　"))

str1 = "丑八怪能否别把灯打开\t 我要的爱出没在漆黑一片的舞台" \
       "\t \n\t丑八怪在这暧昧的时代\t\t 我的存在不意外"
print(str1)
# 默认以空白字符拆分
list2 = str1.split()
print((list2))

list3 = ",".join(list2)
print(list3)
