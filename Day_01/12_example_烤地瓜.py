"""
案例：烤地瓜案例

需求：
    烘烤时间            地瓜状态
    [0, 3)              生的
    [3, 7)              半生不熟
    [7, 12)             熟了
    [12, ♾️)            糊了
"""
class SweetPotato:
    def __init__(self):
        self.cook_time = 0
        self.cook_state = '生的'
        self.condiments = []

    def cook(self, time):
        if time < 0:
            print('无效值，你是火星来的吧！')
        else:
            self.cook_time += time
            if 0 <= time < 3:
                self.cook_state = "生的"
            elif 3 <= time < 7:
                self.cook_state = "半生不熟"
            elif 7 <= time < 12:
                self.cook_state = "熟了"
            else:
                self.cook_state = "糊了"

    def add_condiment(self, condiment):
        self.condiments.append(condiment)

    def __str__(self):
        return f'烘烤时间：{self.cook_time} min,烘烤状态：{self.cook_state}，调料：{self.condiments}'

if __name__ == '__main__':
    DG = SweetPotato()

    DG.cook(23)

    DG.add_condiment('鹤顶红')

    print(DG)
