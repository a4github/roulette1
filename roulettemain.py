import random
import os
import datetime
import sqlite3

# 試行回数
N_LOOP = 38

# TSV出力ファイル
output_filename = "roulette1/data.txt"

# Sqlite3
# データベースファイルのパス
dbpath = 'roulette1/rltdb1.db'

# データベース接続とカーソル生成
connection = sqlite3.connect(dbpath)
# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
# connection.isolation_level = None
cursor = connection.cursor()

class Roulette():

    def __init__(self,mode):

        #self.output_filename = "roulette1/data.txt"

        self.number = None
        self.color = None
        self.eo = None

        self.numberhistory = []
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
        self.number=random.choice(self.spotlist)
        self.eo=self.CheckEo(self.number)
        self.color=self.CheckColer(self.number)

        self.numberhistory.append(self.number)
        self.colorhistory.append(self.color)
        self.eohistory.append(self.eo)

    def GetResult(self):
        return self.number

    def GetColer(self):
        return self.color

    def GetEo(self):
        return self.eo

    def CheckColer(self,number2):
        if number2 == '0': return 'zero'
        elif number2 == '00': return 'zero'
        elif number2 == '1': return 'red'
        elif number2 == '2': return 'black'
        elif number2 == '3': return 'red'
        elif number2 == '4': return 'black'
        elif number2 == '5': return 'red'
        elif number2 == '6': return 'black'
        elif number2 == '7': return 'red'
        elif number2 == '8': return 'black'
        elif number2 == '9': return 'red'
        elif number2 == '10': return 'black'
        elif number2 == '11': return 'black'
        elif number2 == '12': return 'red'
        elif number2 == '13': return 'black'
        elif number2 == '14': return 'red'
        elif number2 == '15': return 'black'
        elif number2 == '16': return 'red'
        elif number2 == '17': return 'black'
        elif number2 == '18': return 'red'
        elif number2 == '19': return 'red'
        elif number2 == '20': return 'black'
        elif number2 == '21': return 'red'
        elif number2 == '22': return 'black'
        elif number2 == '23': return 'red'
        elif number2 == '24': return 'black'
        elif number2 == '25': return 'red'
        elif number2 == '26': return 'black'
        elif number2 == '27': return 'red'
        elif number2 == '28': return 'black'
        elif number2 == '29': return 'black'
        elif number2 == '30': return 'red'
        elif number2 == '31': return 'black'
        elif number2 == '32': return 'red'
        elif number2 == '33': return 'black'
        elif number2 == '34': return 'red'
        elif number2 == '35': return 'black'
        elif number2 == '36': return 'red'
        else:return 'error'

    def CheckEo(self,number2):
        if int(number2) == 0: return 'zero'
        elif (int(number2) % 2) == 0: return 'even'
        else: return 'odd'

    def PrintList(self):
        for i in range(len(self.numberhistory)):
            print(self.numberhistory[i]+'/'+self.colorhistory[i]+'/'+self.eohistory[i])
    
    def OutputList(self):
        print('ファイル書き出し中...' + str(datetime.datetime.now()))

        # 出目のカウント
        number_count = []
        zero_count =0
        red_count = 0
        black_count = 0

        for i in range(len(self.spotlist)):
            number_count.append(self.numberhistory.count(self.spotlist[i]))

        #file = open(self.output_filename, 'w')
        file = open(output_filename, 'w')
        
        for i in range(len(self.numberhistory)):
            file.write(self.numberhistory[i]+'\t'+self.colorhistory[i]+'\t'+self.eohistory[i]+'\n') 

        # 改行
        file.write('\n\n')

        # 出目のカウント
        for i in range(len(self.spotlist)):
            file.write(self.spotlist[i]+'\t'+str(number_count[i])+'\n') 

        # 色別のカウント
        zero_count = self.numberhistory.count('0') + self.numberhistory.count('00')
        red_count = self.colorhistory.count('red')
        black_count = self.colorhistory.count('black')

        file.write('zero\t'+str(zero_count)+'\n')
        file.write('red\t'+str(red_count)+'\n')
        file.write('black\t'+str(black_count)+'\n')

        file.close()

        print('ファイル書き出し完了' + str(datetime.datetime.now())) 

    def SaveSqlite(self):
        print('Sqlite INSERT start:' + str(datetime.datetime.now())) 

        cursor.execute("delete from deme;")

        for i in range(len(self.numberhistory)):
            cursor.execute("INSERT INTO deme valueS (:id, :number, :color, :eo)",
                   {'id': i, 'number': self.numberhistory[i], 'color':self.colorhistory[i], 'eo':self.eohistory[i]})

        #cursor.execute("INSERT INTO deme valueS (:id, :number, :color, :eo)",
        #           {'id': 1, 'number': '田中', 'color':'blue', 'eo':'test'})

        # 保存を実行（忘れると保存されないので注意）
        connection.commit()

        # 接続を閉じる
        connection.close()

        print('Sqlite INSERT finish:' + str(datetime.datetime.now())) 



# main

rlt = Roulette('a')

print('ルーレット実行中...' + str(datetime.datetime.now()))
for i in range(N_LOOP):
    rlt.Do()

print('ルーレット実行完了' + str(datetime.datetime.now()))

# データベースに書き出し
rlt.SaveSqlite()

# ファイルに書き出し
rlt.OutputList()




