import os

# 创建目录
# os.mkdir('test')

# 删除目录
# os.rmdir('dir')

# 改变目录 os.chdir()

# 获取重命名文件夹的名字
folder_name = input('目录名：')

# 获取指定文件夹中所有文件的名字
fil_names = os.listdir(folder_name)

os.chdir(folder_name)

# 重命名
for name in fil_names:
    print(name)
    os.rename(name, '[m]' + name)
