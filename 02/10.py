#config:utf-8

i = 0
f = open('hightemp.txt','r')
for line in f:
    i+=1

f.close()
print("行数:%d"%i)

"""
$ sdiff <(wc -l hightemp.txt) <(python 10.py) --width=80
24 hightemp.txt                       | 行数:24
"""
