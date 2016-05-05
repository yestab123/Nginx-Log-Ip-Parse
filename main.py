#!/usr/bin/python
#-*- coding:gbk-*-
from ip import IP

ip_list = []

IP.load("normal_ip.dat")

fd = open("ip_parse", "w")

for i in open("log"):
    a = str.split(i, " ")
    if a[0] in ip_list:
        continue
    else:
        ip_list.append(a[0])
        s = a[0] + " " + a[3] + " " + IP.find(a[0]) + "\n"
    b = s.encode("utf")
    fd.write(str(b))

fd.close()

