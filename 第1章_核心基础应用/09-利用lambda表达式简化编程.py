# *_* coding : UTF-8 *_*
# 开发团队 ： 无
# 开发人员 ： 归零叔
# 开发时间 ： 2020/9/2 9:53
# 文件名称 : 09-利用lambda表达式简化编程.PY
# 开发工具 : PyCharm

# (1)字符串中的典型应用
num2="1314521"
print('\033[1;31m'+"（1）字符串中的典型应用:"+'\033[0m')
print(max(num2,key=lambda x:abs(int(x))))

#(2)列表中的典型应用
listcar = [[837624,"RAV4"],[791275,"途观"],[651090,"索罗德"],[1080757,"福特F系"],[789519,"高尔夫"],[747646,"CR-V"],[1181445,"卡罗拉"]]
listcha2=['莱科宁 236','汉密尔顿 158','维泰尔 214','维斯塔潘 216','博塔斯 227']
listcha3=['236 莱科宁','358 汉密尔顿','294 维泰尔','216 维斯塔潘','227 博塔斯']
listnba= [['哈登',78,36.8,36.1],['乔治',77,36.9,28.0],['阿德托昆博',72,32.8,27.7],['恩比德',64,33.7,27.5],['詹姆斯',55,35.2,27.4],['库里',69,33.8,27.3]]
listnum=[[2, 141, 126, 277, 323],[3, 241, 171, 404, 296],[1, 101, 128, 278, 123]]
print('\033[1;31m'+"（2）列表中的典型应用:"+'\033[0m')
print(max(listcha2,key=lambda x:x[-3:])) # 输出结果为：莱科宁 236
print(max(listcar))         # 输出结果为：[1181445, '卡罗拉']
print(max(listcar,key=lambda x:x[1]))   # 输出结果为：[789519, '高尔夫']
print(max(listnba,key=lambda x:x[3]))    #输出结果为： ['哈登', 78, 36.8, 36.1]
print(max(listnba,key=lambda x:(x[2],x[1],x[3])))  #输出结果为： ['乔治', 77, 36.9, 28.0]
print(max(listnba,key=lambda x:x[3]*x[1]))    #输出结果为： ['哈登', 78, 36.8, 36.1]
print(max(listnba,key=lambda x:(str(x[3]))[1:]))    #输出结果为：['乔治', 77, 36.9, 28.0]
print(max(listnum,key=lambda x:x[1]+x[2]+x[3]+x[4]))  #输出结果为：[3, 241, 171, 404, 296]

#(3)元组中的典型应用
print('\033[1;31m'+"(3)元组中的典型应用:"+'\033[0m')
tuple1=(2,4,8,16,32,64,128,256,512,1024)         #  数字元组
tuple2=('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec','Mon','Tues','Wed','Thur','Fri') #  月份、星期简写元组
tuple3=('勇士 57','掘金 54','开推者 53','火箭 53','爵士 50','雷霆 49','马刺 48','快船 48')
tuple4=(("肖申克的救赎",1994,9.3),("教父",1972,9.2),("教父2",1974,9.1),("蝙蝠侠：黑暗骑士",2008,9.0),("低俗小说",1994,8.9))   # 电影信息元组
tuple5=((90,128,87.103),(78,99,134.106),(98,102,133.80),(66,78,97,56),(98,123,88.79))
print(max(tuple2,key=lambda x:len(x)))    #  输出元组中长度最大的元组，输出结果为：Sept
print(max(tuple3,key=lambda x:x[-2:]))    #  输出结果为：勇士 57
print(max(tuple4,key=lambda x:x[1]))      #  输出结果为：('蝙蝠侠：黑暗骑士', 2008, 9.0)
print(max(tuple4,key=lambda x:x[2])[0])   #  输出结果为：肖申克的救赎
print(max(max(tuple5,key=lambda x:x[1]))) #  输出结果为：128
print(max(tuple5,key=lambda x:(x[0]+x[1]+x[2])))   #  输出结果为：(98, 102, 133.8)
print(max(tuple5,key=lambda x:(x[0],x[1])))   #  输出结果为：(98, 123, 88.79)

#(4)字典中的典型应用
print('\033[1;31m'+"(4)字典中的典型应用:"+'\033[0m')
dictcar=[{'名称':'卡罗拉','销量':1181445},{'名称':'福特F系','销量':1080757},{'名称':'RAV4','销量':837624},{'名称':'思域','销量':823169},{'名称':'途观','销量':791275}]
dict1 = {'name': 'john', 'age': 23,'money':1200,'gender':'male'}
dict2 = {'name': 'anne', 'age': 22,'money':1500,'gender':'female'}
dict3 = {'name': 'james', 'age': 33,'money':578,'gender':'male'}
dict4 = {'name': 'nick', 'age': 46,'money':158,'gender':'male'}
dict5 = {'name': 'May', 'age': 18,'money':3210,'gender':'female'}    # 创建会员信息字典
lsitdc=[dict1,dict2,dict3,dict4,dict5]      # 创建二维会员信息字典
print(max(dictcar,key=lambda x:x['名称']))  # 输出结果为：{'名称': '途观', '销量': 791275}
# 输出结果为：{'名称': '卡罗拉', '销量': 1181445}
print(max(dictcar,key=lambda x:x['销量']))
# 输出结果为：{'name': 'anne', 'age': 22, 'money': 1500, 'gender': 'female'}
print(max(lsitdc,key=lambda item:(item['gender'] == 'female',item['age'])))
# 将积分超过500的会员年龄最大的会员输出，输出结果为：{'name': 'james', 'age': 33, 'money': 578, 'gender': 'male'}
print(max(lsitdc,key=lambda item:(item['money']>500,item['age'] )))
# 按积分输出最大者，输出结果为：{'name': 'May', 'age': 18, 'money': 3210, 'gender': 'female'}
print(max(lsitdc,key=lambda x:x['money']))
print(max(lsitdc,key=lambda x:x['age']).get('name'))  # 输出结果为：nick
