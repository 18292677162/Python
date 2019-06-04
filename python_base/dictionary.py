info_dict = {"name": "大白",
             "age": 18,
             "gender": True,
             "height": 1.83}

# 字典无序输出顺序可能不一样
print(info_dict)

# 1.取值
print(info_dict["name"])

# 2.增加/修改
# key不存在，新增键值对
info_dict["weight"] = 65.2
# key存在，修改键值对
info_dict["age"] = 19
print(info_dict)

# 3.删除
info_dict.pop("weight")
print(info_dict)

# 4.统计键值对数量
print(len(info_dict))

# 5.合并字典 (相同覆盖)
tmp_dict = {"weight": 68.3}
info_dict.update(tmp_dict)
print(info_dict)

# 6.清空字典
tmp_dict.clear()

# 7.遍历字典
for key in info_dict:
    print("%s: %s" % (key, info_dict[key]))

# 8.与列表结合
list1 = [123,
         {"name": "张三", "hight": 183.2},
         {"name": "李四", "hight": 172.1}]
for i in list1:
    print(i)
