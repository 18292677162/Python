list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1)

# len(item) 计算容器中元素个数
print(len(list1))

# del(item) 删除变量
del (list1[1])
del list1[0]
print(list1)
# del list1

# max & min 最大最小值
print(max(list1))
print(min(list1))

dict1 = {"1": "9", "2": "8", "3": "7"}
print(max(dict1))
print(min(dict1))

# 比较
print(1 < 2)
print("1" < "2")
print("1" < "A")
print("A" < "a")

print([1, 1, 1] > [2, 2, 2])
print((1, 1, 1) > (2, 2, 2))
# print({"a": 1} > {"s": 2}) 字典不可比较

# 切片
print("0123456789"[1:3])
print([0, 1, 2, 3, 4][1:3])
print((0, 1, 2, 3, 4,)[1:3])
# 字典不支持切片

# 运算符
# +产生新元素  extend追加在原元素
print([1, 2] + [3, 4])
print([1] * 4)
print(3 in (1, 2, 3))
print(3 not in (1, 2, 3))

list2 = [1, 2, 3, 4]
print(list2)
list2.extend([5, 6])  # 扩展 每个元素分别追加
print(list2)
list2.append([5, 6])  # 增加 列表参数当成一个独立的元素
print(list2)

for i in range(3):
    print("*")
    # break
else:
    print("else")
print("end")

# 搜索字典
find_name = "李四"
people = [{"name": "张三"},
          {"name": "李四"},
          {"name": "王五"}]
for k in people:
    print(k)
    if (k["name"] == find_name):
        print("找到了: %s" % find_name)
        break
else:
    print("没找到: %s" % find_name)
print("退出")
