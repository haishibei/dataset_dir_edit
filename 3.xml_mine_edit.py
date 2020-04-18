# -*- coding:utf-8 -*-
"""
我要做的工作步骤如下：
循环读取xml文件，取其中一个xml文件
读取父节点（object）
在父节点下创建新的节点，并增加属性与属性值{}，以及字符串内容text
保存，写入
通过这个练习收获如下
1.节点有个要素：tag（标签），attri（属性）、attri[key](属性值)，文本内容（text）
2.得到一个节点parent_node下的所有子节点可以用list（parent_node）
"""
# 创建新的节点使用
from xml.etree.ElementTree import ElementTree, Element
from os.path import isdir, join
from os import listdir


def read_xml(in_path):
    """读取并解析xml文件
      in_path: xml路径
      return: ElementTree"""
    tree = ElementTree()
    tree.parse(in_path)
    return tree


def if_match(node, kv_map):
    """判断某个节点是否包含所有传入参数属性
      node: 节点
      kv_map: 属性及属性值组成的map"""
    for key in kv_map:
        if node.get(key) != kv_map.get(key):
            return False
    return True


def find_nodes(tree, path):
    """查找某个路径匹配的所有节点
      tree: xml树
      path: 节点路径"""
    return tree.findall(path)


def create_node(tag, property_map, content):
    """新造一个节点
      tag:节点标签
      property_map:属性及属性值map
      content: 节点闭合标签里的文本内容
      return 新节点"""
    element = Element(tag, property_map)
    element.text = content
    return element


def get_node_by_keyvalue(nodelist, kv_map):
    """根据属性及属性值定位符合的节点，返回节点
      nodelist: 节点列表
      kv_map: 匹配属性及属性值map"""
    result_nodes = []
    for node in nodelist:
        if if_match(node, kv_map):
            result_nodes.append(node)
    return result_nodes


def write_xml(tree, out_path):
    """将xml文件写出
      tree: xml树
      out_path: 写出路径"""
    tree.write(out_path, encoding="utf-8", xml_declaration=True)


def change_node_text(nodelist, text, is_add=False, is_delete=False):
    """增加/删除/修改 （已存在的）一个节点的文本
      nodelist:节点列表
      text : 更新后的文本"""
    for node in nodelist:
        if is_add:
            node.text += text
        elif is_delete:
            node.text = ""
        else:
            node.text = text


def del_node_by_tagkeyvalue(nodelist, tag):
    """通过属性及属性值定位一个节点，并删除之
      nodelist: 父节点列表
      tag:子节点标签
      kv_map: 属性及属性值列表"""
    for parent_node in nodelist:
        children = parent_node.getchildren()
        for child in children:
            if child.tag == tag:
                parent_node.remove(child)


if __name__ == "__main__":
    """首先循环获取文件路径,操作步骤如下：
    1.获取当前文件的所有文件夹A_s,取其中一个文件夹A，路径为A_d
    2.获取A_d的所有文件B_s, 取出文件B，路径为B_s
    """
    # 1.下面是循环取文件的过程
    rec = './'
    A_s = sorted(listdir(rec))
    for A in A_s:
        if isdir(A):
            A_d = join(rec, A)
            B_s = sorted(listdir(A_d))
            #
            for B in B_s:
                B_d = join(A_d, B)    # B_d是单个xml的路径

                # 读取xml文件并进行相应操作
                tree = read_xml(B_d)

                # TODO 任务1：插入新节点trackid、 occluded
                nodes_1 = find_nodes(tree, "object")

                # # 如果窗口中包含多个目标，进行编号
                vi = 0
                # 插入到父节点之下
                for node in nodes_1:
                    a = create_node("trackid", {}, str(vi))
                    b = create_node("occluded", {}, str(1))
                    node.append(a)
                    node.append(b)
                    vi = int(vi) + 1

                # TODO 任务2修改filename文件名
                # 找到父节点
                nodes_2 = find_nodes(tree, "filename")

                prefix = B.split('.')[0]

                # 得到文件名
                change_node_text(nodes_2, prefix)

                # TODO 任务3 去掉父节点size下的节点（标签）depth
                nodes_3 = find_nodes(tree, "size")
                tag = 'depth'
                del_node_by_tagkeyvalue(nodes_3, tag)

                # TODO 任务4 将标签width与height内的文本交互位置
                """
                我想要做的如下：
                1.找到父节点集size，取出其中一个父节点
                2.得到父节点下子节点width与height，取出其所对应的文本
                3.交换两个文本（删除，并新建）
                """
                nodes_4s = find_nodes(tree, "size")
                for node_4 in nodes_4s:
                    for child in list(node_4):
                        if child.tag == 'width':
                            node_one = child
                            text_one = child.text
                    for child in list(node_4):
                        if child.tag == 'height':
                            node_two = child
                            text_two = child.text
                    node_one.text = text_two
                    node_two.text = text_one

                # TODO 公共输出
                write_xml(tree, B_d)
                print(B_d + 'is finished')
