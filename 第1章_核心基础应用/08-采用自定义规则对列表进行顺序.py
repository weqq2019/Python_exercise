# *_* coding : UTF-8 *_*
# 开发团队 ： 无
# 开发人员 ： 归零叔
# 开发时间 ： 2020/9/2 9:45
# 文件名称 : 08-采用自定义规则对列表进行顺序.PY
# 开发工具 : PyCharm
list_dict = [{"name":"无语","python":99,"c":89},
            {"name":"wgh","python":100,"c":80},
            {"name":"琦琦","python":95,"c":97},
            {"name":"明日","python":91,"c":96}]

print('对列表排序前：')
for d in list_dict:
    print(d)

def rulesort(elem):
    return elem['python']

# list_dict.sort(key=rulesort,reverse=True) #排序排列
list_dict.sort(key=lambda x:x['python'],reverse=True) #排序排列(lambda表达式）
print("对列表排序后：")
for d in list_dict:
    print(d)
