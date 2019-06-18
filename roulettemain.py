import datetime

import roulettoclass

# ルーレットタイプ
MODE = 'a'  #アメリカンタイプ
#MODE = 'e' #ヨーロピアンタイプ

# 試行回数
N_LOOP = 38

# TSV出力ファイル
output_filename = "roulette1/data.txt"

# Sqlite3
# データベースファイルのパス
dbpath = 'roulette1/rltdb1.db'

#ルーレットインスタンス生成
rlt = roulettoclass.Roulette(MODE,output_filename,dbpath)

# 回す
print('ルーレット実行開始:' + str(datetime.datetime.now()))
for i in range(N_LOOP):
    rlt.Do()
print('ルーレット実行完了:' + str(datetime.datetime.now()))

# データベースに書き出し
rlt.SaveSqlite()

# ファイルに書き出し
rlt.OutputList()




