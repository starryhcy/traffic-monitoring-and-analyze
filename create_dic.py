# -*- coding: utf-8 -*-
#创建dic.dat
import shelve
propertys = {'6':3, '17':1,'443':4,'80':2,'6000':6,'587':15,'192.168.64.128':7}
save = shelve.open('dic.dat')
save['DICT'] = propertys
save.close()