# *_* coding : UTF-8 *_*
# 开发团队 ： 无
# 开发人员 ： 归零叔
# 开发时间 ： 2020/9/9 11:23
# 文件名称 : 08-如何像资源管理器一样显示指定文件下的所有子文件夹及文件.PY
# 开发工具 : PyCharm

import os
while True:
    path=input("请输入一个路径:")
    try:
        list=os.listdir(path)
        filenames=[]
        dirnames=[]
        for i in range(0,len(list)):
            filepath=os.path.join(path,list[i])
            if os.path.isdir(filepath):
                dirnames.append(list[i])
            elif os.path.isfile(filepath):
                filenames.append(list[i])
        print('\033[1;42m------文件夹列表------\033[0m')
        for dirname in dirnames:
            print(' ',dirnames)
        print('\033[1;42m------文件列表------\033[0m')
        for filename in filenames:
            print(' ', filenames)
    except:
        print("请输入一个有效路径")