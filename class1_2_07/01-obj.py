# 学习pytho类与对象第一天
class Cat:
    def eat(self):
        print("Cat is eating ....")

    def drink(self):
        print("Cat is drink ....")

    def introduce(self):
        print("Cat name %s, age %d"%(self.name, self.age))


#创建一个对象
tom = Cat()
tom.name = "Tom"
tom.age = 18

tom.eat()
tom.drink()
tom.introduce()

lan = Cat()
lan.name = "蓝猫"
lan.age = 40

tom.eat()
tom.drink()
lan.introduce()