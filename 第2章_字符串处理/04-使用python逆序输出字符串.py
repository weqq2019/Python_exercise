# *_* coding : UTF-8 *_*
# 开发团队 ： 无
# 开发人员 ： 归零叔
# 开发时间 ： 2020/9/6 12:23
# 文件名称 : 04-使用python逆序输出字符串.PY
# 开发工具 : PyCharm

#1.使用range(函数）
bin20="123456789"
for x in range(len(bin20)-1,-1,-1):
    print(bin20[x],end="")

print()

#2.使用reversed()函数
for x in (reversed(bin20)):
    print(x,end="")

print()

#3.倒序打印输出
for x in bin20[::-1]:
    print(x,end="")