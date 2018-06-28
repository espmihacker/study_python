# 复制文件中的内容

file_name = input('请输入要复制的文件名(md.txt)：')
src = open(file_name)
text = src.read()

# new_file_name = '[copy]' + file_name
position = file_name.rfind('.')
new_file_name = file_name[0:position] + '[copy]' + file_name[position:]
dist = open(new_file_name, 'w')
dist.write(text)

src.close()
dist.close()
