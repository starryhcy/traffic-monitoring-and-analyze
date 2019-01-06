# -*- coding: utf-8 -*-
#samtran
#将样本特征分类
#tranres.dat
import shelve
import numpy as np

#使能够打印全部数组
#np.set_printoptions(threshold = 1e6)

res = [[3,2,7],[1,6,7],[3,15,7],[1,137,7],[3,2000,7],[3,4,7]]
res_labels = [['browser'],['chat'],['mail'],['other'],['other'],['browser']]
tmp1 = []
for i in range(6):
    tmp1.append(np.vstack(tuple(res[i])))

tmp2 = []
for i in tmp1:
    tmp2.append(i.reshape(-1, 3))

final = np.vstack(tuple(tmp2))
final = final.astype(np.float64)

fres = {}
fres['sample'] = final
fres['label'] = res_labels

print fres['sample']
#print  res_labels[615]

savefile = raw_input(
    'Translate have finish,choose a new file to save the result: ')
f = shelve.open(savefile)
f['res'] = fres
f.close()


'''
import shelve
import numpy as np

#使能够打印全部数组
np.set_printoptions(threshold = 1e6)

filename = 'sample.tmp'
dictname = 'dic.dat'

f = shelve.open(filename)
l = len(f['res'])

dictfile = shelve.open(dictname)
dict = dictfile['DICT']

sample = f['res']

res = []
labels = ['browser', 'chat', 'mail', 'others']
res_labels = []

for i in sample:
    tmp = []
    for x in sample[i]:
        if x in dict:
            tmp.append(dict[x])
            if (x == '80' or x == '443'):
                res_labels.append(labels[0])
            elif x == '6000':
                res_labels.append(labels[1])
            elif x == '587':
                res_labels.append(labels[2])
            elif x == '192.168.64.128':
                pass
        else:
        	tmp.append(str(x))
        	res_labels.append(labels[3])
    res.append(tmp)
    
#print res

tmp1 = []
for i in range(l):
    tmp1.append(np.vstack(tuple(res[i])))

tmp2 = []
for i in tmp1:
    tmp2.append(i.reshape(-1, 3))

final = np.vstack(tuple(tmp2))
final = final.astype(np.float64)

fres = {}
fres['sample'] = final
fres['label'] = res_labels

print fres['sample']
#print  res_labels[615]

savefile = raw_input(
    'Translate have finish,choose a new file to save the result: ')
f = shelve.open(savefile)
f['res'] = fres
f.close()
'''