# 获取当前的温度
def get_temperature():
    temperature = 22
    print("当前的温度是：%d"%(temperature))
    return temperature

# 获取华氏温度（假设）
def get_temperature2():
    temperature = get_temperature() + 3
    print("当前的温度（华氏）是：%d"%(temperature))
    return temperature

# 函数的调用
get_temperature2()
