# 学习类的继承,python3推荐写上object
class Animal(object):

    def eat(self):
        print("eat")

    def run(self):
        print("run")


class Cat(Animal):

    def lo(self):
        print("cat lo")


class Dog(Animal):

    # 覆写父类Animal中的方法
    def run(self):
        print("疾走")

        # 下面两种方式调用父类的方法
        # Animal.run(self)
        # super().run()


# 多继承
class XXX(Cat, Dog):
    pass


#####################################
cat = Cat()
cat.run()
dog = Dog()
dog.run()

# 私有的方法不会被继承
# 私有的属性不会被继承
# 调用父类中继承的公有方法，在该方法中调用私有属性和方法可行
# 在子类中实现的公有方法，该方法是不能调用父类中的私有属性和私有方法

