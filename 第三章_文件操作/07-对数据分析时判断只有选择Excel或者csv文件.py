# *_* coding : UTF-8 *_*
# 开发团队 ： 无
# 开发人员 ： 归零叔
# 开发时间 ： 2020/9/9 11:12
# 文件名称 : 07-对数据分析时判断只有选择Excel或者csv文件.PY
# 开发工具 : PyCharm
def istype(filetype):
    """
    判断是否为Excel或者CSV文件
    :param filetype: 文件扩展名
    :return: 是,返回True,不是,返回False
    """
    filetype=filetype.lower()   #扩展名转换为小写
    if filetype==".xls":
        return True
    elif filetype==".xlsx":
        return True
    elif filetype==".csv":
        return True
    else:
        return False

import os
while True:
    path=input("输入要判断的文件名:")#记录输入的路径
    filetype=os.path.splitext(path)[1]#获取扩展名
    if istype(filetype):
        print("您选择的文件符合数据分析的文件格式......")
    else:
        print("选择的文件不是数据表格格式!")
