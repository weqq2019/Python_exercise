# *_* coding : UTF-8 *_*
# 开发团队 ： 无
# 开发人员 ： 归零叔
# 开发时间 ： 2020/9/8 11:58
# 文件名称 : 05-批量提取文件名保存到一个文件中.PY
# 开发工具 : PyCharm

import os
with open(r'D:\test.txt','a') as f:
    path=input("请输入要提取名称的文件所在路径：")      #以追加方式打开文件
    try:        #记录输入的路径
        list=os.listdir(path)       #遍历选择的文件夹
        for i in range(0,len(list)):        #遍历文件列表
            filename=os.path.splitext(list[i])[0] #提取文件名
            f.write(filename+'\n')   #将提取的文件名写入文本文件
        print("文件名提取完成")
    except:
        print("请输入一个有效路径......")
