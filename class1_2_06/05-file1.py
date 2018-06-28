# 文件操作
# r 只读，文件必须存在,默认
# w 只写，文件可以不存在，存在删了重来
# a 追加
# -- b,二进制 --
# rb
# wb
# ab
# -- 读写 --
# r+
# w+
# a+
# -- --
# rb+
# wb+
# ab+

# read
# file = open('md.txt', 'r')
# print(file.read())
# file.close()

# write
# file = open('md.txt', 'w')
# file.write('888\n\n')
# file.close()

# append
file = open('md.txt', 'a')
file.write('\n\n666')
file.close()
