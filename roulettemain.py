import random

class Roulette():

    def __init__(self,mode):

        self.value = None
        self.color = None
        self.eo = None

        # a -> アメリカンタイプ 
        # e -> ヨーロピアンタイプ
        if mode =='a':
            self.spotlist=['0', '00',\
            '1', '2', '3','4','5','6','7','8','9','10','11','12',\
            '13','14','15','16','17','18','19','20','21','22','23','24',\
            '25','26','27','28','29','30','31','32','33','34','35','36']
        elif mode =='e':
            self.spotlist=['0',\
            '1', '2', '3','4','5','6','7','8','9','10','11','12',\
            '13','14','15','16','17','18','19','20','21','22','23','24',\
            '25','26','27','28','29','30','31','32','33','34','35','36']

    def Do(self):
        self.value=random.choice(self.spotlist)
        self.eo=self.checkEo(self.value)
        self.color=self.CheckColer(self.value)

    def GetResult(self):
        return self.value

    def GetColer(self):
        return self.color

    def GetEo(self):
        return self.eo

    def CheckColer(self,value2):
        if value2 == '0': return 'zero'
        elif value2 == '00': return 'zero'
        elif value2 == '1': return 'red'
        elif value2 == '2': return 'black'
        elif value2 == '3': return 'red'
        elif value2 == '4': return 'black'
        elif value2 == '5': return 'red'
        elif value2 == '6': return 'black'
        elif value2 == '7': return 'red'
        elif value2 == '8': return 'black'
        elif value2 == '9': return 'red'
        elif value2 == '10': return 'black'
        elif value2 == '11': return 'black'
        elif value2 == '12': return 'red'
        elif value2 == '13': return 'black'
        elif value2 == '14': return 'red'
        elif value2 == '15': return 'black'
        elif value2 == '16': return 'red'
        elif value2 == '17': return 'black'
        elif value2 == '18': return 'red'
        elif value2 == '19': return 'red'
        elif value2 == '20': return 'black'
        elif value2 == '21': return 'red'
        elif value2 == '22': return 'black'
        elif value2 == '23': return 'red'
        elif value2 == '24': return 'black'
        elif value2 == '25': return 'red'
        elif value2 == '26': return 'black'
        elif value2 == '27': return 'red'
        elif value2 == '28': return 'black'
        elif value2 == '29': return 'black'
        elif value2 == '30': return 'red'
        elif value2 == '31': return 'black'
        elif value2 == '32': return 'red'
        elif value2 == '33': return 'black'
        elif value2 == '34': return 'red'
        elif value2 == '35': return 'black'
        elif value2 == '36': return 'red'
        else:return '-1'

    def checkEo(self,value2):
        if int(value2) == 0: return 'zero'
        elif (int(value2) % 2) == 0: return 'even'
        else: return 'odd'


rlt = Roulette('a')
rlt.Do()
print(rlt.GetResult()+'/'+rlt.GetColer()+'/'+rlt.GetEo())

