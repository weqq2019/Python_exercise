# *_* coding : UTF-8 *_*
# 开发团队 ： 无
# 开发人员 ： 归零叔
# 开发时间 ： 2020/9/6 13:05
# 文件名称 : 07-如何生成高考填报志愿时的姓名区位码.PY
# 开发工具 : PyCharm
def getCode(chinaese):
    '''
    获取汉字的对应区位码
    :param chinaese:单个汉字
    :return:获取到的区位码
    '''
    barray = chinaese.encode('gb2312')
    # 计算区位码（如果是1位,则格式为2位）
    code = '{0:02d}'.format((barray[0] - 160)) + '{0:02d}'.format((barray[1] - 160))
    return code

while True:
    name=input("请输入姓名：")
    for word in name:
        print(word,":",getCode(word))