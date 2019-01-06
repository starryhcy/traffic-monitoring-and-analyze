# -*- coding: utf-8 -*-
#gentran

import shelve
import random
import numpy as np

filename = raw_input('Enter the property file: ')
dictname = raw_input('Enter the dictionary file: ')

dic_tmp = shelve.open(dictname)
dic = dic_tmp['DICT']
raw_file = shelve.open(filename)
raw = raw_file['res']
l = len(raw)
res = []

for i in raw:
    tmp = []
    for j in raw[i]:
        if j in dic:
            tmp.append(dic[j])
        else:
            tmp.append(int(j))
    res.append(tmp)
#print res

tmp1 = []
for i in range(l):
    tmp1.append(np.vstack(tuple(res[i])))

tmp2 = []
for i in tmp1:
    tmp2.append(i.reshape(-1, 3))

final = np.vstack(tuple(tmp2))

savefile = raw_input(
    'Translate have finish,choose a new file to save the result: ')
temp = shelve.open(savefile)
temp['res'] = final
temp.close()