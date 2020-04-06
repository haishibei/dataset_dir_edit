from os import listdir, rename
from os.path import join, isdir
import shutil
from glob import glob
"""该文档的作用是将该路径的文件下的特定子文件
复制到指定路径并进行重命名（有前缀，按照数量依次递增）
做法步骤：
1.列举当前路径'./'下的文件夹A_s,取出文件的A，获得文件A的路径A_d
2.抓取A_d下特定文件moving_obj = Annotations/JPEGImages'
3.对文件B进行重命名'ILSVRC2015_train_000000(左补齐，共8位)
将文件复制到其他路径中
"""

# 可修改的变量如下
moving_obj = 'Annotations'   # 1.要移动Annotations（标注）还是JPEGImages（图片数据）

if moving_obj == 'Annotations':
    moving_obj_ = 'Annotations'  # Annotations对应Annotations
elif moving_obj == 'Annotations':
    moving_obj_ = 'Data'         # Annotations对应Data
dst_ = join('/media/data/zhibao_jiao/mydateset/ILSVRC2015', moving_obj_,
            'VID/train/ILSVRC2015_VID_train_0001')      # 2.目标路径

prefix = 'mydataset_train_'         # 3.文件夹前缀
num_start = 10      # 4.起始编号

rec = './'
A_s = listdir(rec)
for vi, A in enumerate(sorted(A_s)):
    if isdir(A):
        A_d = join(rec, A)
        B_s = listdir(A_d)
        for B in B_s:
            B_d = join(A_d, B)
            num = "%08d" % (vi + num_start)
            if str(B) == moving_obj:
                dst = join(dst_, prefix+str(num))
                shutil.copytree(B_d, dst)
                print(prefix + str(num) + 'is finished')