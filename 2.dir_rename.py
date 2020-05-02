# -*- coding: utf-8 -*-

from os.path import isdir, join
from os import listdir, rename
from glob import glob

"""
本程序的作用是：将文件夹的名称（是数字）减1，并进行左补零(8位对齐)
（下面是删减功能：
可调整的参数如下：
1.num = int(A) - 1， 如果不是减0，可更改为其他数字
  比如改为0，则文件名称（数字）大小不变，仅仅进行形式变换）
"""

rec = './'
A_s = sorted(listdir(rec))
for A in A_s:
    if isdir(A):
        B_s = glob(join(rec, A, '*'))
        for B in B_s:
            num_0 = int(B.split('/')[-1].split('.')[-2])
            suffix = B.split('/')[-1].split('.')[-1]
            num_1 = str("%06d" % (num_0 - 1))
            B_n_d = join(rec, A, num_1 + '.' + suffix)
            rename(B, B_n_d)
            print('{} is finished'.format(B_n_d))

#
# A_s = sorted(listdir(rec))
# for A in A_s:
#     if isdir(A):
#         old = join(rec, A)
#         num = int(A)
#         num = "%08d" % num
#         number = float(num)
#         new = join(rec, 'mydataset_train_' + num)
#         rename(old, new)
#
#         """
#         下面进行迭代
#         将A中的文件名称减1，并进行左补零
#         """