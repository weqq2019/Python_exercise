# *_* coding : UTF-8 *_*
# 开发团队 ： 无
# 开发人员 ： 归零叔
# 开发时间 ： 2020/9/8 11:31
# 文件名称 : 04-如何调用系统默认程序打开相应文件.PY
# 开发工具 : PyCharm
import os
while True:
    try:
        path=input(r"请输入文件所在路径：")
        os.startfile(path)
    except:
        print("请输入正确的文件路径.......")
