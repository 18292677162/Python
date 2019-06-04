tuple1 = ("hello", "你好", 12, 12, 3.14)
tuple2 = ()
# 元组只有一个元素后面加, 与变量区分开
tuple3 = (95,)

print(tuple1)
print(tuple2)
print(tuple3)

# count统计计数
count = tuple1.count(12)
print(count)
# 取值 index取索引
index = tuple1.index("你好")
print(index, tuple1[index])

for data in tuple1:
    print(data, end=" ")
print()

list(tuple1).append("哈哈哈")
print(tuple1)

# 格式化字符串本质是元组
tuple4 = ("大白", 1.83, 65)
print("%s 身高: %.2f 体重: %d" % tuple4)
info = "%s 身高: %.2f 体重: %d" % tuple4
print(info)
