class Cat:

    # 初始化对象，有些类似构造方法
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("__________init__________")

    # 对象的描述信息
    def __str__(self):
        return "haha~"

    def eat(self):
        print("Cat is eating ....")

    def drink(self):
        print("Cat is drink ....")

    def introduce(self):
        print("Cat name %s, age %d"%(self.name, self.age))


#创建一个对象
tom = Cat("Tom", 18)
# tom.name = "Tom"
# tom.age = 18

tom.introduce()
tom.eat()
tom.drink()
# -----------------------------
lan = Cat("蓝猫", 40)
# lan.name = "蓝猫"
# lan.age = 40

lan.introduce()
tom.eat()
tom.drink()
# -----------------------------
print(tom)
print(lan)
# <__main__.Cat object at 0x7efc9c356b38>
# <__main__.Cat object at 0x7efc9c356c50>
