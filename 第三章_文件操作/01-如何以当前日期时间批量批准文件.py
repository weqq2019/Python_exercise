# *_* coding : UTF-8 *_*
# 开发团队 ： 无
# 开发人员 ： 归零叔
# 开发时间 ： 2020/9/7 11:56
# 文件名称 : 01-如何以当前日期时间批量批准文件.PY
# 开发工具 : PyCharm
import os
import datetime
import time

while True:
    path = input("请输入文件保存地址：")  # 记录文件保存地址
    num = int(input("请输入创建文件的数量："))  # 记录文件创建数量
    # 循环创建文件
    for i in range(num):
        t = datetime.datetime.now()  # 获取当前时间
        # 对当前日期时间进行格式化,作为文件名
        print(t.strftime('%Y%m%d%H%M%S'))
        print(path)
        file = os.path.join(path, t.strftime('%Y%m%d%H%M%S') + 'txt')
        open(file, 'w', encoding='utf-8')  # 以UTF-8编码创建文件
        time.sleep(1)
        i += 1  # 循环标识加1
    print('创建成功')
    os.startfile(path)  # 打开路径查看

