#config:utf-8

i = 0
f = open('hightemp.txt','r')
for line in f:
    i+=1

print("行数:%d"%i)
