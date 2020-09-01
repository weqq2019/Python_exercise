# *_* coding : UTF-8 *_*
# 开发团队 ： 无
# 开发人员 ： 归零叔
# 开发时间 ： 2020/9/1 12:36
# 文件名称 : 05-动态循环输出数字.PY
# 开发工具 : PyCharm
import sys
from time import sleep


def add1(j):
    for n in range(len(j)):
        sleep(0.0001)
        j[n] = j[n] + 1
        sys.stdout.write("\r# Process: %0.1f %%" % (float(n + 1) / float(len(j)) * 100))
    return j

i=[i for i in range(1,10000,1)]
# print(i)
i = add1(i)
