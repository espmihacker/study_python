import sys

class T:
    pass


t = T()
tt = t


# 获取引用计数
count = sys.getrefcount(t)
print(count)
