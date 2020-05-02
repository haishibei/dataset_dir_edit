from os.path import isdir, join
from os import listdir, rename

"""
1.本程序的作用是：修改文件夹的名称， 并且在原基础上将序号增加
经过这一步可以进行1.dir_move_rename.py操作
2.将文件1.dir_move_rename.py放入该文件夹，修改后运行
"""

rec = './'
A_s = sorted(listdir(rec))
for A in A_s:
    if str(A).split('D')[0] == 'VI':
        num = int(str(A).split('D')[-1]) + 368
        A_n = str(A).split('D')[0] + 'D' + str(num)
        rename(A, A_n)
