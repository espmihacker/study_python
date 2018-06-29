class Dog:

    # 对象销毁前调用，善后工作
    def __del__(self):
        print("Dog over")


dog1 = Dog()
print("==================")
dog2 = dog1

del dog1
print("==================")
