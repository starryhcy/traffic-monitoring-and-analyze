# -*- coding: utf-8 -*-
# extra
#提取测试集特征
from scapy.all import *
import shelve

pcap = raw_input("Enter pcap file path and name: ")
#pcap = 'http.pcap'
file = rdpcap(pcap)
lines = len(file)
#print file

raw_pkt = {}
for i in range(lines):
    raw_pkt[i] = file[i]

propertys = {}
for i in range(lines):
    try:
        if(raw_pkt[i].proto == 6 or raw_pkt[i].proto == 17):
            if ((raw_pkt[i]['IP'].src =='192.168.64.128') and 'Raw' in raw_pkt[i]):
                #print 'yes'
                propertys[i + 1] = []
                propertys[i + 1].append(str(raw_pkt[i].proto))
                propertys[i + 1].append(str(raw_pkt[i].dport))
                propertys[i + 1].append(raw_pkt[i]['IP'].src)
    except AttributeError:
        continue

print('Extraction have finished')
name = raw_input("Please use a new file to save it: ")
save = shelve.open(name)
save['res'] = propertys
save.close()