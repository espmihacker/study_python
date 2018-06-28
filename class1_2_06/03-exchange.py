# 交换，面试题之一


a = 4
b = 5
c = 0
print("[原]a=%d,b=%d" % (a, b))

# 第一种方法
# c = a
# a = b
# b = c
#
# print("[交]a=%d,b=%d" % (a, b))

# 第二种
# a = a + b
# b = a - b
# a = a - b
#
# print("[交]a=%d,b=%d" % (a, b))

# 第三种，python所独有
a, b = b, a

print("[交]a=%d,b=%d" % (a, b))
