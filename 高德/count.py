# coding=utf-8
file_name = 'file/gaode_hk.txt'
with open(file_name,'r',encoding='utf-8') as f:
    idx = 0
    for zuobiao in f:
        idx +=1
    print('总数%d'%idx)

