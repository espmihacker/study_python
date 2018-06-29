class Tool(object):

    # 类属性，仅定义一次
    num = 0

    # 实例方法
    def __init__(self, name):
        self.name = name
        Tool.num += 1

    # 操作类属性(类方法)
    @classmethod
    def add_num(cls):
        cls.num = 100

    # 静态方法
    @staticmethod
    def print_menu():
        print("-"*25)
        print("    地下城与勇士")
        print("    1.开始游戏")
        print("    2.退出游戏")
        print("-"*25)


Tool.print_menu()
# 全局变量
# num = 0
tool = Tool("铁锹")
print(Tool.num)
bgc = Tool("工兵铲")
print(Tool.num)
qianzi = Tool("钳子")
print(Tool.num)

print("#"*25)
# 通过类的名字调用类方法，还可以通过创建的对象调用
Tool.add_num()
print(Tool.num)

print("#"*25)

