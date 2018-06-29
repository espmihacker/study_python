class Dog:

    # 通过方法对属性 进行设置
    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name


dog = Dog()

dog.set_name("XiaoH")

print(dog.get_name())