# 打印三个数的和


# 2.定义函数
def sum(a, b, c):
    result = a + b + c
    average = result / 3
    print('三个数的和为：%d，平均值为：%d'%(result, average))


# 1.获取三个数的值
num1 = int(input('输入1：'))
num2 = int(input('输入2：'))
num3 = int(input('输入3：'))

# 3.调用函数
sum(num1, num2, num3)
