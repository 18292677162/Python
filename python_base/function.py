def sum(left, right):
    """求和"""
    print("%d + %d = " % (left, right), end="")
    return left + right


print("%d" % sum(1, 2))


def print_line(char):
    """
    打印单行字符串
    :param char: 字符
    """
    print(char * 20)


print_line("*")


def print_lines(row, char):
    """打印多行字符串

    :param row:行数
    :param char:字符
    """
    n = 0
    while (n < row):
        print_line(char)
        n += 1


print_lines(5, "-")
