#config:utf-8

# 3行目を取得
col = [line.split('\t')[2] for line in open('hightemp.txt','r')]
new_col = list(set(col))
print('\n'.join(sorted(new_col)))

"""
$ sdiff -w80 <(cut -f3 hightemp.txt | sort | uniq) <(python 18.py)
39.9                                    39.9
40                                      40
40.1                                    40.1
40.2                                    40.2
40.3                                    40.3
40.4                                    40.4
40.5                                    40.5
40.6                                    40.6
40.7                                    40.7
40.8                                    40.8
40.9                                    40.9
41                                      41

"""
