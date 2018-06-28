#coding=utf-8


# 匿名函数的应用2
def test(a, b, func):
    result = func(a, b)
    return result

# python2直接当做表达式 python3使用eval()
func_new = eval(input('请输入一个匿名函数:'))

num = test(11, 22, func_new)
print(num)
