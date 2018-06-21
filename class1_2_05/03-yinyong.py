# 可变类型与不可变类型 列表和字典可变


# 递归完成阶乘运算
def get_nums(num):
    if num > 1:
        return num * get_nums(num - 1)
    else:
        return num


result = get_nums(5)

print('result=%d' % result)
