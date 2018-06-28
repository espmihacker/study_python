class SweetPotato:

    def __init__(self):
        self.cookedString = '生的'
        self.cookedLevel = 0
        self.condiments = []

    def __str__(self):
        return "地瓜 状态：%s[%d]，添加作料：%s" % (self.cookedString, self.cookedLevel, str(self.condiments))

    def cook(self, cooked_time):
        self.cookedLevel += cooked_time

        if 3 > self.cookedLevel >= 0:
            self.cookedString = '生的'
        elif 5 > self.cookedLevel >= 3:
            self.cookedString = '半生不熟'
        elif 8 > self.cookedLevel >= 5:
            self.cookedString = '熟了'
        elif self.cookedLevel >= 8:
            self.cookedString = '焦了'

    def addCondiments(self, condiment):
        self.condiments.append(condiment)


# 创建了一个地瓜对象
di_gua = SweetPotato()

di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
di_gua.addCondiments("大蒜")
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
di_gua.addCondiments("芥末")
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)


