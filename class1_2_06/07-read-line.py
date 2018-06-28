# 读取大文件的时候禁止使用read(),应该采用readline()进行一行一行的读取
file_name = input('请输入要复制的文件名(md.txt)：')

position = file_name.rfind('.')
new_file_name = file_name[0:position] + '[copy2]' + file_name[position:]

src = open(file_name)
dist = open(new_file_name, 'a')
while len(src.readline()) == 0:
    dist.write(src.readline() + '\n')

src.close()
dist.close()
