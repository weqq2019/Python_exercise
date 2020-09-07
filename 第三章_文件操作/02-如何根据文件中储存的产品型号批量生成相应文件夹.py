# *_* coding : UTF-8 *_*
# 开发团队 ： 无
# 开发人员 ： 归零叔
# 开发时间 ： 2020/9/7 12:25
# 文件名称 : 02-如何根据文件中储存的产品型号批量生成相应文件夹.PY
# 开发工具 : PyCharm
import os
path2=os.path.split(os.path.realpath(__file__))[0]+'\\'
print(path2)
path = 'D:\\test\\不支持中文\\'
# 以只读方式打开文件
with open(path2+'product.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():  # 读取所有行
        dirpath = path + line.strip()  # 拼接要创建的文件夹路径
        if not os.path.exists(dirpath):  # 判断路径不存在
            os.mkdir(dirpath)  # 创建文件夹
print('创建完成')
os.startfile(path)  # 打开路径
