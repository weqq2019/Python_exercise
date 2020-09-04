# *_* coding : UTF-8 *_*
# 开发团队 ： 无
# 开发人员 ： 归零叔
# 开发时间 ： 2020/9/4 10:14
# 文件名称 : 11-拼接字符串、列表和字典.PY
# 开发工具 : PyCharm

#方法1：使用加号"+" 连接字符串
data='www.'+'baidu.'+'com'
print(data)
train1='www.'+'12306'+'.com'
train2='www.'+str(12306)+'.com'
print(train1)
print(train2)

#方法2：使用逗号连接字符串
name=input('姓名：')
phone=input('电话：')
university=input('学校：')
data=name,phone,university
print(data)
print(' '.join(data))

#方法3：直接连接字符串
print('baidu''.com')

#方法4:通过"%"连接字符串
print("%s %s"%('baidu','taobao'))