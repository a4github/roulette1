import random
import os
import datetime

class Roulette():

    def __init__(self,mode):

        self.output_filename = "data.txt"

        self.value = None
        self.color = None
        self.eo = None

        self.valuehistory = []
        self.colorhistory = []
        self.eohistory = []

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
        self.eo=self.CheckEo(self.value)
        self.color=self.CheckColer(self.value)

        self.valuehistory.append(self.value)
        self.colorhistory.append(self.color)
        self.eohistory.append(self.eo)

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

    def CheckEo(self,value2):
        if int(value2) == 0: return 'zero'
        elif (int(value2) % 2) == 0: return 'even'
        else: return 'odd'

    def PrintList(self):
        for i in range(len(self.valuehistory)):
            print(self.valuehistory[i]+'/'+self.colorhistory[i]+'/'+self.eohistory[i])
    
    def OutputList(self):
        print('ファイル書き出し中...' + str(datetime.datetime.now()))
        file = open(self.output_filename, 'w')
        for i in range(len(self.valuehistory)):
            file.write(self.valuehistory[i]+'\t'+self.colorhistory[i]+'\t'+self.eohistory[i]+'\n')  
        file.close()
        print('ファイル書き出し完了' + str(datetime.datetime.now())) 

# main

rlt = Roulette('a')

print('ルーレット実行中...' + str(datetime.datetime.now()))
for i in range(100000):
    rlt.Do()

print('ルーレット実行完了' + str(datetime.datetime.now()))

rlt.OutputList()
#rlt.PrintList()

#print(rlt.GetResult()+'/'+rlt.GetColer()+'/'+rlt.GetEo())

