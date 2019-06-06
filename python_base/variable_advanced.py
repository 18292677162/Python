# 变量与数据分开储存, 全部采用引用的方式
a = 1
c = 1
print("a " + str(id(a)))
print("1 " + str(id(1)))
print("c " + str(id(c)))
print("1 " + str(id(1)))
b = a
print("b " + str(id(b)))


# 调用函数 及返回值 本质传递的是实参保存 数据的引用
def test(num):
    print("函数内部 %d 的地址 %d" % (num, id(num)))
    result = "hello"
    print("函数内部字符串地址 %d" % id(result))
    return result


a = 10
print("a 变量的内存地址 %d" % id(a))
ret = test(a)
print("%s 的内存地址是 %d" % (ret, id(ret)))

# 不可变类型
a = 1
a = "hello"
a = (1, 2, 3)

# 可变类型
a = [1, 2, 3]
print(id(a))
a.append(4)
print(id(a))
a = {"1": "x", "2": "y", "3": "z"}
print(id(a))
a[(1,)] = "w"
print(id(a))

# hash
print(hash("hello"))
print(hash((1,)))

# 全局变量 局部变量
gl_val = 10


def test():
    # 函数先找局部变量，在找全局变量
    # g_val = 20
    # global 对函数内部所有同名变量声明为全局变量
    # 局部变量不会再被创建
    global gl_val
    gl_val = 30


test()
print(gl_val)


# 元组 列表 字典 可以作为返回值类型一次返回多个值
def measure():
    temp = 13
    wetness = 50
    # return (temp, wetness)
    return temp, wetness


# TODO 返回元组  ---  括号可省略
result = measure()
print(result)
# 一次性接收元组返回结果
gl_temp, gl_wetness = measure()
print(gl_temp, gl_wetness)

# 面试题--不创建新元素    交换两个变量的值
a = 6
b = 10
a, b = (b, a)
a, b = b, a
print(a, b)

tuple1 = 1, 2, 3, 4
print(type(tuple1))


# 函数参数的修改
def demo(num, list):
    print("函数内部")
    num += 100
    list.append(4)
    # TODO 对列表+=本质上是调用列表的.extend()方法
    # 所以外部变量会被修改
    list += [5, 6]


gl_num = 1
gl_list = [1, 2, 3]
demo(gl_num, gl_list)
print(gl_num, gl_list)


# TODO 缺省参数 从右向左依次来给(同C++)
def print_info(name, title="", gender=True):
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("[%s] %s 是 %s" % (title, name, gender_text))


print_info("小明")
print_info("小李", "班长")
# 少于缺省参数列表需要指明参数名称
# 如默认升序, reverse=True降序
print_info("小美", gender=False)
gl_list = [4, 6, 7]
gl_list.sort(reverse=True)
print(gl_list)


# TODO 多值参数 *元组 **字典
def more_info(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)


more_info(1, 2, 3, 4, name="小明", age=18)


# 数字累加
def sum(*args):
    num = 0
    print(args)
    for n in args:
        num += n
    return num


ret = sum(1, 2, 3, 4)
print(ret)


# TODO 元组字典的拆包
def open(*args, **kwargs):
    print(args, kwargs)


gl_tuple = (1, 2, 3)
gl_dict = {"name": "小明", "age": 18}
# 拆包---简化元组 字典变量的传递
open(*gl_tuple, **gl_dict)
open(1, 2, 3, name="小明", age=18)


# 递归
def sum_num(num):
    if num == 1:
        return 1
    tem = num + sum_num(num - 1)
    return tem


print(sum_num(5))
