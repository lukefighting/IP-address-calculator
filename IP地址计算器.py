# -*- coding: UTF-8 -*-
#__author__ = 'Luke'

from netaddr import *
import os

while True:
    # divi = input("\n请输入要进行查询的地址（示例：192.168.1.52/27）:\n\n")
    # input()
    # ip = IPNetwork(divi)
    # yjma = ip.prefixlen
    ipx = input("\n请输入要进行查询的地址（示例：192.168.1.52）:\n\n")
    yjma = int(input("\n请输入要进行查询的地址的掩码（示例：27）:\n\n"))
    ip = IPNetwork(ipx)
    ip.prefixlen = int(yjma)
    
    ip_list = list(ip)
    print('\n要查询的IP地址：',ip.ip,',掩码：',yjma)
    print('\n','=*='*10)
    print('\n开始地址---结束地址：',end='')
    print(ip_list[0],'-',ip_list[ip.size-1])
    print('\n地址数量：',ip.size)
    if yjma > 24:
        print('\n以下列举该C段内，掩码为' + str(yjma) + '的全部地址段(开始地址---结束地址)：\n')
        ipi = IPNetwork(ip.ip)
        ipi.prefixlen = 24
        ipi_list = list(ipi)
        for i in range(2**(yjma-24)):
            print('第',i+1,'段 : ',end='')
            print(ipi_list[i*int(ip.size)],'-',ipi_list[(i+1)*int(ip.size)-1])
    print('\n\n')
    os.system('pause')
    os.system('cls')




