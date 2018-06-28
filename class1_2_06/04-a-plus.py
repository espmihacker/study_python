# a+=a和a++的区别
# a = 100   #值
a = [100]   #地址


def fun1(num):
    #
    num += num
    print(num)


def fun2(num):
    # 先算右边，再赋值给左边 num+num ===> [100,100] 局部num指向[100, 100]，而全局的a并没有指向[100，100]
    num = num + num
    print(num)


fun2(a)
print(a)

# fun1()运行结果：
# [100, 100]
# [100, 100]

# fun2()运行结果：
# [100, 100]
# [100]
