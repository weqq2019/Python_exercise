# *_* coding : UTF-8 *_*
# 开发团队 ： 无
# 开发人员 ： 归零叔
# 开发时间 ： 2020/9/9 11:34
# 文件名称 : 09-如何对运营数据文件进行分类整理.PY
# 开发工具 : PyCharm
import os
import shutil
while True:
    path=input("请输入要整理文件所在路径:")
    # try:
    list=os.listdir(path)
    for i in range(0,len(list)):
        filepath=os.path.join(path,list[i])
        dirname=list[i][0:3] #获取文件名的前3个字符串,用来作为文件夹名
        dirpath=os.path.join(path,dirname)  #拼接文件夹路径
        print(dirname)
        if not os.path.exists(dirpath): #判断文件夹路径是否存在
            print(dirpath)
            os.mkdir(dirpath)
        shutil.move(filepath,os.path.join(dirpath,list[i]))
    print("整理完成")
    # except:
    #     print("有输入一个有效路径......")
