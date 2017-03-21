#coding:utf-8
import sys
import linecache

# コマンドライン引数を受け取る
# 無かったら2行(splitコマンドと同様)
argvs = sys.argv
if len(argvs) <= 1:
    row = 2
else:
    row = int(argvs[1])

lines = []
for line in open('hightemp.txt','r'):
    lines.append(line)

# 1 ファイルの行数
val = len(lines) / row

# ファイルの分割
for i in range(row):
    text = ''
    # 指定した行数だけテキストを保持
    for j in range(int(i*val),int((i+1)*val)):
        text = text + lines[j]
    # ファイルへの書き込み
    f = open('split/'+str(i)+'.txt','w')
    f.write(text)
    f.close()
