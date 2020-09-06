# *_* coding : UTF-8 *_*
# 开发团队 ： 无
# 开发人员 ： 归零叔
# 开发时间 ： 2020/9/6 12:37
# 文件名称 : 05-如何生成虚拟姓名.PY
# 开发工具 : PyCharm

import random
surname="李刘王孙周吴冯陈蒋龙许张涂"
second="泉建於宇文海春"
#第三位名字库
thrid="娟峰"
surname_new=surname.split(",")
second_new=second.split(",")
thrid_new=thrid.split(",")
namelist=[]
many=input("请输入需要生成姓名的数量：\n")
for i in range(int(many)):
    data=[2,3]
    namelen=random.choice(data)
    if namelen==2:
        newname=random.choice(surname)+random.choice(second)
    else:
        newname=random.choice(surname)+random.choice(second)+random.choice(thrid)
    namelist.append(newname)
print('生成的虚拟姓名列表：\n'+'\n'.join(namelist))
