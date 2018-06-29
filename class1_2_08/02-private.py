class Dog:

    # 私有方法
    def __test1(self):
        print("------Messing")

    # 公有方法
    def test2(self, money):
        if money > 1:
            self.__test1()
        else:
            print("余额不足！")
        print("------2")


dog = Dog()
dog.test2(-1)