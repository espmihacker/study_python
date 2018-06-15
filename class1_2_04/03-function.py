# 一个函数中返回多个返回值


def test():
    a = 1
    b = 2
    c = 3

    # return a # 函数运行到return就运行结束了

    # 用一个列表来封装要返回的三个数的值
    d = [a, b, c]
    return d


num = test()
print(num)
