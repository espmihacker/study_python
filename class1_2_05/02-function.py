a = 0


def fun():
    """测试全局变量"""
    # 使用global声明下面是使用全局变量而不是新建局部变量
    global a
    a = 33

    print(a)


fun()
print(a)
