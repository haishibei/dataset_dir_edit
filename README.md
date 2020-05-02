# dataset_dir_edit
This file is set to edit  directory for  storage and edit the labels created by the software 'labelImg'
## 使用步骤如下
### 第一步：
在子数据集中导入1.dir_rename.py，在原数字基础上进行增加或者减少
### 第二步：
在目标文件中，比如/media/data/zhibao_jiao/mydateset/ILSVRC2015/Data/
                      VID/train/ILSVRC2015_VID_train_0000
       导入2.dir_rename.py，对子文件夹进行重命名
### 第三步：对xml文件进行操作
       在目标文件中，比如/media/data/zhibao_jiao/mydateset/ILSVRC2015/
       Annotation/VID/train/ILSVRC2015_VID_train_0000
       导入3.xml_mine_edit.py, 对xml文件修改
### 注：
   文件4.dir_rename.py仅仅是为了对标注文件名不符合的文件修改时使用，例如，统一文件夹名
   称格式为VID， 而标注者的格式为VID*，则进行修改.