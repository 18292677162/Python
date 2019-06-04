# 定义列表
my_list = ["hello", "world"]

# 1.取值取索引
# 打印列表
print(my_list)
print(my_list[1])
print(my_list[-1])

# 取索引---数据不存在报错
print(my_list.index("hello"))

# 2.修改
my_list[0] = "myhello"
print(my_list)

# 3.增加

# 尾插 append(self, object)
my_list.append(12)
print(my_list)

# 固定位置插入 insert(self, index, object)
my_list.insert(1, "new")
print(my_list)

# 列表尾插 extend(self, iterable)
tmp_list = ["你好", "你好", "谢谢", "再见"]
my_list.extend(tmp_list)
print(my_list)

# 4.统计

# len 元素总数
list_len = len(my_list)
print("元素总数: %d" % list_len)

# count 某一数据出现次数
print("你好出现的次数 %d" % (my_list.count("你好")))

# 5.删除

# 删除指定数据 remove(object)
my_list.remove("new")
print(my_list)

# 删除指定位置数据(默认删除最后一个数据) pop(index)
my_list.pop(2)
print(my_list)
# del关键字---本质是将一个变量从内存中删除
# 后续代码不可使用此变量
del my_list[2]
print(my_list)

# 清空列表 clear(self)
my_list.clear()
print(my_list)

# del关键字---本质是将一个变量从内存中删除
# 后续代码不可使用此变量
age = 18
del age
# print(age)

# 6.排序
list1 = [4, 5, 2, 3, 1, 7, 9, 6, 0, 8]
# 升序 L.sort(key=None, reverse=False)
list1.sort()
print(list1)
# 降序
list1 = [4, 5, 2, 3, 1, 7, 9, 6, 0, 8]
list1.sort(reverse=True)
print(list1)
# 逆序
list1 = [4, 5, 2, 3, 1, 7, 9, 6, 0, 8]
list1.reverse()
print(list1)

# 关键字
import keyword

print(keyword.kwlist)
