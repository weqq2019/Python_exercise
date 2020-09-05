# *_* coding : UTF-8 *_*
# 开发团队 ： 无
# 开发人员 ： 归零叔
# 开发时间 ： 2020/9/5 11:58
# 文件名称 : 02-实现数据编号的几种方法.PY
# 开发工具 : PyCharm
datasort=[]
i=0
data = '莱科宁 236,汉密尔顿 358,维泰尔 294,维斯塔潘 216,博塔斯 227'
newlist=data.split(',')
print(newlist)
for item in newlist:
    opendata=item.split(' ')
    datasort.append([opendata[1],opendata[0]])
datasort.sort(reverse=True)
print(datasort)
print("\033[1;34m="*35)
print("输出F大将赛车手积分".center(25))
print('排名     车手                 积分')
for item in datasort:
    i=i+1
    print("\033[1;32;41m"+str(i).zfill(2)+"\033[0m     ",item[1].ljust(14)+'\t',item[0].ljust(6)+'\t')
    print()

print("-"*100)
nba=['猛龙','勇士','雄鹿','开拓者','掘金','76人']   # 数据列表
i=0                                                 # 默认编号
for item in nba:
    i=i+1                                           # 递增编号
    data='{:0>2}'.format(i)+ '   '+  item           # 数字补0，填充左边宽度为2
    print(data)                                     # 打印带编号的数据

